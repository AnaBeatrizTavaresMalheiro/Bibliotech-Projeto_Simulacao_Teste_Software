from sqlmodel import Session
from sqlalchemy import select
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio
from aplicacao.db.models import Usuario
import types
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


def x__ensure_session__mutmut_orig(sessao):
    """
    Garante que 'sessao' seja um objeto Session e não um generator.
    Isso protege contra mutações do Mutmut e usos incorretos.
    """
    if isinstance(sessao, types.GeneratorType):
        sessao = next(sessao)
    return sessao


def x__ensure_session__mutmut_1(sessao):
    """
    Garante que 'sessao' seja um objeto Session e não um generator.
    Isso protege contra mutações do Mutmut e usos incorretos.
    """
    if isinstance(sessao, types.GeneratorType):
        sessao = None
    return sessao


def x__ensure_session__mutmut_2(sessao):
    """
    Garante que 'sessao' seja um objeto Session e não um generator.
    Isso protege contra mutações do Mutmut e usos incorretos.
    """
    if isinstance(sessao, types.GeneratorType):
        sessao = next(None)
    return sessao

x__ensure_session__mutmut_mutants : ClassVar[MutantDict] = {
'x__ensure_session__mutmut_1': x__ensure_session__mutmut_1, 
    'x__ensure_session__mutmut_2': x__ensure_session__mutmut_2
}

def _ensure_session(*args, **kwargs):
    result = _mutmut_trampoline(x__ensure_session__mutmut_orig, x__ensure_session__mutmut_mutants, args, kwargs)
    return result 

_ensure_session.__signature__ = _mutmut_signature(x__ensure_session__mutmut_orig)
x__ensure_session__mutmut_orig.__name__ = 'x__ensure_session'


def x_garantir_usuario_existe__mutmut_orig(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_1(sessao: Session, usuario_id: int) -> Usuario:
    sessao = None

    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_2(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(None)

    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_3(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = None
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_4(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(None, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_5(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(Usuario, None)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_6(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_7(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(Usuario, )
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_8(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(Usuario, usuario_id)
    if usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_9(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio(None)
    return usuario


def x_garantir_usuario_existe__mutmut_10(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("XXUsuário não encontrado.XX")
    return usuario


def x_garantir_usuario_existe__mutmut_11(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("usuário não encontrado.")
    return usuario


def x_garantir_usuario_existe__mutmut_12(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("USUÁRIO NÃO ENCONTRADO.")
    return usuario

x_garantir_usuario_existe__mutmut_mutants : ClassVar[MutantDict] = {
'x_garantir_usuario_existe__mutmut_1': x_garantir_usuario_existe__mutmut_1, 
    'x_garantir_usuario_existe__mutmut_2': x_garantir_usuario_existe__mutmut_2, 
    'x_garantir_usuario_existe__mutmut_3': x_garantir_usuario_existe__mutmut_3, 
    'x_garantir_usuario_existe__mutmut_4': x_garantir_usuario_existe__mutmut_4, 
    'x_garantir_usuario_existe__mutmut_5': x_garantir_usuario_existe__mutmut_5, 
    'x_garantir_usuario_existe__mutmut_6': x_garantir_usuario_existe__mutmut_6, 
    'x_garantir_usuario_existe__mutmut_7': x_garantir_usuario_existe__mutmut_7, 
    'x_garantir_usuario_existe__mutmut_8': x_garantir_usuario_existe__mutmut_8, 
    'x_garantir_usuario_existe__mutmut_9': x_garantir_usuario_existe__mutmut_9, 
    'x_garantir_usuario_existe__mutmut_10': x_garantir_usuario_existe__mutmut_10, 
    'x_garantir_usuario_existe__mutmut_11': x_garantir_usuario_existe__mutmut_11, 
    'x_garantir_usuario_existe__mutmut_12': x_garantir_usuario_existe__mutmut_12
}

def garantir_usuario_existe(*args, **kwargs):
    result = _mutmut_trampoline(x_garantir_usuario_existe__mutmut_orig, x_garantir_usuario_existe__mutmut_mutants, args, kwargs)
    return result 

garantir_usuario_existe.__signature__ = _mutmut_signature(x_garantir_usuario_existe__mutmut_orig)
x_garantir_usuario_existe__mutmut_orig.__name__ = 'x_garantir_usuario_existe'


def x_garantir_usuario_sem_multa__mutmut_orig(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def x_garantir_usuario_sem_multa__mutmut_1(sessao: Session, usuario_id: int) -> None:
    sessao = None

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def x_garantir_usuario_sem_multa__mutmut_2(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(None)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def x_garantir_usuario_sem_multa__mutmut_3(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = None
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def x_garantir_usuario_sem_multa__mutmut_4(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(None, usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def x_garantir_usuario_sem_multa__mutmut_5(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, None)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def x_garantir_usuario_sem_multa__mutmut_6(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def x_garantir_usuario_sem_multa__mutmut_7(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, )
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def x_garantir_usuario_sem_multa__mutmut_8(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio(None)


def x_garantir_usuario_sem_multa__mutmut_9(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("XXUsuário possui multa pendente.XX")


def x_garantir_usuario_sem_multa__mutmut_10(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("usuário possui multa pendente.")


def x_garantir_usuario_sem_multa__mutmut_11(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("USUÁRIO POSSUI MULTA PENDENTE.")

x_garantir_usuario_sem_multa__mutmut_mutants : ClassVar[MutantDict] = {
'x_garantir_usuario_sem_multa__mutmut_1': x_garantir_usuario_sem_multa__mutmut_1, 
    'x_garantir_usuario_sem_multa__mutmut_2': x_garantir_usuario_sem_multa__mutmut_2, 
    'x_garantir_usuario_sem_multa__mutmut_3': x_garantir_usuario_sem_multa__mutmut_3, 
    'x_garantir_usuario_sem_multa__mutmut_4': x_garantir_usuario_sem_multa__mutmut_4, 
    'x_garantir_usuario_sem_multa__mutmut_5': x_garantir_usuario_sem_multa__mutmut_5, 
    'x_garantir_usuario_sem_multa__mutmut_6': x_garantir_usuario_sem_multa__mutmut_6, 
    'x_garantir_usuario_sem_multa__mutmut_7': x_garantir_usuario_sem_multa__mutmut_7, 
    'x_garantir_usuario_sem_multa__mutmut_8': x_garantir_usuario_sem_multa__mutmut_8, 
    'x_garantir_usuario_sem_multa__mutmut_9': x_garantir_usuario_sem_multa__mutmut_9, 
    'x_garantir_usuario_sem_multa__mutmut_10': x_garantir_usuario_sem_multa__mutmut_10, 
    'x_garantir_usuario_sem_multa__mutmut_11': x_garantir_usuario_sem_multa__mutmut_11
}

def garantir_usuario_sem_multa(*args, **kwargs):
    result = _mutmut_trampoline(x_garantir_usuario_sem_multa__mutmut_orig, x_garantir_usuario_sem_multa__mutmut_mutants, args, kwargs)
    return result 

garantir_usuario_sem_multa.__signature__ = _mutmut_signature(x_garantir_usuario_sem_multa__mutmut_orig)
x_garantir_usuario_sem_multa__mutmut_orig.__name__ = 'x_garantir_usuario_sem_multa'


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_orig(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_1(sessao: Session, usuario_id: int, limite: int = 4) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_2(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = None

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_3(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(None)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_4(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    usuario = None
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_5(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(None, usuario_id)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_6(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, None)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_7(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(usuario_id)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_8(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, )
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_9(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.qtd_emprestimo > limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_nao_ultrapassou_limite__mutmut_10(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(None)

x_garantir_usuario_nao_ultrapassou_limite__mutmut_mutants : ClassVar[MutantDict] = {
'x_garantir_usuario_nao_ultrapassou_limite__mutmut_1': x_garantir_usuario_nao_ultrapassou_limite__mutmut_1, 
    'x_garantir_usuario_nao_ultrapassou_limite__mutmut_2': x_garantir_usuario_nao_ultrapassou_limite__mutmut_2, 
    'x_garantir_usuario_nao_ultrapassou_limite__mutmut_3': x_garantir_usuario_nao_ultrapassou_limite__mutmut_3, 
    'x_garantir_usuario_nao_ultrapassou_limite__mutmut_4': x_garantir_usuario_nao_ultrapassou_limite__mutmut_4, 
    'x_garantir_usuario_nao_ultrapassou_limite__mutmut_5': x_garantir_usuario_nao_ultrapassou_limite__mutmut_5, 
    'x_garantir_usuario_nao_ultrapassou_limite__mutmut_6': x_garantir_usuario_nao_ultrapassou_limite__mutmut_6, 
    'x_garantir_usuario_nao_ultrapassou_limite__mutmut_7': x_garantir_usuario_nao_ultrapassou_limite__mutmut_7, 
    'x_garantir_usuario_nao_ultrapassou_limite__mutmut_8': x_garantir_usuario_nao_ultrapassou_limite__mutmut_8, 
    'x_garantir_usuario_nao_ultrapassou_limite__mutmut_9': x_garantir_usuario_nao_ultrapassou_limite__mutmut_9, 
    'x_garantir_usuario_nao_ultrapassou_limite__mutmut_10': x_garantir_usuario_nao_ultrapassou_limite__mutmut_10
}

def garantir_usuario_nao_ultrapassou_limite(*args, **kwargs):
    result = _mutmut_trampoline(x_garantir_usuario_nao_ultrapassou_limite__mutmut_orig, x_garantir_usuario_nao_ultrapassou_limite__mutmut_mutants, args, kwargs)
    return result 

garantir_usuario_nao_ultrapassou_limite.__signature__ = _mutmut_signature(x_garantir_usuario_nao_ultrapassou_limite__mutmut_orig)
x_garantir_usuario_nao_ultrapassou_limite__mutmut_orig.__name__ = 'x_garantir_usuario_nao_ultrapassou_limite'


def x_validar_usuario_para_emprestimo__mutmut_orig(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_1(sessao: Session, usuario_id: int, limite: int = 4) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_2(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = None

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_3(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(None)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_4(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(None, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_5(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, None)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_6(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_7(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, )
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_8(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(None, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_9(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, None)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_10(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_11(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, )
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_12(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(None, usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_13(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, None, limite)


def x_validar_usuario_para_emprestimo__mutmut_14(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, None)


def x_validar_usuario_para_emprestimo__mutmut_15(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(usuario_id, limite)


def x_validar_usuario_para_emprestimo__mutmut_16(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, limite)


def x_validar_usuario_para_emprestimo__mutmut_17(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, )

x_validar_usuario_para_emprestimo__mutmut_mutants : ClassVar[MutantDict] = {
'x_validar_usuario_para_emprestimo__mutmut_1': x_validar_usuario_para_emprestimo__mutmut_1, 
    'x_validar_usuario_para_emprestimo__mutmut_2': x_validar_usuario_para_emprestimo__mutmut_2, 
    'x_validar_usuario_para_emprestimo__mutmut_3': x_validar_usuario_para_emprestimo__mutmut_3, 
    'x_validar_usuario_para_emprestimo__mutmut_4': x_validar_usuario_para_emprestimo__mutmut_4, 
    'x_validar_usuario_para_emprestimo__mutmut_5': x_validar_usuario_para_emprestimo__mutmut_5, 
    'x_validar_usuario_para_emprestimo__mutmut_6': x_validar_usuario_para_emprestimo__mutmut_6, 
    'x_validar_usuario_para_emprestimo__mutmut_7': x_validar_usuario_para_emprestimo__mutmut_7, 
    'x_validar_usuario_para_emprestimo__mutmut_8': x_validar_usuario_para_emprestimo__mutmut_8, 
    'x_validar_usuario_para_emprestimo__mutmut_9': x_validar_usuario_para_emprestimo__mutmut_9, 
    'x_validar_usuario_para_emprestimo__mutmut_10': x_validar_usuario_para_emprestimo__mutmut_10, 
    'x_validar_usuario_para_emprestimo__mutmut_11': x_validar_usuario_para_emprestimo__mutmut_11, 
    'x_validar_usuario_para_emprestimo__mutmut_12': x_validar_usuario_para_emprestimo__mutmut_12, 
    'x_validar_usuario_para_emprestimo__mutmut_13': x_validar_usuario_para_emprestimo__mutmut_13, 
    'x_validar_usuario_para_emprestimo__mutmut_14': x_validar_usuario_para_emprestimo__mutmut_14, 
    'x_validar_usuario_para_emprestimo__mutmut_15': x_validar_usuario_para_emprestimo__mutmut_15, 
    'x_validar_usuario_para_emprestimo__mutmut_16': x_validar_usuario_para_emprestimo__mutmut_16, 
    'x_validar_usuario_para_emprestimo__mutmut_17': x_validar_usuario_para_emprestimo__mutmut_17
}

def validar_usuario_para_emprestimo(*args, **kwargs):
    result = _mutmut_trampoline(x_validar_usuario_para_emprestimo__mutmut_orig, x_validar_usuario_para_emprestimo__mutmut_mutants, args, kwargs)
    return result 

validar_usuario_para_emprestimo.__signature__ = _mutmut_signature(x_validar_usuario_para_emprestimo__mutmut_orig)
x_validar_usuario_para_emprestimo__mutmut_orig.__name__ = 'x_validar_usuario_para_emprestimo'


def x_validar_usuario_unico__mutmut_orig(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_1(sessao, email: str):
    sessao = None

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_2(sessao, email: str):
    sessao = _ensure_session(None)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_3(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = ""

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_4(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(None, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_5(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, None):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_6(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr("exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_7(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, ):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_8(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "XXexecXX"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_9(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "EXEC"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_10(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = None

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_11(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            None
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_12(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(None)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_13(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(None).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_14(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email != email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_15(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = None

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_16(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=None).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_17(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(None).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_18(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio(None)

    return True


def x_validar_usuario_unico__mutmut_19(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("XXE-mail já cadastrado.XX")

    return True


def x_validar_usuario_unico__mutmut_20(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("e-mail já cadastrado.")

    return True


def x_validar_usuario_unico__mutmut_21(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-MAIL JÁ CADASTRADO.")

    return True


def x_validar_usuario_unico__mutmut_22(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return False

x_validar_usuario_unico__mutmut_mutants : ClassVar[MutantDict] = {
'x_validar_usuario_unico__mutmut_1': x_validar_usuario_unico__mutmut_1, 
    'x_validar_usuario_unico__mutmut_2': x_validar_usuario_unico__mutmut_2, 
    'x_validar_usuario_unico__mutmut_3': x_validar_usuario_unico__mutmut_3, 
    'x_validar_usuario_unico__mutmut_4': x_validar_usuario_unico__mutmut_4, 
    'x_validar_usuario_unico__mutmut_5': x_validar_usuario_unico__mutmut_5, 
    'x_validar_usuario_unico__mutmut_6': x_validar_usuario_unico__mutmut_6, 
    'x_validar_usuario_unico__mutmut_7': x_validar_usuario_unico__mutmut_7, 
    'x_validar_usuario_unico__mutmut_8': x_validar_usuario_unico__mutmut_8, 
    'x_validar_usuario_unico__mutmut_9': x_validar_usuario_unico__mutmut_9, 
    'x_validar_usuario_unico__mutmut_10': x_validar_usuario_unico__mutmut_10, 
    'x_validar_usuario_unico__mutmut_11': x_validar_usuario_unico__mutmut_11, 
    'x_validar_usuario_unico__mutmut_12': x_validar_usuario_unico__mutmut_12, 
    'x_validar_usuario_unico__mutmut_13': x_validar_usuario_unico__mutmut_13, 
    'x_validar_usuario_unico__mutmut_14': x_validar_usuario_unico__mutmut_14, 
    'x_validar_usuario_unico__mutmut_15': x_validar_usuario_unico__mutmut_15, 
    'x_validar_usuario_unico__mutmut_16': x_validar_usuario_unico__mutmut_16, 
    'x_validar_usuario_unico__mutmut_17': x_validar_usuario_unico__mutmut_17, 
    'x_validar_usuario_unico__mutmut_18': x_validar_usuario_unico__mutmut_18, 
    'x_validar_usuario_unico__mutmut_19': x_validar_usuario_unico__mutmut_19, 
    'x_validar_usuario_unico__mutmut_20': x_validar_usuario_unico__mutmut_20, 
    'x_validar_usuario_unico__mutmut_21': x_validar_usuario_unico__mutmut_21, 
    'x_validar_usuario_unico__mutmut_22': x_validar_usuario_unico__mutmut_22
}

def validar_usuario_unico(*args, **kwargs):
    result = _mutmut_trampoline(x_validar_usuario_unico__mutmut_orig, x_validar_usuario_unico__mutmut_mutants, args, kwargs)
    return result 

validar_usuario_unico.__signature__ = _mutmut_signature(x_validar_usuario_unico__mutmut_orig)
x_validar_usuario_unico__mutmut_orig.__name__ = 'x_validar_usuario_unico'
