import json
from pathlib import Path
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import text
from datetime import date

from aplicacao.db.models import Livro, Usuario, Emprestimo

# -------------------------------------------------------------
# Caminhos
# -------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "dados"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "biblioteca.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

LIVROS_JSON = DATA_DIR / "livros.json"
USUARIOS_JSON = DATA_DIR / "usuarios.json"
EMPRESTIMO_JSON = DATA_DIR / "emprestimo.json"

# -------------------------------------------------------------
# Engine
# -------------------------------------------------------------
engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)

# -------------------------------------------------------------
# Criar tabelas
# -------------------------------------------------------------
def criar_tabelas():
    SQLModel.metadata.create_all(engine)

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def criar_indices():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Parse de datas
# -------------------------------------------------------------
def parse_date(value):
    if value is None:
        return None
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def carregar_seed():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Inicializar banco (startup)
# -------------------------------------------------------------
def inicializar_banco():
    criar_tabelas()
    criar_indices()
    carregar_seed()

# -------------------------------------------------------------
# Resetar banco (rollback para testes)
# -------------------------------------------------------------
def resetar_banco():
    from aplicacao.db.sessao import engine as eng

    # fecha conexões
    eng.dispose()

    import time
    time.sleep(0.3)  # Windows precisa disso para soltar o arquivo

    # apaga arquivo antigo
    if DB_PATH.exists():
        try:
            DB_PATH.unlink()
        except PermissionError:
            time.sleep(0.5)
            DB_PATH.unlink()

    # recria tabelas
    SQLModel.metadata.create_all(eng)
