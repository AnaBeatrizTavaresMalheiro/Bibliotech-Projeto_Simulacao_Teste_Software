# server/routers/livros_router.py
from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlmodel import Session, select

from aplicacao.db.sessao import get_session
from aplicacao.db.models import Livro, Emprestimo
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado, ErroDeRegraNegocio
from pydantic import BaseModel, Field


router = APIRouter()
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


# DTOs ----------------------------------------------

class LivroIn(BaseModel):
    titulo: str = Field(..., min_length=1)
    isbn: str = Field(..., min_length=5)
    disponivel: Optional[bool] = True


class LivroOut(BaseModel):
    id: int
    titulo: str
    isbn: str
    disponivel: bool


class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    isbn: Optional[str] = None
    disponivel: Optional[bool] = None


# ROTAS -------------------------------------------

@router.post("/", response_model=LivroOut, status_code=201)
def criar_livro(payload: LivroIn, sessao: Session = Depends(get_session)):
    livro = Livro(**payload.dict())
    sessao.add(livro)
    sessao.commit()
    sessao.refresh(livro)
    return livro


@router.get("/", response_model=List[LivroOut])
def listar_livros(
    ordenar_por: str = Query(default="id"),
    ordem: str = Query(default="asc"),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    sessao: Session = Depends(get_session)
):
    colunas = {
        "id": Livro.id,
        "titulo": Livro.titulo,
        "isbn": Livro.isbn,
        "disponivel": Livro.disponivel,
    }
    coluna = colunas.get(ordenar_por, Livro.id)

    stmt = select(Livro).order_by(
        coluna.desc() if ordem == "desc" else coluna.asc()
    ).offset(offset).limit(limit)

    return sessao.exec(stmt).all()


@router.patch("/{livro_id}", response_model=LivroOut)
def atualizar_livro(livro_id: int, payload: LivroUpdate, sessao: Session = Depends(get_session)):
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroNaoEncontrado("Livro não encontrado.")

    dados = payload.model_dump(exclude_unset=True)
    for campo, valor in dados.items():
        setattr(livro, campo, valor)

    sessao.commit()
    sessao.refresh(livro)
    return livro


@router.delete("/{livro_id}", status_code=204)
def remover_livro(livro_id: int, sessao: Session = Depends(get_session)):
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroNaoEncontrado("Livro não encontrado.")

    ativo = sessao.exec(
        select(Emprestimo).where(
            Emprestimo.livro_id == livro_id,
            Emprestimo.data_devolucao_real.is_(None)
        )
    ).first()

    if ativo:
        raise ErroDeRegraNegocio("Livro possui empréstimo ativo; não pode ser deletado.")

    sessao.delete(livro)
    sessao.commit()
