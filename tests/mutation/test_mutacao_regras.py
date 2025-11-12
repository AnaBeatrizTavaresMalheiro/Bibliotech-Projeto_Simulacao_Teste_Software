import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.server import regras
from src.configuracoes.excecoes import ErroDeRegraNegocio

def test_validar_usuario_com_multa():
    usuario = {"possui_multa_aberta": True}
    try:
        regras.validar_usuario(usuario)
    except ErroDeRegraNegocio:
        pass

def test_calculo_multa():
    multa = regras.calcular_multa(3, 2.0)
    assert multa == 6.0
