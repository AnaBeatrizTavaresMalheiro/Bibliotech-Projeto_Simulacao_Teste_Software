from sqlmodel import SQLModel
from db.conexao import motor

def inicializar_banco():
    SQLModel.metadata.create_all(motor)
