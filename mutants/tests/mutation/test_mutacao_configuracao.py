import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.configuracoes.excecoes import ErroDeRegraNegocio

def test_erro_de_regra_negocio_str():
    erro = ErroDeRegraNegocio("Usuário inválido")
    assert str(erro) == "Usuário inválido"
