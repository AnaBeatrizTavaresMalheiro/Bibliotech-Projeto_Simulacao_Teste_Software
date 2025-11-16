import pytest
import os
from pathlib import Path

from aplicacao.configuracoes.config import (
    Configuracoes,
    URL_BANCO_DADOS,
    CAMINHO_DB,
    CAMINHO_DADOS,
    validar_estrutura
)


# ================================================================
# TESTES DO MODELO DE CONFIGURAÇÕES
# ================================================================
def test_configuracoes_default():
    cfg = Configuracoes()
    assert cfg.multa_por_dia == 1.50
    assert cfg.max_emprestimos_ativos == 3


def test_configuracoes_env_override(monkeypatch):
    monkeypatch.setenv("MULTA_POR_DIA", "2.5")
    monkeypatch.setenv("MAX_EMPRESTIMOS_ATIVOS", "5")

    cfg = Configuracoes(
        multa_por_dia=float(os.getenv("MULTA_POR_DIA")),
        max_emprestimos_ativos=int(os.getenv("MAX_EMPRESTIMOS_ATIVOS")),
    )

    assert cfg.multa_por_dia == 2.5
    assert cfg.max_emprestimos_ativos == 5


# ================================================================
# TESTE DO CAMINHO / URL DE BANCO
# ================================================================
def test_url_banco_dados_ok():
    caminho_normalizado = str(CAMINHO_DB).replace("\\", "/")
    url_normalizada = URL_BANCO_DADOS.replace("\\", "/")

    assert url_normalizada.startswith("sqlite:///")
    assert caminho_normalizado in url_normalizada


# ================================================================
# TESTE DA VALIDAÇÃO DE ESTRUTURA — CAMINHO FELIZ
# ================================================================
def test_validar_estrutura_ok(tmp_path, monkeypatch):
    pasta_dados = tmp_path / "dados"
    pasta_dados.mkdir()

    pasta_db = tmp_path / "db"
    pasta_db.mkdir()

    arquivo_db = pasta_db / "biblioteca.db"
    arquivo_db.touch()

    monkeypatch.setattr("aplicacao.configuracoes.config.CAMINHO_DADOS", pasta_dados)
    monkeypatch.setattr("aplicacao.configuracoes.config.CAMINHO_DB", arquivo_db)

    validar_estrutura()  # não deve lançar erro


# ================================================================
# TESTE — FALTA PASTA DE DADOS
# ================================================================
def test_validar_estrutura_falta_pasta_dados(tmp_path, monkeypatch):
    pasta_dados_inexistente = tmp_path / "dados"

    pasta_db = tmp_path / "db"
    pasta_db.mkdir()
    arquivo_db = pasta_db / "biblioteca.db"
    arquivo_db.touch()

    monkeypatch.setattr("aplicacao.configuracoes.config.CAMINHO_DADOS", pasta_dados_inexistente)
    monkeypatch.setattr("aplicacao.configuracoes.config.CAMINHO_DB", arquivo_db)

    with pytest.raises(RuntimeError):
        validar_estrutura()


# ================================================================
# TESTE — FALTA PASTA DO BANCO
# ================================================================
def test_validar_estrutura_falta_pasta_banco(tmp_path, monkeypatch):
    pasta_dados = tmp_path / "dados"
    pasta_dados.mkdir()

    arquivo_db = tmp_path / "inexistente" / "biblioteca.db"

    monkeypatch.setattr("aplicacao.configuracoes.config.CAMINHO_DADOS", pasta_dados)
    monkeypatch.setattr("aplicacao.configuracoes.config.CAMINHO_DB", arquivo_db)

    with pytest.raises(RuntimeError):
        validar_estrutura()
