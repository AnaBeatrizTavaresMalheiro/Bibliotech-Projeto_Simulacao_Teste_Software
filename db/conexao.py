# db/conexao.py
from pathlib import Path
from sqlmodel import create_engine, Session

# >>> MESMO cálculo de caminho do criar_schemas.py <<<
ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "biblioteca.db"   # único ponto de verdade

DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

# Para SQLite + FastAPI, desabilite check_same_thread
motor = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

def obter_sessao():
    with Session(motor) as sess:
        yield sess
