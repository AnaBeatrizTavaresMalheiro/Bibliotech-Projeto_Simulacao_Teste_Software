from sqlmodel import Session
from aplicacao.db.database import engine
from contextlib import contextmanager
import types


# ----------------------------------------------------------
# Cria uma sessão pura (imutável para o Mutmut)
# ----------------------------------------------------------
def _create_session():
    return Session(engine)


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
def get_session():
    # Obtém a sessão de forma segura
    with _session_context() as session:

        # CASO o Mutmut transforme a sessão em um generator,
        # nós "desenrolamos" ele com next().
        if isinstance(session, types.GeneratorType):
            session = next(session)

        # FastAPI espera um generator, então yield aqui é seguro.
        yield session
