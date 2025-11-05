import json
import sqlite3
from pathlib import Path
from typing import Optional, List

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "biblioteca.db"
DATA_DIR = ROOT_DIR / "data"
LIVROS_JSON = DATA_DIR / "livros.json"
USUARIOS_JSON = DATA_DIR / "usuarios.json"
EMPRESTIMO_JSON = DATA_DIR / "emprestimo.json"

class CriadorDeSchemasBiblioteca:
    def __init__(self, caminho_db: Path = DB_PATH) -> None:
        self.caminho_db: Path = caminho_db
        self.conexao: Optional[sqlite3.Connection] = None

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def abrir(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, check_same_thread=False)
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    def fechar(self) -> None:
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            print("[OK] Conexão fechada.")

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def criar_tabelas(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def criar_indices(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # SEED — INSERIR DADOS SE VAZIO
    # ----------------------------------------------------------
    def _tabela_vazia(self, nome_tabela: str) -> bool:
        assert self.conexao
        cur = self.conexao.execute(f"SELECT 1 FROM {nome_tabela} LIMIT 1;")
        return cur.fetchone() is None

    def inserir_seed_se_vazio(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def mostrar_resumo(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(" -", nome)


# --- Funções de fachada para usar no FastAPI ---

def inicializar_banco() -> None:
    """
    Cria tabelas e índices. Não insere dados.
    Útil para ser chamado no evento de startup da API.
    """
    ddl = CriadorDeSchemasBiblioteca()
    ddl.abrir()
    ddl.criar_tabelas()
    ddl.criar_indices()
    ddl.fechar()
    print("[OK] Banco inicializado (tabelas + índices).")

def carregar_seed_se_vazio() -> None:
    """
    Insere dados do data/livros.json e data/usuarios.json
    apenas se as tabelas estiverem vazias.
    """
    ddl = CriadorDeSchemasBiblioteca()
    ddl.abrir()
    ddl.inserir_seed_se_vazio()
    ddl.fechar()



# ----------------------------------------------------------
# EXECUÇÃO DIRETA
# ----------------------------------------------------------
if __name__ == "__main__":
    ddl = CriadorDeSchemasBiblioteca()
    ddl.abrir()
    ddl.criar_tabelas()
    ddl.criar_indices()
    ddl.inserir_seed_se_vazio()
    ddl.mostrar_resumo()
    ddl.fechar()



# debug

# from pydantic import BaseModel, EmailStr, constr

# class UsuarioIn(BaseModel):
#     nome: constr(min_length=1)        # pelo menos 1 caractere
#     email: EmailStr                    # valida formato de e-mail
    
    