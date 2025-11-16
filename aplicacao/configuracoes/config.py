from pydantic import BaseModel
from pathlib import Path

# --------------------------------------------------------------
# Caminhos base da aplicação
# --------------------------------------------------------------
RAIZ_PROJETO = Path(__file__).resolve().parents[2]
CAMINHO_DB = RAIZ_PROJETO / "db" / "biblioteca.db" #Projeto de Testes\db\biblioteca.db
CAMINHO_DADOS = RAIZ_PROJETO / "dados" #Projeto de Testes\dados

# --------------------------------------------------------------
# URL do banco
# --------------------------------------------------------------
URL_BANCO_DADOS = f"sqlite:///{str(CAMINHO_DB)}"

# --------------------------------------------------------------
# Modelo de Configurações
# --------------------------------------------------------------
class Configuracoes(BaseModel):
    multa_por_dia: float = 1.50
    max_emprestimos_ativos: int = 3

# Configuração global carregada
config = Configuracoes()


# --------------------------------------------------------------
# Validar se as estruturas bases existem
# --------------------------------------------------------------
def validar_estrutura() -> None:
    if not CAMINHO_DADOS.exists():
        raise RuntimeError(f"Pasta de dados não encontrada: {CAMINHO_DADOS}")

    if not CAMINHO_DB.parent.exists():
        raise RuntimeError(f"Pasta do banco não encontrada: {CAMINHO_DB.parent}")

