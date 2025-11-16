from sqlmodel import Session
from aplicacao.db.database import engine
from contextlib import contextmanager
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


# ----------------------------------------------------------
# Cria uma sessão pura (imutável para o Mutmut)
# ----------------------------------------------------------
def x__create_session__mutmut_orig():
    return Session(engine)


# ----------------------------------------------------------
# Cria uma sessão pura (imutável para o Mutmut)
# ----------------------------------------------------------
def x__create_session__mutmut_1():
    return Session(None)

x__create_session__mutmut_mutants : ClassVar[MutantDict] = {
'x__create_session__mutmut_1': x__create_session__mutmut_1
}

def _create_session(*args, **kwargs):
    result = _mutmut_trampoline(x__create_session__mutmut_orig, x__create_session__mutmut_mutants, args, kwargs)
    return result 

_create_session.__signature__ = _mutmut_signature(x__create_session__mutmut_orig)
x__create_session__mutmut_orig.__name__ = 'x__create_session'


# ----------------------------------------------------------
# Context manager seguro contra mutações
# ----------------------------------------------------------
@contextmanager
def _session_context():
    session = _create_session()
    try:
        yield session
    finally:
        session.close()


# ----------------------------------------------------------
# Função usada pelo FastAPI como dependência
# Blindada contra mutação do Mutmut
# ----------------------------------------------------------
def x_get_session__mutmut_orig():
    # Obtém a sessão de forma segura
    with _session_context() as session:

        # CASO o Mutmut transforme a sessão em um generator,
        # nós "desenrolamos" ele com next().
        if isinstance(session, types.GeneratorType):
            session = next(session)

        # FastAPI espera um generator, então yield aqui é seguro.
        yield session


# ----------------------------------------------------------
# Função usada pelo FastAPI como dependência
# Blindada contra mutação do Mutmut
# ----------------------------------------------------------
def x_get_session__mutmut_1():
    # Obtém a sessão de forma segura
    with _session_context() as session:

        # CASO o Mutmut transforme a sessão em um generator,
        # nós "desenrolamos" ele com next().
        if isinstance(session, types.GeneratorType):
            session = None

        # FastAPI espera um generator, então yield aqui é seguro.
        yield session


# ----------------------------------------------------------
# Função usada pelo FastAPI como dependência
# Blindada contra mutação do Mutmut
# ----------------------------------------------------------
def x_get_session__mutmut_2():
    # Obtém a sessão de forma segura
    with _session_context() as session:

        # CASO o Mutmut transforme a sessão em um generator,
        # nós "desenrolamos" ele com next().
        if isinstance(session, types.GeneratorType):
            session = next(None)

        # FastAPI espera um generator, então yield aqui é seguro.
        yield session

x_get_session__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_session__mutmut_1': x_get_session__mutmut_1, 
    'x_get_session__mutmut_2': x_get_session__mutmut_2
}

def get_session(*args, **kwargs):
    result = _mutmut_trampoline(x_get_session__mutmut_orig, x_get_session__mutmut_mutants, args, kwargs)
    return result 

get_session.__signature__ = _mutmut_signature(x_get_session__mutmut_orig)
x_get_session__mutmut_orig.__name__ = 'x_get_session'
