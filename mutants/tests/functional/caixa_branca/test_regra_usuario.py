import pytest
from sqlmodel import SQLModel, Session, create_engine

from aplicacao.db.models import Usuario
from aplicacao.regras_negocio.regras_usuario import (
    garantir_usuario_existe,
    garantir_usuario_sem_multa,
    garantir_usuario_nao_ultrapassou_limite,
    validar_usuario_para_emprestimo,
    validar_usuario_unico,
)
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture
def sessao_memoria():
    engine = create_engine("sqlite:///:memory:", echo=False)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as s:
        yield s


@pytest.fixture
def usuario(sessao_memoria):
    u = Usuario(
        nome="Bruno",
        email="bruno@x.com",
        possui_multa_aberta=False,
        qtd_emprestimo=0
    )
    sessao_memoria.add(u)
    sessao_memoria.commit()
    sessao_memoria.refresh(u)
    return u


# =============================================================================
# garantir_usuario_existe
# =============================================================================

def test_garantir_usuario_existe_sucesso(sessao_memoria, usuario):
    achado = garantir_usuario_existe(sessao_memoria, usuario.id)
    assert achado.id == usuario.id


def test_garantir_usuario_existe_inexistente(sessao_memoria):
    with pytest.raises(ErroDeRegraNegocio):
        garantir_usuario_existe(sessao_memoria, 999)


# =============================================================================
# garantir_usuario_sem_multa
# =============================================================================

def test_garantir_usuario_sem_multa_sucesso(sessao_memoria, usuario):
    garantir_usuario_sem_multa(sessao_memoria, usuario.id)
    assert True


def test_garantir_usuario_sem_multa_com_multa(sessao_memoria, usuario):
    usuario.possui_multa_aberta = True
    sessao_memoria.commit()

    with pytest.raises(ErroDeRegraNegocio):
        garantir_usuario_sem_multa(sessao_memoria, usuario.id)


# =============================================================================
# garantir_usuario_nao_ultrapassou_limite
# =============================================================================

def test_garantir_usuario_nao_ultrapassou_limite_sucesso(sessao_memoria, usuario):
    usuario.qtd_emprestimo = 2
    sessao_memoria.commit()

    garantir_usuario_nao_ultrapassou_limite(sessao_memoria, usuario.id, limite=3)
    assert True


def test_garantir_usuario_nao_ultrapassou_limite_estourado(sessao_memoria, usuario):
    usuario.qtd_emprestimo = 3
    sessao_memoria.commit()

    with pytest.raises(ErroDeRegraNegocio):
        garantir_usuario_nao_ultrapassou_limite(sessao_memoria, usuario.id, limite=3)


# =============================================================================
# validar_usuario_para_emprestimo (função agregadora)
# =============================================================================

def test_validar_usuario_para_emprestimo_sucesso(sessao_memoria, usuario):
    validar_usuario_para_emprestimo(sessao_memoria, usuario.id)
    assert True


def test_validar_usuario_para_emprestimo_usuario_inexistente(sessao_memoria):
    with pytest.raises(ErroDeRegraNegocio):
        validar_usuario_para_emprestimo(sessao_memoria, 999)


def test_validar_usuario_para_emprestimo_com_multa(sessao_memoria, usuario):
    usuario.possui_multa_aberta = True
    sessao_memoria.commit()

    with pytest.raises(ErroDeRegraNegocio):
        validar_usuario_para_emprestimo(sessao_memoria, usuario.id)


def test_validar_usuario_para_emprestimo_limite_estourado(sessao_memoria, usuario):
    usuario.qtd_emprestimo = 3
    sessao_memoria.commit()

    with pytest.raises(ErroDeRegraNegocio):
        validar_usuario_para_emprestimo(sessao_memoria, usuario.id)


# =============================================================================
# validar_usuario_unico - via sessao.exec() (SQLModel)
# =============================================================================

def test_validar_usuario_unico_sucesso(sessao_memoria):
    assert validar_usuario_unico(sessao_memoria, "novo@x.com") is True


def test_validar_usuario_unico_existente(sessao_memoria, usuario):
    with pytest.raises(ErroDeRegraNegocio):
        validar_usuario_unico(sessao_memoria, usuario.email)


# =============================================================================
# validar_usuario_unico - fallback .query() (modo SQLAlchemy)
# =============================================================================

class SessionFakeQuery:
    """
    Fake para testar caminho .query() → cobrimos todas as linhas 34–49
    """

    def __init__(self, existente):
        self.existe = existente

    class QueryFake:
        def __init__(self, existe):
            self.existe = existe

        def filter_by(self, **kwargs):
            return self

        def first(self):
            if self.existe:
                return object()
            return None

    def query(self, *args, **kwargs):
        return SessionFakeQuery.QueryFake(self.existe)


def test_validar_usuario_unico_query_fallback_sucesso():
    sessao_fake = SessionFakeQuery(False)
    assert validar_usuario_unico(sessao_fake, "alguem@x.com") is True


def test_validar_usuario_unico_query_fallback_existente():
    sessao_fake = SessionFakeQuery(True)
    with pytest.raises(ErroDeRegraNegocio):
        validar_usuario_unico(sessao_fake, "qualquer@x.com")
