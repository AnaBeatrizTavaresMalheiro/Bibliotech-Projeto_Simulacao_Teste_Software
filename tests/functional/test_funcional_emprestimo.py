from datetime import date
from sqlmodel import Session, select
from src.db.conexao import motor
from src.server import regras
from src.configuracoes.excecoes import ErroDeRegraNegocio
from src.db.modelos import Usuario, Livro, Emprestimo

def test_criar_emprestimo_usuario_e_livro_validos():
    with Session(motor) as sessao:
        # Usuário João (id=1), Livro "O Alienista" (id=4)
        emprestimo = regras.criar_emprestimo(sessao, usuario_id=1, livro_id=4)
        assert emprestimo.usuario_id == 1
        assert emprestimo.livro_id == 4

def test_emprestimo_usuario_inexistente():
    with Session(motor) as sessao:
        try:
            regras.criar_emprestimo(sessao, usuario_id=999, livro_id=1)
            assert False, "Deveria falhar com ErroDeRegraNegocio"
        except ErroDeRegraNegocio:
            assert True

def test_emprestimo_livro_inexistente():
    with Session(motor) as sessao:
        try:
            regras.criar_emprestimo(sessao, usuario_id=1, livro_id=999)
            assert False
        except ErroDeRegraNegocio:
            assert True

def test_emprestimo_livro_indisponivel():
    with Session(motor) as sessao:
        livro = sessao.get(Livro, 5)
        livro.disponivel = False
        sessao.commit()
        try:
            regras.criar_emprestimo(sessao, usuario_id=2, livro_id=5)
            assert False
        except ErroDeRegraNegocio:
            assert True
        finally:
            livro.disponivel = True
            sessao.commit()


def test_emprestimo_mesmo_livro_para_outro_usuario_falha():
    """Não deve permitir emprestar um livro já emprestado a outro usuário."""
    with Session(motor) as sessao:
        livro = sessao.get(Livro, 3)
        livro.disponivel = False
        sessao.commit()

        try:
            regras.criar_emprestimo(sessao, usuario_id=2, livro_id=3)
            assert False, "Deveria falhar pois o livro está indisponível"
        except ErroDeRegraNegocio:
            assert True
        finally:
            livro.disponivel = True
            sessao.commit()

def test_criar_emprestimo_usuario_e_livro_validos():
    with Session(motor) as sessao:
        usuario = sessao.get(Usuario, 1)
        usuario.qtd_emprestimo = 0  # reset
        sessao.commit()

        emprestimo = regras.criar_emprestimo(sessao, usuario_id=1, livro_id=4)
        assert emprestimo.usuario_id == 1
        assert emprestimo.livro_id == 4


def test_usuario_nao_pode_emprestar_mesmo_livro_duas_vezes():
    with Session(motor) as sessao:
        usuario = sessao.get(Usuario, 1)
        usuario.qtd_emprestimo = 0  # reset antes do teste
        sessao.commit()

        emprestimo1 = regras.criar_emprestimo(sessao, usuario_id=1, livro_id=1)

        # Tenta emprestar o mesmo livro novamente
        try:
            regras.criar_emprestimo(sessao, usuario_id=1, livro_id=1)
            assert False, "Usuário não deveria conseguir emprestar o mesmo livro duas vezes."
        except ErroDeRegraNegocio:
            assert True

from sqlmodel import Session
from src.db.conexao import motor
from src.server import regras
from src.configuracoes.excecoes import ErroDeRegraNegocio
from src.db.modelos import Usuario, Livro

def test_usuario_com_multa_nao_pode_emprestar():
    with Session(motor) as sessao:
        # Simula um usuário existente com multa aberta
        usuario = sessao.get(Usuario, 2)
        usuario.possui_multa_aberta = True
        sessao.commit()

        livro = sessao.get(Livro, 2)
        livro.disponivel = True
        sessao.commit()

        try:
            regras.criar_emprestimo(sessao, usuario_id=usuario.id, livro_id=livro.id)
            assert False, "Deveria falhar com ErroDeRegraNegocio pois o usuário possui multa"
        except ErroDeRegraNegocio:
            assert True
        finally:
            # Restaura o estado original
            usuario.possui_multa_aberta = False
            sessao.commit()
