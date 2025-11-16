from sqlmodel import Session
from sqlalchemy import select
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio
from aplicacao.db.models import Livro


def garantir_livro_existe(sessao: Session, livro_id: int) -> Livro:
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    return livro


def garantir_livro_disponivel(sessao: Session, livro_id: int) -> None:
    livro = garantir_livro_existe(sessao, livro_id)
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")

def validar_livro_unico(sessao, isbn: str):
    existente = None

    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Livro).where(Livro.isbn == isbn)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Livro).filter(Livro.isbn == isbn).first()

    if existente:
        raise ErroDeRegraNegocio("ISBN já cadastrado.")

    return True