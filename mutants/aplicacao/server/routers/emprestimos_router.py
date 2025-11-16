# aplicacao/server/routers/emprestimos_router.py

from datetime import date
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from aplicacao.db.sessao import get_session
from aplicacao.db.models import Emprestimo, Usuario, Livro
from aplicacao.regras_negocio.regras_emprestimo import (
    validar_usuario_para_emprestimo,
    garantir_livro_disponivel,
    processar_devolucao,
)
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado

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


@router.post("/", status_code=201)
def criar_emprestimo(dados: dict, session: Session = Depends(get_session)):

    usuario_id = dados["usuario_id"]
    livro_id = dados["livro_id"]
    data_emprestimo = date.fromisoformat(dados["data_emprestimo"])
    data_prevista = date.fromisoformat(dados["data_devolucao_prevista"])

    # regras de negócio
    validar_usuario_para_emprestimo(session, usuario_id)
    garantir_livro_disponivel(session, livro_id)

    emp = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_prevista,
    )

    session.add(emp)

    # Atualiza contador do usuário e disponibilidade do livro
    usuario = session.get(Usuario, usuario_id)
    livro = session.get(Livro, livro_id)

    usuario.qtd_emprestimo += 1
    livro.disponivel = False

    session.commit()
    session.refresh(emp)

    return emp


@router.post("/{emprestimo_id}/devolucao")
def devolver_emprestimo(emprestimo_id: int, dados: dict, session: Session = Depends(get_session)):
    emprestimo = session.get(Emprestimo, emprestimo_id)
    if not emprestimo:
        raise ErroNaoEncontrado("Empréstimo não encontrado.")

    data_real = date.fromisoformat(dados["data_devolucao_real"])

    processar_devolucao(session, emprestimo, data_real)
    session.commit()
    session.refresh(emprestimo)

    return emprestimo


@router.get("/")
def listar_emprestimos(session: Session = Depends(get_session)):
    return session.exec(select(Emprestimo)).all()
