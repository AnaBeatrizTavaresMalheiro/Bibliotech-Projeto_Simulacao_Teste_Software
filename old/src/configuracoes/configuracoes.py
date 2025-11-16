# configuracoes/config.py
from pydantic import BaseModel
from pathlib import Path

CAMINHO_DB = Path(__file__).resolve().parents[2] / "biblioteca.db"
URL_BANCO_DADOS = f"sqlite:///{CAMINHO_DB}"

class Configuracoes(BaseModel):
    # ESTE NOME PRECISA EXISTIR, pois o main.py usa config.nome_app
    nome_app: str = "Sistema de Empréstimos da Biblioteca"
    multa_por_dia: float = 1.50
    max_emprestimos_ativos: int = 3

config = Configuracoes()

