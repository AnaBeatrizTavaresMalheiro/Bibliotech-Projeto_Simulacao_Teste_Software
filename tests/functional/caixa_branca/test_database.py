import pytest
from aplicacao.db.database import (
    resetar_banco,
    criar_tabelas,
    carregar_seed,
)
from sqlalchemy import inspect
from aplicacao.db.sessao import engine


@pytest.fixture(autouse=True)
def rollback():
    resetar_banco()


@pytest.fixture
def sessao_fake(mocker):
    return mocker.MagicMock()


def test_criar_tabelas():
    criar_tabelas()
    insp = inspect(engine)
    assert "usuario" in insp.get_table_names()


def test_carregar_seed_sem_erro():
    carregar_seed()
