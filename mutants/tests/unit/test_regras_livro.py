import pytest
from unittest.mock import MagicMock
from aplicacao.regras_negocio.regras_livro import (
    garantir_livro_existe,
    garantir_livro_disponivel,validar_livro_unico
)
from aplicacao.db.models import Livro
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio


@pytest.fixture
def sessao_fake():
    sessao = MagicMock()
    sessao.get = MagicMock()
    return sessao


@pytest.fixture
def livro_ok():
    return Livro(id=1, titulo="RDR2", isbn="123", disponivel=True)


@pytest.fixture
def livro_indisponivel():
    return Livro(id=2, titulo="TLOU", isbn="456", disponivel=False)


def test_livro_existe(sessao_fake, livro_ok):
    sessao_fake.get.return_value = livro_ok
    assert garantir_livro_existe(sessao_fake, livro_ok.id) is livro_ok


def test_livro_inexistente(sessao_fake):
    sessao_fake.get.return_value = None
    with pytest.raises(ErroDeRegraNegocio):
        garantir_livro_existe(sessao_fake, 999)

def test_livro_duplicado(sessao_fake):
    """
    Cenário de Erro:
    ISBN já existente → deve levantar ErroDeRegraNegocio.
    """

    livro_existente = Livro(id=1, titulo="RDR2", isbn="1234", disponivel=True)

    # o método .exec() deve retornar o livro existente
    sessao_fake.exec.return_value.first.return_value = livro_existente

    with pytest.raises(ErroDeRegraNegocio):
        validar_livro_unico(sessao_fake, "1234")

def test_livro_disponivel(sessao_fake, livro_ok):
    sessao_fake.get.return_value = livro_ok
    garantir_livro_disponivel(sessao_fake, livro_ok.id)


def test_livro_indisponivel(sessao_fake, livro_indisponivel):
    sessao_fake.get.return_value = livro_indisponivel
    with pytest.raises(ErroDeRegraNegocio):
        garantir_livro_disponivel(sessao_fake, livro_indisponivel.id)


def test_livro_disponibilidade_corrompida(sessao_fake, livro_ok):
    livro_ok.disponivel = None
    sessao_fake.get.return_value = livro_ok
    with pytest.raises(ErroDeRegraNegocio):
        garantir_livro_disponivel(sessao_fake, livro_ok.id)


def test_livro_campo_indisponivel_string(sessao_fake, livro_ok):
    livro_ok.disponivel = "não sei"
    sessao_fake.get.return_value = livro_ok

    with pytest.raises(ErroDeRegraNegocio):
        validar_livro(sessao_fake, livro_ok.id)

def test_livro_existe_mas_com_campo_faltando(sessao_fake):
    livro = Livro(id=3, titulo="Teste", isbn="ZZZ")
    livro.disponivel = None
    sessao_fake.get.return_value = livro
    with pytest.raises(ErroDeRegraNegocio):
        garantir_livro_disponivel(sessao_fake, 3)


def test_livro_isbn_invalido(sessao_fake, livro_ok):
    livro_ok.isbn = ""
    sessao_fake.get.return_value = livro_ok
    garantir_livro_existe(sessao_fake, livro_ok.id)

def validar_livro(sessao, livro_id: int):
    livro = sessao.get(Livro, livro_id)
    if livro is None:
        raise ErroDeRegraNegocio("Livro não encontrado.")

    if not isinstance(livro.disponivel, bool):
        raise ErroDeRegraNegocio("Campo 'disponivel' deve ser booleano.")

    return livro