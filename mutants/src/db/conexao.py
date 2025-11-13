# db/conexao.py
from pathlib import Path
from sqlmodel import create_engine, Session

# >>> MESMO cálculo de caminho do criar_schemas.py <<<
# ROOT_DIR = Path(__file__).resolve().parents[1]
# DB_PATH = ROOT_DIR / "biblioteca.db"   # único ponto de verdade

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "data" / "biblioteca.db"

print("📁 Usando banco em:", DB_PATH)


DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

# Para SQLite + FastAPI, desabilite check_same_thread
motor = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})
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

def x_obter_sessao__mutmut_orig():
    with Session(motor) as sess:
        yield sess

def x_obter_sessao__mutmut_1():
    with Session(None) as sess:
        yield sess

x_obter_sessao__mutmut_mutants : ClassVar[MutantDict] = {
'x_obter_sessao__mutmut_1': x_obter_sessao__mutmut_1
}

def obter_sessao(*args, **kwargs):
    result = _mutmut_trampoline(x_obter_sessao__mutmut_orig, x_obter_sessao__mutmut_mutants, args, kwargs)
    return result 

obter_sessao.__signature__ = _mutmut_signature(x_obter_sessao__mutmut_orig)
x_obter_sessao__mutmut_orig.__name__ = 'x_obter_sessao'

from sqlmodel import create_engine

def x_criar_engine__mutmut_orig(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" in url else {}
    return create_engine(url, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_1(url: str, echo: bool = True):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" in url else {}
    return create_engine(url, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_2(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = None
    return create_engine(url, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_3(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"XXcheck_same_threadXX": False} if "sqlite" in url else {}
    return create_engine(url, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_4(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"CHECK_SAME_THREAD": False} if "sqlite" in url else {}
    return create_engine(url, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_5(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": True} if "sqlite" in url else {}
    return create_engine(url, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_6(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "XXsqliteXX" in url else {}
    return create_engine(url, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_7(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "SQLITE" in url else {}
    return create_engine(url, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_8(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" not in url else {}
    return create_engine(url, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_9(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" in url else {}
    return create_engine(None, echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_10(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" in url else {}
    return create_engine(url, echo=None, connect_args=connect_args)

def x_criar_engine__mutmut_11(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" in url else {}
    return create_engine(url, echo=echo, connect_args=None)

def x_criar_engine__mutmut_12(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" in url else {}
    return create_engine(echo=echo, connect_args=connect_args)

def x_criar_engine__mutmut_13(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" in url else {}
    return create_engine(url, connect_args=connect_args)

def x_criar_engine__mutmut_14(url: str, echo: bool = False):
    """
    Cria e retorna uma engine SQLModel/SQLAlchemy.
    Para SQLite, desabilita check_same_thread automaticamente.
    """
    connect_args = {"check_same_thread": False} if "sqlite" in url else {}
    return create_engine(url, echo=echo, )

x_criar_engine__mutmut_mutants : ClassVar[MutantDict] = {
'x_criar_engine__mutmut_1': x_criar_engine__mutmut_1, 
    'x_criar_engine__mutmut_2': x_criar_engine__mutmut_2, 
    'x_criar_engine__mutmut_3': x_criar_engine__mutmut_3, 
    'x_criar_engine__mutmut_4': x_criar_engine__mutmut_4, 
    'x_criar_engine__mutmut_5': x_criar_engine__mutmut_5, 
    'x_criar_engine__mutmut_6': x_criar_engine__mutmut_6, 
    'x_criar_engine__mutmut_7': x_criar_engine__mutmut_7, 
    'x_criar_engine__mutmut_8': x_criar_engine__mutmut_8, 
    'x_criar_engine__mutmut_9': x_criar_engine__mutmut_9, 
    'x_criar_engine__mutmut_10': x_criar_engine__mutmut_10, 
    'x_criar_engine__mutmut_11': x_criar_engine__mutmut_11, 
    'x_criar_engine__mutmut_12': x_criar_engine__mutmut_12, 
    'x_criar_engine__mutmut_13': x_criar_engine__mutmut_13, 
    'x_criar_engine__mutmut_14': x_criar_engine__mutmut_14
}

def criar_engine(*args, **kwargs):
    result = _mutmut_trampoline(x_criar_engine__mutmut_orig, x_criar_engine__mutmut_mutants, args, kwargs)
    return result 

criar_engine.__signature__ = _mutmut_signature(x_criar_engine__mutmut_orig)
x_criar_engine__mutmut_orig.__name__ = 'x_criar_engine'
