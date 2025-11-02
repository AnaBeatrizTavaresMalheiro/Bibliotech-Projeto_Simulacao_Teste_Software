from typing import Optional, List
from datetime import date
from sqlmodel import SQLModel, Field, Relationship

class Livro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    isbn: str
    disponivel: bool = True

    emprestimos: List["Emprestimo"] = Relationship(back_populates="livro")

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str
    qtd_emprestimo: int = 0
    possui_multa_aberta: bool = False

    emprestimos: List["Emprestimo"] = Relationship(back_populates="usuario")


class Emprestimo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    livro_id: int = Field(foreign_key="livro.id")
    usuario_id: int = Field(foreign_key="usuario.id")
    data_emprestimo: date
    data_devolucao_prevista: date
    data_devolucao_real: Optional[date] = None
    dias_atraso: int = 0
    valor_multa: float = 0.0

    livro: Livro = Relationship(back_populates="emprestimos")
    usuario: Usuario = Relationship(back_populates="emprestimos")
