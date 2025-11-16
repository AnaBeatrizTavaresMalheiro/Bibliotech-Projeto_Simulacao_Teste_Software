# db/conexao.py
from pathlib import Path
from sqlmodel import create_engine, Session

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "data" / "biblioteca.db"

print("📁 Usando banco em:", DB_PATH)


DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

# Para SQLite + FastAPI, desabilite check_same_thread
motor = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

def obter_sessao():
    with Session(motor) as sess:
        yield sess

from sqlmodel import create_engine

def criar_engine(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" in url else {}
    return create_engine(url, echo=echo, connect_args=connect_args)
