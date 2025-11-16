import pytest
from unittest.mock import MagicMock
from aplicacao.regras_negocio.regras_usuario import (
    garantir_usuario_existe,
    garantir_usuario_sem_multa,
    garantir_usuario_nao_ultrapassou_limite,
    validar_usuario_para_emprestimo,
    validar_usuario_unico
)
from aplicacao.db.models import Usuario
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio


# ---------------- FIXTURES ----------------
@pytest.fixture
def sessao_fake():
    sessao = MagicMock()
    sessao.get = MagicMock()
    return sessao


@pytest.fixture
def usuario_ok():
    return Usuario(id=1, nome="Bruno", email="b@b.com",
                   qtd_emprestimo=0, possui_multa_aberta=False)


@pytest.fixture
def usuario_com_multa():
    return Usuario(id=2, nome="Ana", email="a@a.com",
                   qtd_emprestimo=1, possui_multa_aberta=True)


@pytest.fixture
def usuario_com_3_emprestimos():
    return Usuario(id=3, nome="João", email="j@j.com",
                   qtd_emprestimo=3, possui_multa_aberta=False)


# ---------------- TESTES: garantir_usuario_existe ----------------
def test_usuario_existe(sessao_fake, usuario_ok):
    sessao_fake.get.return_value = usuario_ok
    result = garantir_usuario_existe(sessao_fake, usuario_ok.id)
    assert result is usuario_ok


def test_usuario_inexistente(sessao_fake):
    sessao_fake.get.return_value = None
    with pytest.raises(ErroDeRegraNegocio):
        garantir_usuario_existe(sessao_fake, 999)

def test_usuario_duplicado(sessao_fake):
    

    usuario_existente = Usuario(
        id=1,
        nome="Bruno",
        email="bruno@teste.com",
        qtd_emprestimo=0,
        possui_multa_aberta=False
    )

    # Simula que o SELECT retorna um usuário já cadastrado
    sessao_fake.exec.return_value.first.return_value = usuario_existente

    with pytest.raises(ErroDeRegraNegocio):
        validar_usuario_unico(sessao_fake, "bruno@teste.com")


# ---------------- TESTES: garantir_usuario_sem_multa ----------------
def test_usuario_sem_multa(sessao_fake, usuario_ok):
    sessao_fake.get.return_value = usuario_ok
    garantir_usuario_sem_multa(sessao_fake, usuario_ok.id)


def test_usuario_com_multa(sessao_fake, usuario_com_multa):
    sessao_fake.get.return_value = usuario_com_multa
    with pytest.raises(ErroDeRegraNegocio):
        garantir_usuario_sem_multa(sessao_fake, usuario_com_multa.id)


# ---------------- TESTES: garantir_usuario_pode_emprestar ----------------
def test_usuario_pode_emprestar(sessao_fake, usuario_ok):
    sessao_fake.get.return_value = usuario_ok
    garantir_usuario_nao_ultrapassou_limite(sessao_fake, usuario_ok.id)


def test_usuario_nao_pode_emprestar_3_livros(sessao_fake, usuario_com_3_emprestimos):
    sessao_fake.get.return_value = usuario_com_3_emprestimos
    with pytest.raises(ErroDeRegraNegocio):
        validar_usuario_para_emprestimo(sessao_fake, usuario_com_3_emprestimos.id)


def test_usuario_multa_bloqueia(sessao_fake, usuario_com_multa):
    sessao_fake.get.return_value = usuario_com_multa
    with pytest.raises(ErroDeRegraNegocio):
        validar_usuario_para_emprestimo(sessao_fake, usuario_com_multa.id)


def test_usuario_inexistente_emprestar(sessao_fake):
    sessao_fake.get.return_value = None
    with pytest.raises(ErroDeRegraNegocio):
        validar_usuario_para_emprestimo(sessao_fake, 123)


def test_usuario_emprestimo_negativo(sessao_fake, usuario_ok):
    usuario_ok.qtd_emprestimo = -1
    sessao_fake.get.return_value = usuario_ok
    validar_usuario_para_emprestimo(sessao_fake, usuario_ok.id)


def test_usuario_emprestimo_limite(sessao_fake, usuario_ok):
    usuario_ok.qtd_emprestimo = 2
    sessao_fake.get.return_value = usuario_ok
    validar_usuario_para_emprestimo(sessao_fake, usuario_ok.id)
