from sqlmodel import Session
from sqlalchemy import select
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio
from aplicacao.db.models import Usuario
import types


def _ensure_session(sessao):
    """
    Garante que 'sessao' seja um objeto Session e não um generator.
    Isso protege contra mutações do Mutmut e usos incorretos.
    """
    if isinstance(sessao, types.GeneratorType):
        sessao = next(sessao)
    return sessao


def garantir_usuario_existe(sessao: Session, usuario_id: int) -> Usuario:
    sessao = _ensure_session(sessao)

    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")
    return usuario


def garantir_usuario_sem_multa(sessao: Session, usuario_id: int) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def garantir_usuario_nao_ultrapassou_limite(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    usuario = garantir_usuario_existe(sessao, usuario_id)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def validar_usuario_para_emprestimo(sessao: Session, usuario_id: int, limite: int = 3) -> None:
    sessao = _ensure_session(sessao)

    garantir_usuario_existe(sessao, usuario_id)
    garantir_usuario_sem_multa(sessao, usuario_id)
    garantir_usuario_nao_ultrapassou_limite(sessao, usuario_id, limite)


def validar_usuario_unico(sessao, email: str):
    sessao = _ensure_session(sessao)

    existente = None

    # SQLModel
    if hasattr(sessao, "exec"):
        existente = sessao.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    # SQLAlchemy
    else:
        existente = sessao.query(Usuario).filter_by(email=email).first()

    if existente:
        raise ErroDeRegraNegocio("E-mail já cadastrado.")

    return True
