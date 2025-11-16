# testes/unit/conftest.py
import pytest
from unittest.mock import MagicMock
from datetime import date, timedelta
from aplicacao.db.models import Usuario, Livro, Emprestimo

# ------------------------------
# Sessão fake
# ------------------------------
@pytest.fixture
def sessao_fake():
    return MagicMock()


# ------------------------------
# Usuários
# ------------------------------
@pytest.fixture
def usuario_sem_multa():
    return Usuario(
        id=1,
        nome="Bruno",
        email="bruno@teste.com",
        qtd_emprestimo=0,
        possui_multa_aberta=False
    )

@pytest.fixture
def usuario_com_multa():
    return Usuario(
        id=2,
        nome="João",
        email="joao@teste.com",
        qtd_emprestimo=0,
        possui_multa_aberta=True
    )

@pytest.fixture
def usuario_com_3():
    return Usuario(
        id=3,
        nome="Ana",
        email="ana@teste.com",
        qtd_emprestimo=3,
        possui_multa_aberta=False
    )


# ------------------------------
# Livros
# ------------------------------
@pytest.fixture
def livro_disponivel():
    return Livro(
        id=10,
        titulo="Livro X",
        isbn="1111",
        disponivel=True
    )

@pytest.fixture
def livro_indisponivel():
    return Livro(
        id=11,
        titulo="Livro Y",
        isbn="2222",
        disponivel=False
    )


# ------------------------------
# Empréstimos
# ------------------------------
@pytest.fixture
def emprestimo_ativo():
    return Emprestimo(
        id=100,
        usuario_id=1,
        livro_id=10,
        data_emprestimo=date.today(),
        data_devolucao_prevista=date.today() + timedelta(days=7),
        data_devolucao_real=None
    )


@pytest.fixture
def emprestimo_atrasado():
    prevista = date.today() - timedelta(days=5)
    return Emprestimo(
        id=101,
        usuario_id=1,
        livro_id=10,
        data_emprestimo=prevista - timedelta(days=7),
        data_devolucao_prevista=prevista,
        data_devolucao_real=None
    )
