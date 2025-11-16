from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional, List
from pydantic import BaseModel, EmailStr, constr
from sqlmodel import Session, select, col

from aplicacao.db.sessao import get_session
from aplicacao.db.models import Usuario, Emprestimo
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado, ErroDeRegraNegocio


router = APIRouter()


# DTOs ----------------------------------------------

class UsuarioIn(BaseModel):
    nome: constr(min_length=1)
    email: EmailStr
    possui_multa_aberta: Optional[bool] = False


class UsuarioOut(BaseModel):
    id: int
    nome: str
    email: str
    possui_multa_aberta: bool

    class Config:
        orm_mode = True


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    possui_multa_aberta: Optional[bool] = None


# Rotas ----------------------------------------------

@router.post("/", response_model=UsuarioOut, status_code=201)
def criar_usuario(payload: UsuarioIn, sessao: Session = Depends(get_session)):
    stmt = select(Usuario).where(Usuario.email == payload.email)
    existente = sessao.exec(stmt).first()

    if existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    usuario = Usuario(**payload.model_dump())
    sessao.add(usuario)
    sessao.commit()
    sessao.refresh(usuario)
    return usuario


@router.get("/{usuario_id}", response_model=UsuarioOut)
def get_usuario(usuario_id: int, sessao: Session = Depends(get_session)):
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@router.get("/", response_model=List[UsuarioOut])
def listar_usuarios(
    nome: Optional[str] = None,
    email: Optional[str] = None,
    possui_multa_aberta: Optional[bool] = None,
    qtd_min: Optional[int] = None,
    qtd_max: Optional[int] = None,
    ordenar_por: str = "id",
    ordem: str = "asc",
    limit: int = 50,
    offset: int = 0,
    sessao: Session = Depends(get_session),
):
    stmt = select(Usuario)

    if nome:
        stmt = stmt.where(col(Usuario.nome).ilike(f"%{nome}%"))
    if email:
        stmt = stmt.where(col(Usuario.email).ilike(f"%{email}%"))
    if possui_multa_aberta is True:
        stmt = stmt.where(Usuario.possui_multa_aberta.is_(True))
    elif possui_multa_aberta is False:
        stmt = stmt.where(Usuario.possui_multa_aberta.is_(False))

    if qtd_min is not None:
        stmt = stmt.where(Usuario.qtd_emprestimo >= qtd_min)
    if qtd_max is not None:
        stmt = stmt.where(Usuario.qtd_emprestimo <= qtd_max)

    mapa_ord = {
        "id": Usuario.id,
        "nome": Usuario.nome,
        "email": Usuario.email,
        "qtd_emprestimo": Usuario.qtd_emprestimo,
        "possui_multa_aberta": Usuario.possui_multa_aberta,
    }

    coluna = mapa_ord.get(ordenar_por, Usuario.id)

    stmt = stmt.order_by(
        coluna.desc() if ordem == "desc" else coluna.asc()
    ).offset(offset).limit(limit)

    return sessao.exec(stmt).all()


@router.patch("/{usuario_id}", response_model=UsuarioOut)
def atualizar_usuario(usuario_id: int, payload: UsuarioUpdate, sessao: Session = Depends(get_session)):
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroNaoEncontrado("Usuário não encontrado.")

    dados = payload.model_dump(exclude_unset=True)
    for k, v in dados.items():
        setattr(usuario, k, v)

    sessao.commit()
    sessao.refresh(usuario)
    return usuario


@router.delete("/{usuario_id}", status_code=204)
def remover_usuario(usuario_id: int, sessao: Session = Depends(get_session)):
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroNaoEncontrado("Usuário não encontrado.")

    ativo = sessao.exec(
        select(Emprestimo).where(
            Emprestimo.usuario_id == usuario_id,
            Emprestimo.data_devolucao_real.is_(None)
        )
    ).first()

    if ativo:
        raise ErroDeRegraNegocio("Usuário possui empréstimo ativo; não pode ser removido.")

    sessao.delete(usuario)
    sessao.commit()
