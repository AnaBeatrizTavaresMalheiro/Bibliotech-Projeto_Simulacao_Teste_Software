import pytest
from datetime import date
from aplicacao.db.database import resetar_banco, parse_date


@pytest.fixture(autouse=True)
def rollback():
    resetar_banco()


@pytest.fixture
def sessao_fake(mocker):
    return mocker.MagicMock()


def test_parse_none():
    assert parse_date(None) is None


def test_parse_date_object():
    d = date.today()
    assert parse_date(d) == d


def test_parse_date_string():
    assert parse_date("2024-01-01").year == 2024
