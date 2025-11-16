import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi import APIRouter, Depends
from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field, EmailStr, constr # Importações adicionadas
from sqlmodel import Session, select, col
from fastapi import Query, HTTPException


from src.db.conexao import obter_sessao
from src.db.modelos import Livro, Usuario, Emprestimo
from src.server.regras import garantir_usuario_pode_emprestar, garantir_livro_disponivel, processar_devolucao
from src.configuracoes.excecoes import ErroNaoEncontrado, ErroDeRegraNegocio

app_rotas = APIRouter()

# =========================================================
# DTOs públicos (sem Relationship) — ficam neste arquivo
# =========================================================
class LivroIn(BaseModel):
    titulo: str = Field(..., min_length=1)
    isbn: str = Field(..., min_length=5)
    disponivel: Optional[bool] = True

class LivroOut(BaseModel):
    id: int
    titulo: str
    isbn: str
    disponivel: bool

class LivroUpdate(BaseModel):
    titulo: Optional[str] = Field(None, min_length=1)
    isbn: Optional[str] = Field(None, min_length=5)
    disponivel: Optional[bool] = None

class UsuarioIn(BaseModel): # DTO unificado e validado
    nome: constr(min_length=1)
    email: EmailStr
    possui_multa_aberta: Optional[bool] = False
    # Nota: qtd_emprestimo não está aqui pois é calculado pelo backend

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

class EmprestimoIn(BaseModel):
    livro_id: int
    usuario_id: int
    data_emprestimo: date
    data_devolucao_prevista: date

class DevolucaoIn(BaseModel):
    data_devolucao_real: date

class EmprestimoOut(BaseModel):
    id: int
    livro_id: int
    usuario_id: int
    data_emprestimo: date
    data_devolucao_prevista: date
    data_devolucao_real: Optional[date] = None
    dias_atraso: int
    valor_multa: float

class EmprestimoUpdate(BaseModel):
    # permitido alterar apenas a data prevista (prorrogação)
    data_devolucao_prevista: Optional[date] = None

class EmprestimoListDetalheOut(BaseModel):
    id: int
    usuario_id: int
    livro_id: int
    data_emprestimo: date
    data_devolucao_prevista: date
    data_devolucao_real: Optional[date] = None
    dias_atraso: int
    valor_multa: float


# =========================================================
# LIVROS
# =========================================================
@app_rotas.post("/livros", response_model=LivroOut, status_code=201)
def criar_livro(payload: LivroIn, sessao: Session = Depends(obter_sessao)):
    livro = Livro(**payload.dict())  
    sessao.add(livro)
    sessao.commit()
    sessao.refresh(livro)
    return livro



@app_rotas.get("/livros", response_model=List[LivroOut])
def listar_todos_os_livros(
    ordenar_por: str = Query(default="id", description="id|titulo|isbn|disponivel"),
    ordem: str = Query(default="asc", description="asc|desc"),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    sessao: Session = Depends(obter_sessao),
):
    cols = {
        "id": Livro.id,
        "titulo": Livro.titulo,
        "isbn": Livro.isbn,
        "disponivel": Livro.disponivel,
    }
    coluna = cols.get(ordenar_por, Livro.id)
    stmt = select(Livro).order_by(coluna.desc() if ordem.lower()=="desc" else coluna.asc())
    stmt = stmt.offset(offset).limit(limit)
    return sessao.exec(stmt).all()

@app_rotas.patch("/livros/{livro_id}", response_model=LivroOut)
def atualizar_livro(livro_id: int, payload: LivroUpdate, sessao: Session = Depends(obter_sessao)):
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroNaoEncontrado("Livro não encontrado.")
    dados = payload.model_dump(exclude_unset=True)
    for k, v in dados.items():
        setattr(livro, k, v)
    sessao.add(livro)
    sessao.commit()
    sessao.refresh(livro)
    return livro

@app_rotas.delete("/livros/{livro_id}", status_code=204)
def remover_livro(livro_id: int, sessao: Session = Depends(obter_sessao)):
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroNaoEncontrado("Livro não encontrado.")
    # Não deletar livro com empréstimo ativo
    emprestimo_ativo = sessao.exec(
        select(Emprestimo).where(
            Emprestimo.livro_id == livro_id,
            Emprestimo.data_devolucao_real.is_(None)
        )
    ).first()
    if emprestimo_ativo:
        raise ErroDeRegraNegocio("Livro possui empréstimo ativo; não pode ser deletado.")
    sessao.delete(livro)
    sessao.commit()
    return None


# =========================================================
# USUÁRIOS
# =========================================================
@app_rotas.post("/usuarios", response_model=UsuarioOut, status_code=201)
def criar_usuario(payload: UsuarioIn, sessao: Session = Depends(obter_sessao)):
    print("==> payload recebido:", payload.dict())

    # 💥 CORREÇÃO: Usando sessao.exec(select(...)) em vez de sessao.query(...)
    stmt = select(Usuario).where(Usuario.email == payload.email)
    usuario_existente = sessao.exec(stmt).first()
    
    print("==> usuario_existente:", usuario_existente)

    if usuario_existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    usuario = Usuario(**payload.model_dump())
    sessao.add(usuario)
    sessao.commit()
    sessao.refresh(usuario)
    print("==> usuario criado:", usuario)
    return usuario


@app_rotas.get("/usuarios/{usuario_id}", response_model=UsuarioOut)
def get_usuario(usuario_id: int, sessao: Session = Depends(obter_sessao)):
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail=f"Usuário {usuario_id} não encontrado")
    return usuario


@app_rotas.get("/usuarios", response_model=List[UsuarioOut])
def listar_usuarios(
    # filtros
    nome: Optional[str] = Query(default=None, description="Busca parcial no nome (case-insensitive)"),
    email: Optional[str] = Query(default=None, description="Busca parcial no e-mail (case-insensitive)"),
    possui_multa_aberta: Optional[bool] = Query(default=None, description="True=tem multa; False=sem multa"),
    qtd_min: Optional[int] = Query(default=None, ge=0, description="Mínimo de empréstimos ativos"),
    qtd_max: Optional[int] = Query(default=None, ge=0, description="Máximo de empréstimos ativos"),
    # ordenação/paginação
    ordenar_por: str = Query(default="id", description="Campos: id, nome, email, qtd_emprestimo, possui_multa_aberta"),
    ordem: str = Query(default="asc", description="asc | desc"),
    limit: int = Query(default=50, ge=1, le=200, description="Máximo de registros retornados"),
    offset: int = Query(default=0, ge=0, description="Pular N registros"),
    sessao: Session = Depends(obter_sessao),
):
    stmt = select(Usuario)

    # Filtros
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

    # Ordenação segura (whitelist)
    mapa_ord = {
        "id": Usuario.id,
        "nome": Usuario.nome,
        "email": Usuario.email,
        "qtd_emprestimo": Usuario.qtd_emprestimo,
        "possui_multa_aberta": Usuario.possui_multa_aberta,
    }
    coluna = mapa_ord.get(ordenar_por, Usuario.id)
    stmt = stmt.order_by(coluna.desc() if ordem.lower() == "desc" else coluna.asc())

    # Paginação
    stmt = stmt.offset(offset).limit(limit)

    return sessao.exec(stmt).all()


@app_rotas.patch("/usuarios/{usuario_id}", response_model=UsuarioOut)
def atualizar_usuario(usuario_id: int, payload: UsuarioUpdate, sessao: Session = Depends(obter_sessao)):
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroNaoEncontrado("Usuário não encontrado.")
    dados = payload.model_dump(exclude_unset=True)
    for k, v in dados.items():
        setattr(usuario, k, v)
    sessao.add(usuario)
    sessao.commit()
    sessao.refresh(usuario)
    return usuario

@app_rotas.delete("/usuarios/{usuario_id}", status_code=204)
def remover_usuario(usuario_id: int, sessao: Session = Depends(obter_sessao)):
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroNaoEncontrado("Usuário não encontrado.")
    # Não deletar usuário com empréstimo ativo
    emprestimo_ativo = sessao.exec(
        select(Emprestimo).where(
            Emprestimo.usuario_id == usuario_id,
            Emprestimo.data_devolucao_real.is_(None)
        )
    ).first()
    if emprestimo_ativo:
        raise ErroDeRegraNegocio("Usuário possui empréstimo ativo; não pode ser deletado.")
    sessao.delete(usuario)
    sessao.commit()
    return None


# =========================================================
# EMPRÉSTIMOS
# =========================================================
@app_rotas.post("/emprestimos", response_model=EmprestimoOut)
def criar_emprestimo(payload: EmprestimoIn, sessao: Session = Depends(obter_sessao)):
    garantir_usuario_pode_emprestar(sessao, payload.usuario_id)
    garantir_livro_disponivel(sessao, payload.livro_id)

    emprestimo = Emprestimo(**payload.model_dump())
    sessao.add(emprestimo)

    # Atualiza disponibilidade do livro
    livro = sessao.get(Livro, payload.livro_id)
    livro.disponivel = False

    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo

@app_rotas.post("/emprestimos/{emprestimo_id}/devolucao", response_model=EmprestimoOut)
def devolver_emprestimo(emprestimo_id: int, payload: DevolucaoIn, sessao: Session = Depends(obter_sessao)):
    emprestimo = sessao.get(Emprestimo, emprestimo_id)
    if not emprestimo:
        raise ErroNaoEncontrado("Empréstimo não encontrado.")
    processar_devolucao(sessao, emprestimo, payload.data_devolucao_real)
    livro = sessao.get(Livro, emprestimo.livro_id)
    livro.disponivel = True
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo

@app_rotas.patch("/emprestimos/{emprestimo_id}", response_model=EmprestimoOut)
def atualizar_emprestimo(emprestimo_id: int, payload: EmprestimoUpdate, sessao: Session = Depends(obter_sessao)):
    emprestimo = sessao.get(Emprestimo, emprestimo_id)
    if not emprestimo:
        raise ErroNaoEncontrado("Empréstimo não encontrado.")
    dados = payload.model_dump(exclude_unset=True)
    # Só permitimos prorrogar a data prevista se ainda não foi devolvido
    if "data_devolucao_prevista" in dados:
        if emprestimo.data_devolucao_real is not None:
            raise ErroDeRegraNegocio("Não é possível prorrogar um empréstimo já devolvido.")
        emprestimo.data_devolucao_prevista = dados["data_devolucao_prevista"]
    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo

@app_rotas.delete("/emprestimos/{emprestimo_id}", status_code=204)
def remover_emprestimo(emprestimo_id: int, sessao: Session = Depends(obter_sessao)):
    emprestimo = sessao.get(Emprestimo, emprestimo_id)
    if not emprestimo:
        raise ErroNaoEncontrado("Empréstimo não encontrado.")
    # Só remover empréstimo já devolvido (registro histórico)
    if emprestimo.data_devolucao_real is None:
        raise ErroDeRegraNegocio("Não é possível remover empréstimo ativo; devolva primeiro.")
    sessao.delete(emprestimo)
    sessao.commit()
    return None

from fastapi import Query

@app_rotas.get("/emprestimos", response_model=List[EmprestimoListDetalheOut])
def listar_emprestimos(
    # filtros (opcionais)
    usuario_id: Optional[int] = Query(default=None, description="Filtra por usuário"),
    livro_id: Optional[int] = Query(default=None, description="Filtra por livro"),
    ativos: Optional[bool] = Query(default=None, description="True = apenas ativos; False = apenas devolvidos"),
    data_ini: Optional[date] = Query(default=None, description="Data emprestimo inicial (YYYY-MM-DD)"),
    data_fim: Optional[date] = Query(default=None, description="Data emprestimo final (YYYY-MM-DD)"),
    # ordenação
    ordenar_por: str = Query(default="id", description="Campos: id, data_emprestimo, data_devolucao_prevista, usuario_id, livro_id"),
    ordem: str = Query(default="asc", description="asc | desc"),
    sessao: Session = Depends(obter_sessao),
):
    # base
    stmt = select(Emprestimo)

    # filtros
    if usuario_id is not None:
        stmt = stmt.where(Emprestimo.usuario_id == usuario_id)
    if livro_id is not None:
        stmt = stmt.where(Emprestimo.livro_id == livro_id)
    if ativos is True:
        stmt = stmt.where(Emprestimo.data_devolucao_real.is_(None))
    elif ativos is False:
        stmt = stmt.where(Emprestimo.data_devolucao_real.is_not(None))
    if data_ini is not None:
        stmt = stmt.where(Emprestimo.data_emprestimo >= data_ini)
    if data_fim is not None:
        stmt = stmt.where(Emprestimo.data_emprestimo <= data_fim)

    # ordenação segura (whitelist)
    mapa_ord = {
        "id": Emprestimo.id,
        "data_emprestimo": Emprestimo.data_emprestimo,
        "data_devolucao_prevista": Emprestimo.data_devolucao_prevista,
        "usuario_id": Emprestimo.usuario_id,
        "livro_id": Emprestimo.livro_id,
    }
    coluna = mapa_ord.get(ordenar_por, Emprestimo.id)
    stmt = stmt.order_by(coluna.desc() if ordem.lower() == "desc" else coluna.asc())

    return sessao.exec(stmt).all()