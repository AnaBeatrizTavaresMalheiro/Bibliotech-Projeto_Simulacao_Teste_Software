# aplicacao/regras_negocio/regras_livro.py

from sqlmodel import Session
from sqlalchemy import select
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio
from aplicacao.db.models import Livro
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


def x_garantir_livro_existe__mutmut_orig(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    return livro


def x_garantir_livro_existe__mutmut_1(sessao: Session, livro_id: int) -> Livro:
    livro = None
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    return livro


def x_garantir_livro_existe__mutmut_2(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(None, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    return livro


def x_garantir_livro_existe__mutmut_3(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(Livro, None)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    return livro


def x_garantir_livro_existe__mutmut_4(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    return livro


def x_garantir_livro_existe__mutmut_5(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(Livro, )
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    return livro


def x_garantir_livro_existe__mutmut_6(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(Livro, livro_id)
    if livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    return livro


def x_garantir_livro_existe__mutmut_7(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio(None)
    return livro


def x_garantir_livro_existe__mutmut_8(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("XXLivro não encontrado.XX")
    return livro


def x_garantir_livro_existe__mutmut_9(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("livro não encontrado.")
    return livro


def x_garantir_livro_existe__mutmut_10(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("LIVRO NÃO ENCONTRADO.")
    return livro

x_garantir_livro_existe__mutmut_mutants : ClassVar[MutantDict] = {
'x_garantir_livro_existe__mutmut_1': x_garantir_livro_existe__mutmut_1, 
    'x_garantir_livro_existe__mutmut_2': x_garantir_livro_existe__mutmut_2, 
    'x_garantir_livro_existe__mutmut_3': x_garantir_livro_existe__mutmut_3, 
    'x_garantir_livro_existe__mutmut_4': x_garantir_livro_existe__mutmut_4, 
    'x_garantir_livro_existe__mutmut_5': x_garantir_livro_existe__mutmut_5, 
    'x_garantir_livro_existe__mutmut_6': x_garantir_livro_existe__mutmut_6, 
    'x_garantir_livro_existe__mutmut_7': x_garantir_livro_existe__mutmut_7, 
    'x_garantir_livro_existe__mutmut_8': x_garantir_livro_existe__mutmut_8, 
    'x_garantir_livro_existe__mutmut_9': x_garantir_livro_existe__mutmut_9, 
    'x_garantir_livro_existe__mutmut_10': x_garantir_livro_existe__mutmut_10
}

def garantir_livro_existe(*args, **kwargs):
    result = _mutmut_trampoline(x_garantir_livro_existe__mutmut_orig, x_garantir_livro_existe__mutmut_mutants, args, kwargs)
    return result 

garantir_livro_existe.__signature__ = _mutmut_signature(x_garantir_livro_existe__mutmut_orig)
x_garantir_livro_existe__mutmut_orig.__name__ = 'x_garantir_livro_existe'


def x_garantir_livro_disponivel__mutmut_orig(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(sessao, livro_id)
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_1(sessao: Session, livro_id: int) -> None:
    livro = None
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_2(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(None, livro_id)
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_3(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(sessao, None)
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_4(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(livro_id)
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_5(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(sessao, )
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_6(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(sessao, livro_id)
    if livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_7(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(sessao, livro_id)
    if not livro.disponivel:
        raise ErroDeRegraNegocio(None)


def x_garantir_livro_disponivel__mutmut_8(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(sessao, livro_id)
    if not livro.disponivel:
        raise ErroDeRegraNegocio("XXLivro indisponível para empréstimo.XX")


def x_garantir_livro_disponivel__mutmut_9(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(sessao, livro_id)
    if not livro.disponivel:
        raise ErroDeRegraNegocio("livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_10(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(sessao, livro_id)
    if not livro.disponivel:
        raise ErroDeRegraNegocio("LIVRO INDISPONÍVEL PARA EMPRÉSTIMO.")

x_garantir_livro_disponivel__mutmut_mutants : ClassVar[MutantDict] = {
'x_garantir_livro_disponivel__mutmut_1': x_garantir_livro_disponivel__mutmut_1, 
    'x_garantir_livro_disponivel__mutmut_2': x_garantir_livro_disponivel__mutmut_2, 
    'x_garantir_livro_disponivel__mutmut_3': x_garantir_livro_disponivel__mutmut_3, 
    'x_garantir_livro_disponivel__mutmut_4': x_garantir_livro_disponivel__mutmut_4, 
    'x_garantir_livro_disponivel__mutmut_5': x_garantir_livro_disponivel__mutmut_5, 
    'x_garantir_livro_disponivel__mutmut_6': x_garantir_livro_disponivel__mutmut_6, 
    'x_garantir_livro_disponivel__mutmut_7': x_garantir_livro_disponivel__mutmut_7, 
    'x_garantir_livro_disponivel__mutmut_8': x_garantir_livro_disponivel__mutmut_8, 
    'x_garantir_livro_disponivel__mutmut_9': x_garantir_livro_disponivel__mutmut_9, 
    'x_garantir_livro_disponivel__mutmut_10': x_garantir_livro_disponivel__mutmut_10
}

def garantir_livro_disponivel(*args, **kwargs):
    result = _mutmut_trampoline(x_garantir_livro_disponivel__mutmut_orig, x_garantir_livro_disponivel__mutmut_mutants, args, kwargs)
    return result 

garantir_livro_disponivel.__signature__ = _mutmut_signature(x_garantir_livro_disponivel__mutmut_orig)
x_garantir_livro_disponivel__mutmut_orig.__name__ = 'x_garantir_livro_disponivel'

def x_validar_livro_unico__mutmut_orig(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_1(sessao, isbn: str):
    existente = ""

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_2(sessao, isbn: str):
    existente = None

    if hasattr(None, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_3(sessao, isbn: str):
    existente = None

    if hasattr(sessao, None):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_4(sessao, isbn: str):
    existente = None

    if hasattr("exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_5(sessao, isbn: str):
    existente = None

    if hasattr(sessao, ):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_6(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "XXexecXX"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_7(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "EXEC"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_8(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = None

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_9(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            None
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_10(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(None)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_11(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(None).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_12(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn != isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_13(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = None

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_14(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(None).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_15(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(None).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_16(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn != isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_17(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio(None)

    return True

def x_validar_livro_unico__mutmut_18(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("XXISBN já cadastrado.XX")

    return True

def x_validar_livro_unico__mutmut_19(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("isbn já cadastrado.")

    return True

def x_validar_livro_unico__mutmut_20(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN JÁ CADASTRADO.")

    return True

def x_validar_livro_unico__mutmut_21(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return False

x_validar_livro_unico__mutmut_mutants : ClassVar[MutantDict] = {
'x_validar_livro_unico__mutmut_1': x_validar_livro_unico__mutmut_1, 
    'x_validar_livro_unico__mutmut_2': x_validar_livro_unico__mutmut_2, 
    'x_validar_livro_unico__mutmut_3': x_validar_livro_unico__mutmut_3, 
    'x_validar_livro_unico__mutmut_4': x_validar_livro_unico__mutmut_4, 
    'x_validar_livro_unico__mutmut_5': x_validar_livro_unico__mutmut_5, 
    'x_validar_livro_unico__mutmut_6': x_validar_livro_unico__mutmut_6, 
    'x_validar_livro_unico__mutmut_7': x_validar_livro_unico__mutmut_7, 
    'x_validar_livro_unico__mutmut_8': x_validar_livro_unico__mutmut_8, 
    'x_validar_livro_unico__mutmut_9': x_validar_livro_unico__mutmut_9, 
    'x_validar_livro_unico__mutmut_10': x_validar_livro_unico__mutmut_10, 
    'x_validar_livro_unico__mutmut_11': x_validar_livro_unico__mutmut_11, 
    'x_validar_livro_unico__mutmut_12': x_validar_livro_unico__mutmut_12, 
    'x_validar_livro_unico__mutmut_13': x_validar_livro_unico__mutmut_13, 
    'x_validar_livro_unico__mutmut_14': x_validar_livro_unico__mutmut_14, 
    'x_validar_livro_unico__mutmut_15': x_validar_livro_unico__mutmut_15, 
    'x_validar_livro_unico__mutmut_16': x_validar_livro_unico__mutmut_16, 
    'x_validar_livro_unico__mutmut_17': x_validar_livro_unico__mutmut_17, 
    'x_validar_livro_unico__mutmut_18': x_validar_livro_unico__mutmut_18, 
    'x_validar_livro_unico__mutmut_19': x_validar_livro_unico__mutmut_19, 
    'x_validar_livro_unico__mutmut_20': x_validar_livro_unico__mutmut_20, 
    'x_validar_livro_unico__mutmut_21': x_validar_livro_unico__mutmut_21
}

def validar_livro_unico(*args, **kwargs):
    result = _mutmut_trampoline(x_validar_livro_unico__mutmut_orig, x_validar_livro_unico__mutmut_mutants, args, kwargs)
    return result 

validar_livro_unico.__signature__ = _mutmut_signature(x_validar_livro_unico__mutmut_orig)
x_validar_livro_unico__mutmut_orig.__name__ = 'x_validar_livro_unico'