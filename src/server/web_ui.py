from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_303_SEE_OTHER
from datetime import date

from src.db.conexao import obter_sessao
from src.db.modelos import Usuario, Livro, Emprestimo
from src.configuracoes.excecoes import ErroDeRegraNegocio, ErroNaoEncontrado

from sqlalchemy import select, text

from fastapi.responses import HTMLResponse

import json
from pathlib import Path
from datetime import datetime
from src.db.modelos import Usuario, Livro, Emprestimo

from fastapi import Depends
from sqlalchemy.orm import Session  # se estiver usando SQLAlchemy puro
from src.db.conexao import obter_sessao

# templates & static
# templates = Jinja2Templates(directory="src/server/templates")
# mount static - o main.py já incluiu o router; o app principal monta a pasta estática no main

ROOT_DIR = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = ROOT_DIR / "server" / "templates"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


router = APIRouter(prefix="/web")

    
# --- Home web
@router.get("/", include_in_schema=False)
def web_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ------------------ USUÁRIOS ------------------
# @router.get("/usuarios")
# def web_list_usuarios(request: Request, q: str | None = None, sessao: Session = Depends(obter_sessao)):
#     usuarios = sessao.exec(select(Usuario)).all() if hasattr(sessao, 'exec') else sessao.query(Usuario).all()
#     if q:
#         usuarios = [u for u in usuarios if q.lower() in u.nome.lower()]
#     return templates.TemplateResponse("usuarios_list.html", {"request": request, "usuarios": usuarios})

from sqlalchemy.orm import selectinload

@router.get("/usuarios")
def web_list_usuarios(request: Request, q: str | None = None, sessao: Session = Depends(obter_sessao)):
    resultado = sessao.exec(select(Usuario)) if hasattr(sessao, 'exec') else sessao.query(Usuario)
    usuarios = [r[0] if not isinstance(r, Usuario) else r for r in resultado]

    if q:
        usuarios = [u for u in usuarios if q.lower() in u.nome.lower()]

    usuarios_dict = [
        {
            "id": u.id,
            "nome": u.nome,
            "email": u.email,
            "qtd_emprestimo": u.qtd_emprestimo,
            "possui_multa_aberta": u.possui_multa_aberta,
        }
        for u in usuarios
    ]

    return templates.TemplateResponse(
        "usuarios_list.html",
        {"request": request, "usuarios": usuarios_dict},
    )



@router.get("/usuarios/novo")
def web_usuario_novo(request: Request):
    return templates.TemplateResponse("usuario_form.html", {"request": request, "usuario": None})

@router.post("/usuarios/novo")
async def web_usuario_criar(request: Request):
    form = await request.form()
    nome = form.get("nome", "").strip()
    email = form.get("email", "").strip()
    sessao = next(obter_sessao())
    try:
        # validação simples
        if not nome:
            raise ErroDeRegraNegocio("Nome obrigatório")
        # duplicidade
        existente = sessao.exec(select(Usuario).where(Usuario.email == email)).first() if hasattr(sessao, 'exec') else sessao.query(Usuario).filter_by(email=email).first()
        if existente:
            raise ErroDeRegraNegocio("E-mail já cadastrado")
        usuario = Usuario(nome=nome, email=email)
        sessao.add(usuario)
        sessao.commit()
        sessao.refresh(usuario)
        return RedirectResponse(url="/web/usuarios", status_code=HTTP_303_SEE_OTHER)
    except ErroDeRegraNegocio as e:
        return templates.TemplateResponse("usuario_form.html", {"request": request, "usuario": {"nome": nome, "email": email}, "erro": str(e)})

@router.get("/usuarios/{usuario_id}/editar")
def web_usuario_editar(request: Request, usuario_id: int):
    sessao = next(obter_sessao())
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        return templates.TemplateResponse("404.html", {"request": request, "mensagem": "Usuário não encontrado"}, status_code=404)
    return templates.TemplateResponse("usuario_form.html", {"request": request, "usuario": usuario})

@router.post("/usuarios/{usuario_id}/editar")
async def web_usuario_update(request: Request, usuario_id: int):
    form = await request.form()
    nome = form.get("nome", "").strip()
    email = form.get("email", "").strip()
    sessao = next(obter_sessao())
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        return templates.TemplateResponse("404.html", {"request": request, "mensagem": "Usuário não encontrado"}, status_code=404)
    try:
        if not nome:
            raise ErroDeRegraNegocio("Nome obrigatório")
        usuario.nome = nome
        usuario.email = email
        sessao.add(usuario)
        sessao.commit()
        sessao.refresh(usuario)
        return RedirectResponse(url="/web/usuarios", status_code=HTTP_303_SEE_OTHER)
    except ErroDeRegraNegocio as e:
        return templates.TemplateResponse("usuario_form.html", {"request": request, "usuario": usuario, "erro": str(e)})

from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

@router.post("/usuarios/{usuario_id}/deletar")
def web_usuario_deletar(
    request: Request,
    usuario_id: int,
    sessao: Session = Depends(obter_sessao),
):
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Usuário não encontrado"},
            status_code=404,
        )

    # Busca TODOS os empréstimos desse usuário
    if hasattr(sessao, "exec"):
        resultado = sessao.exec(
            select(Emprestimo).where(Emprestimo.usuario_id == usuario_id)
        )
        emprestimos = [r[0] if not isinstance(r, Emprestimo) else r for r in resultado]
    else:
        emprestimos = (
            sessao.query(Emprestimo)
            .filter(Emprestimo.usuario_id == usuario_id)
            .all()
        )

    emprestimo_ativo = any(e.data_devolucao_real is None for e in emprestimos)

    if emprestimo_ativo:
        # recarrega lista de usuários no mesmo formato da /web/usuarios
        if hasattr(sessao, "exec"):
            resultado_u = sessao.exec(select(Usuario))
            usuarios = [r[0] if not isinstance(r, Usuario) else r for r in resultado_u]
        else:
            usuarios = sessao.query(Usuario).all()

        usuarios_dict = [
            {
                "id": u.id,
                "nome": u.nome,
                "email": u.email,
                "qtd_emprestimo": u.qtd_emprestimo,
                "possui_multa_aberta": u.possui_multa_aberta,
            }
            for u in usuarios
        ]

        return templates.TemplateResponse(
            "usuarios_list.html",
            {
                "request": request,
                "usuarios": usuarios_dict,
                "erro": "Usuário possui empréstimo ativo e não pode ser excluído.",
            },
        )

    # Se só tem empréstimos devolvidos, podemos excluí-los e depois excluir o usuário
    for e in emprestimos:
        sessao.delete(e)

    sessao.delete(usuario)
    sessao.commit()

    return RedirectResponse(url="/web/usuarios", status_code=HTTP_303_SEE_OTHER)

# ------------------ LIVROS ------------------
@router.get("/livros")
# def web_list_livros(request: Request, q: str | None = None, sessao: Session = Depends(obter_sessao)):
#     livros = sessao.exec(select(Livro)).all() if hasattr(sessao, 'exec') else sessao.query(Livro).all()
#     if q:
#         livros = [l for l in livros if q.lower() in l.titulo.lower()]
#     return templates.TemplateResponse("livros_list.html", {"request": request, "livros": livros, "q": q})

@router.get("/livros")
def web_list_livros(request: Request, q: str | None = None, sessao: Session = Depends(obter_sessao)):
    resultado = sessao.exec(select(Livro)) if hasattr(sessao, 'exec') else sessao.query(Livro)
    livros = [r[0] if not isinstance(r, Livro) else r for r in resultado]

    if q:
        livros = [l for l in livros if q.lower() in l.titulo.lower()]

    livros_dict = [
        {
            "id": l.id,
            "titulo": l.titulo,
            "isbn": l.isbn,
            "disponivel": l.disponivel,
        }
        for l in livros
    ]

    return templates.TemplateResponse(
        "livros_list.html",
        {"request": request, "livros": livros_dict},
    )


@router.get("/livros/novo")
def web_livro_novo(request: Request):
    return templates.TemplateResponse("livro_form.html", {"request": request, "livro": None})

@router.post("/livros/novo")
async def web_livro_criar(request: Request):
    form = await request.form()
    titulo = form.get("titulo", "").strip()
    isbn = form.get("isbn", "").strip()
    sessao = next(obter_sessao())
    try:
        if not titulo or not isbn:
            raise ErroDeRegraNegocio("Título e ISBN obrigatórios")
        existente = sessao.exec(select(Livro).where(Livro.isbn == isbn)).first() if hasattr(sessao, 'exec') else sessao.query(Livro).filter_by(isbn=isbn).first()
        if existente:
            raise ErroDeRegraNegocio("ISBN já cadastrado")
        livro = Livro(titulo=titulo, isbn=isbn, disponivel=True)
        sessao.add(livro)
        sessao.commit()
        sessao.refresh(livro)
        return RedirectResponse(url="/web/livros", status_code=HTTP_303_SEE_OTHER)
    except ErroDeRegraNegocio as e:
        return templates.TemplateResponse("livro_form.html", {"request": request, "livro": {"titulo": titulo, "isbn": isbn}, "erro": str(e)})

@router.post("/livros/{livro_id}/deletar")
def web_livro_deletar(
    request: Request,
    livro_id: int,
    sessao: Session = Depends(obter_sessao),
):
    livro = sessao.get(Livro, livro_id)
    if not livro:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Livro não encontrado"},
            status_code=404,
        )

    # Busca TODOS os empréstimos desse livro
    if hasattr(sessao, "exec"):
        resultado = sessao.exec(
            select(Emprestimo).where(Emprestimo.livro_id == livro_id)
        )
        emprestimos = [r[0] if not isinstance(r, Emprestimo) else r for r in resultado]
    else:
        emprestimos = (
            sessao.query(Emprestimo)
            .filter(Emprestimo.livro_id == livro_id)
            .all()
        )

    # Verifica se existe algum empréstimo ATIVO
    emprestimo_ativo = any(e.data_devolucao_real is None for e in emprestimos)

    if emprestimo_ativo:
        # recarrega lista de livros no mesmo formato da /web/livros
        if hasattr(sessao, "exec"):
            resultado_l = sessao.exec(select(Livro))
            livros = [r[0] if not isinstance(r, Livro) else r for r in resultado_l]
        else:
            livros = sessao.query(Livro).all()

        livros_dict = [
            {
                "id": l.id,
                "titulo": l.titulo,
                "isbn": l.isbn,
                "disponivel": l.disponivel,
            }
            for l in livros
        ]

        return templates.TemplateResponse(
            "livros_list.html",
            {
                "request": request,
                "livros": livros_dict,
                "erro": "Livro possui empréstimo ativo e não pode ser excluído.",
            },
        )

    # Se chegou aqui: não há empréstimo ativo.
    # Podemos apagar os empréstimos históricos (devolvidos) e depois o livro.
    for e in emprestimos:
        sessao.delete(e)

    sessao.delete(livro)
    sessao.commit()

    return RedirectResponse(url="/web/livros", status_code=HTTP_303_SEE_OTHER)



@router.get("/livros/{livro_id}/editar")
def web_livro_editar(request: Request, livro_id: int):
    sessao = next(obter_sessao())
    livro = sessao.get(Livro, livro_id)
    if not livro:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Livro não encontrado"},
            status_code=404,
        )

    return templates.TemplateResponse(
        "livro_form.html",
        {
            "request": request,
            "livro": livro,
        },
    )


@router.post("/livros/{livro_id}/editar")
async def web_livro_update(request: Request, livro_id: int):
    form = await request.form()
    titulo = form.get("titulo", "").strip()
    isbn = form.get("isbn", "").strip()

    sessao = next(obter_sessao())
    livro = sessao.get(Livro, livro_id)

    if not livro:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Livro não encontrado"},
            status_code=404,
        )

    try:
        # validação básica
        if not titulo or not isbn:
            raise ErroDeRegraNegocio("Título e ISBN obrigatórios")

        # checa duplicidade de ISBN em OUTRO livro
        if hasattr(sessao, "exec"):
            existente = sessao.exec(
                select(Livro).where(
                    Livro.isbn == isbn,
                    Livro.id != livro_id,
                )
            ).first()
        else:
            existente = (
                sessao.query(Livro)
                .filter(Livro.isbn == isbn, Livro.id != livro_id)
                .first()
            )

        if existente:
            raise ErroDeRegraNegocio("ISBN já cadastrado em outro livro")

        # aplica alterações
        livro.titulo = titulo
        livro.isbn = isbn

        sessao.add(livro)
        sessao.commit()
        sessao.refresh(livro)

        return RedirectResponse(url="/web/livros", status_code=HTTP_303_SEE_OTHER)

    except ErroDeRegraNegocio as e:
        # volta pro form mantendo o livro e mostrando erro
        return templates.TemplateResponse(
            "livro_form.html",
            {
                "request": request,
                "livro": livro,
                "erro": str(e),
            },
        )

# ------------------ EMPRÉSTIMOS ------------------
# @router.get("/emprestimos")
# def web_list_emprestimos(request: Request, sessao: Session = Depends(obter_sessao)):
#     emprestimos = sessao.exec(select(Emprestimo)).all() if hasattr(sessao, 'exec') else sessao.query(Emprestimo).all()
#     return templates.TemplateResponse("emprestimos_list.html", {"request": request, "emprestimos": emprestimos})


@router.get("/emprestimos")
def web_list_emprestimos(request: Request, sessao: Session = Depends(obter_sessao)):
    if hasattr(sessao, "exec"):  # SQLModel
        resultado = sessao.exec(
            select(Emprestimo)
            .options(
                selectinload(Emprestimo.usuario),
                selectinload(Emprestimo.livro),
            )
        )
        emprestimos = resultado.scalars().all()
    else:  # SQLAlchemy
        emprestimos = (
            sessao.query(Emprestimo)
            .options(
                selectinload(Emprestimo.usuario),
                selectinload(Emprestimo.livro),
            )
            .all()
        )

    return templates.TemplateResponse(
        "emprestimos_list.html",
        {"request": request, "emprestimos": emprestimos},
    )



@router.get("/emprestimos/novo")
def web_emprestimo_novo(request: Request, sessao: Session = Depends(obter_sessao)):
    # Usuários
    resultado_u = sessao.exec(select(Usuario)) if hasattr(sessao, 'exec') else sessao.query(Usuario)
    usuarios = [r[0] if not isinstance(r, Usuario) else r for r in resultado_u]

    # Livros disponíveis
    resultado_l = (
        sessao.exec(select(Livro).where(Livro.disponivel == True))
        if hasattr(sessao, 'exec')
        else sessao.query(Livro).filter_by(disponivel=True)
    )
    livros = [r[0] if not isinstance(r, Livro) else r for r in resultado_l]

    return templates.TemplateResponse(
        "emprestimo_form.html",
        {
            "request": request,
            "usuarios": usuarios,
            "livros": livros,
            "erro": None,
        },
    )

@router.post("/emprestimos/novo")
async def web_emprestimo_criar(request: Request):
    form = await request.form()
    usuario_id = int(form.get("usuario_id"))
    livro_id = int(form.get("livro_id"))
    sessao = next(obter_sessao())
    try:
        usuario = sessao.get(Usuario, usuario_id)
        livro = sessao.get(Livro, livro_id)
        if not usuario or not livro:
            raise ErroNaoEncontrado("Usuário ou livro não encontrado")

        # ✅ Regra 1: usuário com multa aberta não pode pegar
        if usuario.possui_multa_aberta:
            raise ErroDeRegraNegocio("Usuário com multa aberta")

        # ✅ Regra 2: máximo 3 empréstimos ativos
        # usando qtd_emprestimo que você já mantém nas devoluções
        if usuario.qtd_emprestimo >= 3:
            raise ErroDeRegraNegocio("Usuário já possui 3 empréstimos ativos")

        # ✅ Regra 3: livro precisa estar disponível
        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro indisponível")

        # cria emprestimo
        from datetime import date, timedelta
        emprestimo = Emprestimo(
            livro_id=livro_id,
            usuario_id=usuario_id,
            data_emprestimo=date.today(),
            data_devolucao_prevista=date.today() + timedelta(days=7),
        )
        sessao.add(emprestimo)

        # atualiza estado do livro e do usuário
        livro.disponivel = False
        usuario.qtd_emprestimo += 1
        sessao.add(livro)
        sessao.add(usuario)

        sessao.commit()
        sessao.refresh(emprestimo)
        return RedirectResponse(url="/web/emprestimos", status_code=HTTP_303_SEE_OTHER)

    except (ErroDeRegraNegocio, ErroNaoEncontrado) as e:
        # recarrega listas para o form, no mesmo formato do GET /emprestimos/novo
        if hasattr(sessao, "exec"):
            # usuarios
            resultado_u = sessao.exec(select(Usuario))
            usuarios = [r[0] if not isinstance(r, Usuario) else r for r in resultado_u]
            # livros disponíveis
            resultado_l = sessao.exec(
                select(Livro).where(Livro.disponivel == True)
            )
            livros = [r[0] if not isinstance(r, Livro) else r for r in resultado_l]
        else:
            usuarios = sessao.query(Usuario).all()
            livros = sessao.query(Livro).filter_by(disponivel=True).all()

        return templates.TemplateResponse(
            "emprestimo_form.html",
            {
                "request": request,
                "usuarios": usuarios,
                "livros": livros,
                "erro": str(e),
            },
        )

@router.post("/emprestimos/{emprestimo_id}/devolver")
def web_emprestimo_devolver(request: Request, emprestimo_id: int):
    sessao = next(obter_sessao())
    emprestimo = sessao.get(Emprestimo, emprestimo_id)
    if not emprestimo:
        return templates.TemplateResponse(
            "404.html",
            {"request": request, "mensagem": "Empréstimo não encontrado"},
            status_code=404,
        )

    if emprestimo.data_devolucao_real:
        # já devolvido
        emprestimos = (
            sessao.exec(select(Emprestimo)).all()
            if hasattr(sessao, "exec")
            else sessao.query(Emprestimo).all()
        )
        return templates.TemplateResponse(
            "emprestimos_list.html",
            {
                "request": request,
                "emprestimos": emprestimos,
                "erro": "Empréstimo já devolvido",
            },
        )

    # 1) define data de devolução real (hoje)
    hoje = date.today()
    emprestimo.data_devolucao_real = hoje

    # 2) calcula atraso em dias (nunca negativo)
    dias_atraso = 0
    valor_multa = 0.0

    if emprestimo.data_devolucao_prevista:
        diff = (hoje - emprestimo.data_devolucao_prevista).days
        dias_atraso = max(diff, 0)
        valor_multa = dias_atraso * 1.5  # regra de multa

    emprestimo.dias_atraso = dias_atraso
    emprestimo.valor_multa = valor_multa

    # 3) atualiza livro e usuário
    livro = sessao.get(Livro, emprestimo.livro_id)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)

    livro.disponivel = True
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    if valor_multa > 0:
        usuario.possui_multa_aberta = True

    sessao.add(livro)
    sessao.add(usuario)
    sessao.add(emprestimo)
    sessao.commit()

    return RedirectResponse(url="/web/emprestimos", status_code=HTTP_303_SEE_OTHER)




############## carregando dados de /data

def carregar_dados_json(sessao):
    """
    Carrega dados dos arquivos JSON da pasta /data para o banco.
    Funciona com SQLAlchemy e SQLModel.
    """
    from pathlib import Path
    import json
    from datetime import datetime
    from src.db.modelos import Usuario, Livro, Emprestimo
    from sqlalchemy import select

    DATA_DIR = Path(__file__).parent.parent / "data"

    # --- Usuários ---
    usuarios_file = DATA_DIR / "usuarios.json"
    if usuarios_file.exists():
        with open(usuarios_file, encoding="utf-8") as f:
            for u in json.load(f):
                if hasattr(sessao, 'exec'):  # SQLModel
                    existente = sessao.exec(select(Usuario).where(Usuario.email == u["email"])).first()
                    if isinstance(existente, tuple) or hasattr(existente, "_mapping"):
                        existente = existente[0]  # descompacta Row
                else:  # SQLAlchemy
                    existente = sessao.query(Usuario).filter_by(email=u["email"]).first()
                
                if not existente:
                    usuario = Usuario(
                        nome=u["nome"],
                        email=u["email"],
                        possui_multa_aberta=u.get("possui_multa_aberta", False),
                        qtd_emprestimo=u.get("qtd_emprestimo", 0)
                    )
                    sessao.add(usuario)
                    sessao.commit()  # commit imediato para gerar ID
                else:
                    usuario = existente
                # cria mapeamento do ID original para o ID real no banco
                u["_db_id"] = usuario.id

    # --- Livros ---
    livros_file = DATA_DIR / "livros.json"
    if livros_file.exists():
        with open(livros_file, encoding="utf-8") as f:
            for l in json.load(f):
                if hasattr(sessao, 'exec'):  # SQLModel
                    existente = sessao.exec(select(Livro).where(Livro.isbn == l["isbn"])).first()
                    if isinstance(existente, tuple) or hasattr(existente, "_mapping"):
                        existente = existente[0]
                else:  # SQLAlchemy
                    existente = sessao.query(Livro).filter_by(isbn=l["isbn"]).first()
                
                if not existente:
                    livro = Livro(
                        titulo=l["titulo"],
                        isbn=l["isbn"],
                        disponivel=l.get("disponivel", True)
                    )
                    sessao.add(livro)
                    sessao.commit()  # commit imediato para gerar ID
                else:
                    livro = existente
                # mapeia ID do JSON para o real
                l["_db_id"] = livro.id

    # --- Empréstimos ---
    emprestimos_file = DATA_DIR / "emprestimo.json"
    if emprestimos_file.exists():
        with open(emprestimos_file, encoding="utf-8") as f:
            for e in json.load(f):
                # busca usuário e livro pelo ID real
                usuario_id = e.get("usuario_id")
                livro_id = e.get("livro_id")
                
                if hasattr(sessao, 'exec'):  # SQLModel
                    usuario = sessao.exec(select(Usuario).where(Usuario.id == usuario_id)).first()
                    livro = sessao.exec(select(Livro).where(Livro.id == livro_id)).first()
                    if isinstance(usuario, tuple) or hasattr(usuario, "_mapping"):
                        usuario = usuario[0]
                    if isinstance(livro, tuple) or hasattr(livro, "_mapping"):
                        livro = livro[0]
                else:
                    usuario = sessao.query(Usuario).filter_by(id=usuario_id).first()
                    livro = sessao.query(Livro).filter_by(id=livro_id).first()
                
                if usuario and livro:
                    data_emprestimo = datetime.fromisoformat(e["data_emprestimo"]).date()
                    data_devolucao_prevista = datetime.fromisoformat(e["data_devolucao_prevista"]).date()
                    data_devolucao_real = datetime.fromisoformat(e["data_devolucao_real"]).date() \
                        if e.get("data_devolucao_real") else None

                    # verifica se já existe um empréstimo igual
                    if hasattr(sessao, 'exec'):
                        existente = sessao.exec(
                            select(Emprestimo).where(
                                Emprestimo.usuario_id == usuario.id,
                                Emprestimo.livro_id == livro.id,
                                Emprestimo.data_emprestimo == data_emprestimo
                            )
                        ).first()
                        if isinstance(existente, tuple) or hasattr(existente, "_mapping"):
                            existente = existente[0]
                    else:
                        existente = sessao.query(Emprestimo).filter_by(
                            usuario_id=usuario.id,
                            livro_id=livro.id,
                            data_emprestimo=data_emprestimo
                        ).first()

                    if not existente:
                        emprestimo = Emprestimo(
                            usuario_id=usuario.id,
                            livro_id=livro.id,
                            data_emprestimo=data_emprestimo,
                            data_devolucao_prevista=data_devolucao_prevista,
                            data_devolucao_real=data_devolucao_real,
                            dias_atraso=e.get("dias_atraso", 0),
                            valor_multa=e.get("valor_multa", 0)
                        )
                        sessao.add(emprestimo)
        sessao.commit()


@router.get("/forcar-carregar-json")
def forcar_carregar_json(request: Request):
    from src.server.web_ui import carregar_dados_json
    from src.db.conexao import obter_sessao

    sessao = next(obter_sessao())
    carregar_dados_json(sessao)
    return {"status": "✅ Dados JSON carregados no banco SQLite"}
