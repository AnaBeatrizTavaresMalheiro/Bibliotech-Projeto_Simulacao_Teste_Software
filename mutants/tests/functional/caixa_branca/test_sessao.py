import pytest
from aplicacao.db.database import resetar_banco
from aplicacao.db.sessao import get_session
from sqlmodel import Session


@pytest.fixture(autouse=True)
def rollback():
    resetar_banco()


@pytest.fixture
def sessao_fake(mocker):
    return mocker.MagicMock()



def test_get_session():
    gen = get_session()
    s = next(gen)      # pega a sessão do generator
    assert isinstance(s, Session)
    s.close()
