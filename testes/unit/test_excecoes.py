import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from configuracoes.excecoes import ErroDeRegraNegocio, ErroNaoEncontrado

def test_erro_de_regra_negocio_str():
    e = ErroDeRegraNegocio("Usuário com multa")
    assert "Usuário com multa" in str(e)

def test_erro_nao_encontrado_str():
    e = ErroNaoEncontrado("Livro não existe")
    assert "Livro não existe" in str(e)
