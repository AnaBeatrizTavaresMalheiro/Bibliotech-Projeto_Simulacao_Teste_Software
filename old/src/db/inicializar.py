
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sqlmodel import SQLModel
from src.db.conexao import motor

def inicializar_banco():
    SQLModel.metadata.create_all(motor)
