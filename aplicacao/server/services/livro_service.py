from sqlmodel import Session, select
from aplicacao.db.models import Livro
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado, ErroDeRegraNegocio


class LivroService:
    def __init__(self, session: Session):
        self.session = session

    def listar(self):
        return self.session.exec(select(Livro)).all()

    def obter(self, livro_id: int):
        livro = self.session.get(Livro, livro_id)
        if not livro:
            raise ErroNaoEncontrado(f"Livro {livro_id} não encontrado")
        return livro

    def criar(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro
