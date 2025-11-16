import pytest
from sqlmodel import SQLModel, Session, create_engine
from aplicacao.db.models import Livro
from aplicacao.regras_negocio.regras_livro import (
    garantir_livro_existe,
    garantir_livro_disponivel,
    validar_livro_unico,
)
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio


# =================================================================
# FIXTURE
# =================================================================
@pytest.fixture
def sessao_memoria():
    engine = create_engine("sqlite:///:memory:", echo=False)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture
def livro(sessao_memoria):
    l = Livro(titulo="A", isbn="123", disponivel=True)
    sessao_memoria.add(l)
    sessao_memoria.commit()
    sessao_memoria.refresh(l)
    return l


# =================================================================
# garantir_livro_existe
# =================================================================

def test_garantir_livro_existe_sucesso(sessao_memoria, livro):
    encontrado = garantir_livro_existe(sessao_memoria, livro.id)
    assert encontrado.id == livro.id


def test_garantir_livro_existe_inexistente(sessao_memoria):
    with pytest.raises(ErroDeRegraNegocio):
        garantir_livro_existe(sessao_memoria, livro_id=999)


# =================================================================
# garantir_livro_disponivel
# =================================================================

def test_garantir_livro_disponivel_sucesso(sessao_memoria, livro):
    # livro.fixture já vem como disponivel=True
    garantir_livro_disponivel(sessao_memoria, livro.id)
    assert True  # passou sem exceção


def test_garantir_livro_disponivel_indisponivel(sessao_memoria, livro):
    livro.disponivel = False
    sessao_memoria.commit()

    with pytest.raises(ErroDeRegraNegocio):
        garantir_livro_disponivel(sessao_memoria, livro.id)


# =================================================================
# validar_livro_unico
# =================================================================

def test_validar_livro_unico_sucesso(sessao_memoria):
    # ISBN não cadastrado
    assert validar_livro_unico(sessao_memoria, "999") is True


def test_validar_livro_unico_isbn_existente(sessao_memoria, livro):
    with pytest.raises(ErroDeRegraNegocio):
        validar_livro_unico(sessao_memoria, livro.isbn)


# =================================================================
# validar_livro_unico - fallback .query() (modo SQLAlchemy)
# =================================================================

class SessionFakeQuery:
    """
    Sessão fake com .query() para testar o caminho alternativo
    """

    def __init__(self, existente: bool):
        self.existe = existente

    class QueryFake:
        def __init__(self, existente):
            self.existe = existente

        def filter(self, *args, **kwargs):
            return self

        def first(self):
            if self.existe:
                return object()
            return None

    def query(self, *args, **kwargs):
        return SessionFakeQuery.QueryFake(self.existe)


def test_validar_livro_unico_query_fallback_sucesso():
    sessao_fake = SessionFakeQuery(False)
    assert validar_livro_unico(sessao_fake, "qualquer") is True


def test_validar_livro_unico_query_fallback_existente():
    sessao_fake = SessionFakeQuery(True)
    with pytest.raises(ErroDeRegraNegocio):
        validar_livro_unico(sessao_fake, "qualquer")
