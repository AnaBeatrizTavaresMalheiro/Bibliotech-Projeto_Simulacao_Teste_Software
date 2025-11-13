from datetime import date, timedelta
import pytest

from src.db.modelos import Emprestimo, Livro, Usuario
from src.server.regras import processar_devolucao
from src.configuracoes.excecoes import ErroDeRegraNegocio


# 🔹 Cenário 3 — Devolução duplicada (erro de regra)
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
