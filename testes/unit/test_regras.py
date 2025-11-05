import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from configuracoes.excecoes import ErroDeRegraNegocio
from server import regras

class SessaoFake:
    def __init__(self, usuario):
        self._usuario = usuario

    def get(self, modelo, id):
        # Ignora o modelo e id — só retorna o usuário fake
        return self._usuario

@pytest.mark.parametrize("qtd_emprestimo", [0, 2, 3])
def test_limite_de_emprestimos(qtd_emprestimo):
    usuario = type("UsuarioFake", (), {
        "id": 1,
        "qtd_emprestimo": qtd_emprestimo,
        "possui_multa_aberta": False
    })()

    sessao = SessaoFake(usuario)

    if qtd_emprestimo >= 3:
        with pytest.raises(ErroDeRegraNegocio):
            regras.garantir_usuario_pode_emprestar(sessao, usuario_id=usuario.id)
    else:
        # não deve lançar exceção
        try:
            regras.garantir_usuario_pode_emprestar(sessao, usuario_id=usuario.id)
        except ErroDeRegraNegocio as e:
            pytest.fail(f"ErroDeRegraNegocio não era esperado aqui: {e}")

def test_usuario_inexistente():
    class SessaoFakeVazia:
        def get(self, modelo, id):
            return None

    sessao = SessaoFakeVazia()
    with pytest.raises(ErroDeRegraNegocio, match="Usuário não encontrado"):
        regras.garantir_usuario_pode_emprestar(sessao, usuario_id=999)

