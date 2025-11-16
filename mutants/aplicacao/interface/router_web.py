from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_303_SEE_OTHER
from sqlmodel import Session, select
from pathlib import Path
from datetime import date, timedelta

from aplicacao.db.sessao import get_session
from aplicacao.db.models import Usuario, Livro, Emprestimo
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio, ErroNaoEncontrado

router = APIRouter(prefix="/web")

ROOT_DIR = Path(__file__).resolve().parents[1]
templates = Jinja2Templates(directory=str(ROOT_DIR / "interface" / "templates"))
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result

# ----------------------------- HOME -----------------------------
@router.get("/", include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ============================================================ USUÁRIOS ============================================================

@router.get("/usuarios")
def list_usuarios(request: Request, session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario)).all()
    return templates.TemplateResponse(
        "usuarios_list.html",
        {"request": request, "usuarios": usuarios},
    )


@router.get("/usuarios/novo")
def usuario_novo(request: Request):
    return templates.TemplateResponse("usuario_form.html", {"request": request})


@router.post("/usuarios/novo")
def usuario_criar(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    session: Session = Depends(get_session)
):
    try:
        if not nome or not email:
            raise ErroDeRegraNegocio("Nome e e-mail são obrigatórios.")

        existente = session.exec(select(Usuario).where(Usuario.email == email)).first()
        if existente:
            raise ErroDeRegraNegocio("Já existe um usuário com este e-mail.")

        usuario = Usuario(nome=nome, email=email)
        session.add(usuario)
        session.commit()

        return RedirectResponse("/web/usuarios", HTTP_303_SEE_OTHER)

    except ErroDeRegraNegocio as e:
        return templates.TemplateResponse(
            "usuario_form.html",
            {"request": request, "erro": str(e), "usuario": {"nome": nome, "email": email}},
        )


@router.get("/usuarios/{id}/editar")
def usuario_editar(request: Request, id: int, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, id)
    if not usuario:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Usuário não encontrado"},
            status_code=404,
        )
    return templates.TemplateResponse(
        "usuario_form.html",
        {"request": request, "usuario": usuario},
    )


@router.post("/usuarios/{id}/editar")
def usuario_atualizar(
    request: Request,
    id: int,
    nome: str = Form(...),
    email: str = Form(...),
    session: Session = Depends(get_session),
):
    usuario = session.get(Usuario, id)
    if not usuario:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Usuário não encontrado"},
            status_code=404,
        )

    try:
        if not nome or not email:
            raise ErroDeRegraNegocio("Nome e e-mail são obrigatórios.")

        conflito = session.exec(
            select(Usuario).where(Usuario.email == email, Usuario.id != id)
        ).first()
        if conflito:
            raise ErroDeRegraNegocio("E-mail já está sendo usado por outro usuário.")

        usuario.nome = nome
        usuario.email = email
        session.commit()

        return RedirectResponse("/web/usuarios", HTTP_303_SEE_OTHER)

    except ErroDeRegraNegocio as e:
        return templates.TemplateResponse(
            "usuario_form.html",
            {"request": request, "usuario": usuario, "erro": str(e)},
        )


@router.post("/usuarios/{id}/deletar")
def usuario_deletar(request: Request, id: int, session: Session = Depends(get_session)):
    usuario = session.get(Usuario, id)
    if not usuario:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Usuário não encontrado"},
            status_code=404,
        )

    emprestimos = session.exec(
        select(Emprestimo).where(
            Emprestimo.usuario_id == id,
            Emprestimo.data_devolucao_real.is_(None)
        )
    ).all()

    if emprestimos:
        usuarios = session.exec(select(Usuario)).all()
        return templates.TemplateResponse(
            "usuarios_list.html",
            {
                "request": request,
                "usuarios": usuarios,
                "erro": "Usuário possui empréstimo ativo e não pode ser excluído.",
            },
        )

    session.delete(usuario)
    session.commit()

    return RedirectResponse("/web/usuarios", HTTP_303_SEE_OTHER)

# ============================================================ LIVROS ============================================================

@router.get("/livros")
def list_livros(request: Request, session: Session = Depends(get_session)):
    livros = session.exec(select(Livro)).all()
    return templates.TemplateResponse(
        "livros_list.html",
        {"request": request, "livros": livros},
    )


@router.get("/livros/novo")
def livro_novo(request: Request):
    return templates.TemplateResponse("livro_form.html", {"request": request})


@router.post("/livros/novo")
def livro_criar(
    request: Request,
    titulo: str = Form(...),
    isbn: str = Form(...),
    session: Session = Depends(get_session)
):
    try:
        if not titulo or not isbn:
            raise ErroDeRegraNegocio("Título e ISBN são obrigatórios.")

        existente = session.exec(select(Livro).where(Livro.isbn == isbn)).first()
        if existente:
            raise ErroDeRegraNegocio("Já existe um livro com este ISBN.")

        livro = Livro(titulo=titulo, isbn=isbn, disponivel=True)
        session.add(livro)
        session.commit()

        return RedirectResponse("/web/livros", HTTP_303_SEE_OTHER)

    except ErroDeRegraNegocio as e:
        return templates.TemplateResponse(
            "livro_form.html",
            {"request": request, "erro": str(e), "livro": {"titulo": titulo, "isbn": isbn}},
        )


@router.get("/livros/{id}/editar")
def livro_editar(request: Request, id: int, session: Session = Depends(get_session)):
    livro = session.get(Livro, id)
    if not livro:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Livro não encontrado"},
            status_code=404,
        )

    return templates.TemplateResponse(
        "livro_form.html",
        {"request": request, "livro": livro},
    )


@router.post("/livros/{id}/editar")
def livro_atualizar(
    request: Request,
    id: int,
    titulo: str = Form(...),
    isbn: str = Form(...),
    session: Session = Depends(get_session),
):
    livro = session.get(Livro, id)
    if not livro:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Livro não encontrado"},
            status_code=404,
        )

    try:
        if not titulo or not isbn:
            raise ErroDeRegraNegocio("Título e ISBN são obrigatórios.")

        conflito = session.exec(
            select(Livro).where(Livro.isbn == isbn, Livro.id != id)
        ).first()
        if conflito:
            raise ErroDeRegraNegocio("ISBN já está cadastrado em outro livro.")

        livro.titulo = titulo
        livro.isbn = isbn
        session.commit()

        return RedirectResponse("/web/livros", HTTP_303_SEE_OTHER)

    except ErroDeRegraNegocio as e:
        return templates.TemplateResponse(
            "livro_form.html",
            {"request": request, "livro": livro, "erro": str(e)},
        )


@router.post("/livros/{id}/deletar")
def livro_deletar(request: Request, id: int, session: Session = Depends(get_session)):
    livro = session.get(Livro, id)
    if not livro:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Livro não encontrado"},
            status_code=404,
        )

    emprestimos_ativos = session.exec(
        select(Emprestimo).where(
            Emprestimo.livro_id == id,
            Emprestimo.data_devolucao_real.is_(None)
        )
    ).all()

    if emprestimos_ativos:
        livros = session.exec(select(Livro)).all()
        return templates.TemplateResponse(
            "livros_list.html",
            {
                "request": request,
                "livros": livros,
                "erro": "Livro possui empréstimo ativo e não pode ser excluído.",
            },
        )

    session.delete(livro)
    session.commit()

    return RedirectResponse("/web/livros", HTTP_303_SEE_OTHER)

# ============================================================ EMPRÉSTIMOS ============================================================

@router.get("/emprestimos")
def list_emprestimos(request: Request, session: Session = Depends(get_session)):
    emprestimos = session.exec(select(Emprestimo)).all()
    return templates.TemplateResponse(
        "emprestimos_list.html",
        {"request": request, "emprestimos": emprestimos},
    )


@router.get("/emprestimos/novo")
def emprestimo_novo(request: Request, session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario)).all()
    livros = session.exec(select(Livro).where(Livro.disponivel == True)).all()

    return templates.TemplateResponse(
        "emprestimo_form.html",
        {"request": request, "usuarios": usuarios, "livros": livros, "erro": None},
    )


@router.post("/emprestimos/novo")
def emprestimo_criar(
    request: Request,
    usuario_id: int = Form(...),
    livro_id: int = Form(...),
    session: Session = Depends(get_session),
):
    try:
        usuario = session.get(Usuario, usuario_id)
        livro = session.get(Livro, livro_id)

        if not usuario or not livro:
            raise ErroNaoEncontrado("Usuário ou livro não encontrado.")

        if usuario.possui_multa_aberta:
            raise ErroDeRegraNegocio("Usuário possui multa em aberto.")

        emprestimos_ativos = session.exec(
            select(Emprestimo).where(
                Emprestimo.usuario_id == usuario_id,
                Emprestimo.data_devolucao_real.is_(None)
            )
        ).all()

        if len(emprestimos_ativos) >= 3:
            raise ErroDeRegraNegocio("Usuário já possui 3 empréstimos ativos.")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro indisponível.")

        hoje = date.today()
        devolucao = hoje + timedelta(days=7)

        emprestimo = Emprestimo(
            usuario_id=usuario_id,
            livro_id=livro_id,
            data_emprestimo=hoje,
            data_devolucao_prevista=devolucao,
        )

        session.add(emprestimo)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        session.commit()

        return RedirectResponse("/web/emprestimos", HTTP_303_SEE_OTHER)

    except (ErroNaoEncontrado, ErroDeRegraNegocio) as e:
        usuarios = session.exec(select(Usuario)).all()
        livros = session.exec(select(Livro).where(Livro.disponivel == True)).all()
        return templates.TemplateResponse(
            "emprestimo_form.html",
            {"request": request, "usuarios": usuarios, "livros": livros, "erro": str(e)},
        )


@router.post("/emprestimos/{id}/devolver")
def emprestimo_devolver(id: int, session: Session = Depends(get_session)):
    emprestimo = session.get(Emprestimo, id)
    if not emprestimo:
        return RedirectResponse("/web/emprestimos", HTTP_303_SEE_OTHER)

    if emprestimo.data_devolucao_real:
        return RedirectResponse("/web/emprestimos", HTTP_303_SEE_OTHER)

    hoje = date.today()
    emprestimo.data_devolucao_real = hoje

    atraso = 0
    multa = 0

    if emprestimo.data_devolucao_prevista:
        diff = (hoje - emprestimo.data_devolucao_prevista).days
        atraso = max(diff, 0)
        multa = atraso * 1.5

    emprestimo.dias_atraso = atraso
    emprestimo.valor_multa = multa

    livro = session.get(Livro, emprestimo.livro_id)
    usuario = session.get(Usuario, emprestimo.usuario_id)

    livro.disponivel = True
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    if multa > 0:
        usuario.possui_multa_aberta = True

    session.commit()

    return RedirectResponse("/web/emprestimos", HTTP_303_SEE_OTHER)
