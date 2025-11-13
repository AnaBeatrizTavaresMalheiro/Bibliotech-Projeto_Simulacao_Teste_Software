import sqlite3
import tempfile
from pathlib import Path
import json
import pytest
from src.db.criar_schemas import CriadorDeSchemasBiblioteca

@pytest.fixture
def db_temp():
    """Cria um banco SQLite temporário para teste de integração."""
    with tempfile.TemporaryDirectory() as tmpdir:
        caminho_db = Path(tmpdir) / "test_biblioteca.db"
        criador = CriadorDeSchemasBiblioteca(caminho_db)
        criador.abrir()
        yield criador
        criador.fechar()


def test_abre_e_fecha_conexao(db_temp):
    assert isinstance(db_temp.conexao, sqlite3.Connection)
    db_temp.fechar()
    assert db_temp.conexao is None


def test_criar_tabelas(db_temp):
    db_temp.criar_tabelas()
    tabelas = [r[0] for r in db_temp.conexao.execute(
        "SELECT name FROM sqlite_master WHERE type='table';")]
    assert set(["livro", "usuario", "emprestimo"]).issubset(tabelas)


def test_criar_indices(db_temp):
    db_temp.criar_tabelas()
    db_temp.criar_indices()
    indices = [r[0] for r in db_temp.conexao.execute(
        "SELECT name FROM sqlite_master WHERE type='index';")]
    assert any("ix_livro_titulo" in i for i in indices)


def test_tabela_vazia_true(db_temp):
    db_temp.criar_tabelas()
    assert db_temp._tabela_vazia("livro") is True


def test_tabela_vazia_false(db_temp):
    db_temp.criar_tabelas()
    db_temp.conexao.execute("INSERT INTO livro (titulo, isbn) VALUES ('Teste', '123');")
    db_temp.conexao.commit()
    assert db_temp._tabela_vazia("livro") is False


def test_inserir_seed_sem_json(db_temp):
    db_temp.criar_tabelas()
    # Sem arquivos JSON -> deve rodar mas não quebrar
    db_temp.inserir_seed_se_vazio()
    assert db_temp._tabela_vazia("livro") is False


def test_inserir_seed_com_json(tmp_path):
    # Cria arquivos JSON falsos
    livros = [{"titulo": "Livro Teste", "isbn": "999"}]
    usuarios = [{"nome": "Usuário Teste", "email": "u@t.com"}]
    emprestimos = [{
        "livro_id": 1, "usuario_id": 1,
        "data_emprestimo": "2024-01-01",
        "data_devolucao_prevista": "2024-01-10"
    }]

    livros_json = tmp_path / "livros.json"
    usuarios_json = tmp_path / "usuarios.json"
    emprestimos_json = tmp_path / "emprestimos.json"

    for path, data in [(livros_json, livros), (usuarios_json, usuarios), (emprestimos_json, emprestimos)]:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f)

    # Substitui caminhos globais do módulo temporariamente
    from src.db import criar_schemas
    criar_schemas.LIVROS_JSON = livros_json
    criar_schemas.USUARIOS_JSON = usuarios_json
    criar_schemas.EMPRESTIMO_JSON = emprestimos_json

    criador = CriadorDeSchemasBiblioteca(tmp_path / "test.db")
    criador.abrir()
    criador.criar_tabelas()
    criador.inserir_seed_se_vazio()

    qtd_livros = criador.conexao.execute("SELECT COUNT(*) FROM livro;").fetchone()[0]
    assert qtd_livros == 1


def test_reexecutar_seed_nao_duplica(db_temp):
    db_temp.criar_tabelas()
    db_temp.conexao.execute("INSERT INTO livro (titulo, isbn) VALUES ('Teste', '123');")
    db_temp.conexao.commit()
    db_temp.inserir_seed_se_vazio()
    qtd = db_temp.conexao.execute("SELECT COUNT(*) FROM livro;").fetchone()[0]
    assert qtd == 1  # não duplicou


def test_excecao_em_criar_tabelas(db_temp):
    db_temp.conexao.execute("CREATE TABLE livro(id INTEGER PRIMARY KEY);")
    db_temp.conexao.commit()
    # Força erro duplicado (já existe)
    db_temp.criar_tabelas()
    assert True  # Não deve lançar erro irrecuperável


def test_fluxo_completo_integrado(tmp_path):
    """Fluxo completo: abre, cria tabelas, índices e insere seeds."""
    criador = CriadorDeSchemasBiblioteca(tmp_path / "biblioteca_int.db")
    criador.abrir()
    criador.criar_tabelas()
    criador.criar_indices()
    criador.inserir_seed_se_vazio()
    criador.fechar()
    assert not criador.conexao
