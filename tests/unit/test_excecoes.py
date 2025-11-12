import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from src.configuracoes.excecoes import ErroDeRegraNegocio, ErroNaoEncontrado

# =========================================================
# Testes básicos de string
# =========================================================
def test_erro_de_regra_negocio_str():
    e = ErroDeRegraNegocio("Usuário com multa")
    assert "Usuário com multa" in str(e)

def test_erro_nao_encontrado_str():
    e = ErroNaoEncontrado("Livro não existe")
    assert "Livro não existe" in str(e)

# =========================================================
# Testes de instância e herança
# =========================================================
def test_erro_de_regra_negocio_instance():
    e = ErroDeRegraNegocio("Teste")
    assert isinstance(e, Exception)
    assert isinstance(e, ErroDeRegraNegocio)

def test_erro_nao_encontrado_instance():
    e = ErroNaoEncontrado("Teste")
    assert isinstance(e, Exception)
    assert isinstance(e, ErroNaoEncontrado)

# =========================================================
# Testes com mensagens diferentes
# =========================================================
@pytest.mark.parametrize("msg", ["Mensagem 1", "Erro crítico", ""])
def test_erro_de_regra_negocio_param(msg):
    e = ErroDeRegraNegocio(msg)
    assert str(e) == msg

@pytest.mark.parametrize("msg", ["Não encontrado", "Usuário inválido", ""])
def test_erro_nao_encontrado_param(msg):
    e = ErroNaoEncontrado(msg)
    assert str(e) == msg

# =========================================================
# Testes de uso com pytest.raises
# =========================================================
def test_raises_erro_de_regra_negocio():
    with pytest.raises(ErroDeRegraNegocio, match="multa"):
        raise ErroDeRegraNegocio("Usuário com multa")

def test_raises_erro_nao_encontrado():
    with pytest.raises(ErroNaoEncontrado, match="não existe"):
        raise ErroNaoEncontrado("Livro não existe")
