from typing import Optional, List
from datetime import date
from sqlmodel import SQLModel, Field, Relationship

# ============================================================
# Modelo Livro
# Representa um registro da tabela 'livro'
# ============================================================
class Livro(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    isbn: str
    disponivel: bool = True


# ============================================================
# Modelo Usuario
# Representa um usuário que pode pegar livros emprestados
# ============================================================
class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str
    qtd_emprestimo: int = 0
    possui_multa_aberta: bool = False

# ============================================================
# Modelo Emprestimo
# Tabela de junção entre Livro e Usuário
# Representa cada empréstimo realizado
# ============================================================
class Emprestimo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    livro_id: int = Field(foreign_key="livro.id")
    usuario_id: int = Field(foreign_key="usuario.id")

    data_emprestimo: date
    data_devolucao_prevista: date
    data_devolucao_real: Optional[date] = None

    dias_atraso: int = 0
    valor_multa: float = 0.0
