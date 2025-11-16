from sqlmodel import Session, select
from datetime import date

from aplicacao.db.models import Emprestimo, Livro, Usuario
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado, ErroDeRegraNegocio
from aplicacao.configuracoes.config import config


class EmprestimoService:
    def __init__(self, session: Session):
        self.session = session

    def criar(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def devolver(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp
