from datetime import date, timedelta
import pytest
from sqlmodel import Session
from src.db.modelos import Emprestimo, Livro, Usuario
from src.server.regras import processar_devolucao
from src.configuracoes.excecoes import ErroDeRegraNegocio
from src.db.conexao import motor
from src.server import regras


def test_devolucao_duplicada():
    usuario = Usuario(id=3, nome="Carlos Mendes", qtd_emprestimo=1)
    livro = Livro(id=3, titulo="Dom Casmurro", disponivel=False)
    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=date.today(),
        data_devolucao_prevista=date.today(),
        data_devolucao_real=date.today()
    )

    with pytest.raises(ErroDeRegraNegocio, match="já foi devolvido"):
        processar_devolucao(sessao=None, emprestimo=emprestimo, data_devolucao_real=date.today())



def test_devolucao_livro_inexistente():
    """Testa se o sistema lida corretamente com devolução de um livro inexistente."""
    with Session(motor) as sessao:
        emprestimo = Emprestimo(
            usuario_id=1,
            livro_id=999,
            data_emprestimo=date.today() - timedelta(days=3),  # define a data de empréstimo
            data_devolucao_prevista=date.today() - timedelta(days=1)
        )

        try:
            regras.processar_devolucao(sessao, emprestimo, date.today())
        except ErroDeRegraNegocio:
            assert True 
        else:
            assert False, "Era esperado erro de livro inexistente."