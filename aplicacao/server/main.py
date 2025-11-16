from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.responses import JSONResponse
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado, ErroDeRegraNegocio


from aplicacao.db.database import inicializar_banco, resetar_banco

# Routers da API REST
from aplicacao.server.routers.livros_router import router as livros_router
from aplicacao.server.routers.usuarios_router import router as usuarios_router
from aplicacao.server.routers.emprestimos_router import router as emprestimos_router

# Router da interface Web
from aplicacao.interface.router_web import router as web_router

# -------------------------------------------
# Criação da aplicação FastAPI
# -------------------------------------------
app = FastAPI(
    title="Bibliotech API",
    version="1.0.0",
)

# -------------------------------------------
# Startup 
# -------------------------------------------
@app.on_event("startup")
def startup():
    print("[STARTUP] Inicializando banco...")
    inicializar_banco()
    print("[STARTUP] Banco pronto!")


# -------------------------------------------
# Registro dos routers REST
# -------------------------------------------
app.include_router(livros_router, prefix="/livros", tags=["Livros"])
app.include_router(usuarios_router, prefix="/usuarios", tags=["Usuários"])
app.include_router(emprestimos_router, prefix="/emprestimos", tags=["Empréstimos"])

# -------------------------------------------
# Interface Web
# -------------------------------------------
app.include_router(web_router)

# -------------------------------------------
# Arquivos estáticos (CSS / imagens / JS)
# -------------------------------------------
ROOT_DIR = Path(__file__).resolve().parents[1]
app.mount("/static", StaticFiles(directory=str(ROOT_DIR / "interface" / "static")), name="static")

# -------------------------------------------
# Healthcheck
# -------------------------------------------
@app.get("/", tags=["Infra"])
def healthcheck():
    return {
        "status": "ok",
        "mensagem": "API ativa",
    }

# -------------------------------------------
# Endpoint para resetar o banco
# -------------------------------------------
@app.post("/admin/resetar-banco")
def admin_resetar_banco():
    resetar_banco()
    return {"status": "ok", "mensagem": "Banco resetado com sucesso"}


@app.exception_handler(ErroNaoEncontrado)
def handler_nao_encontrado(_, exc: ErroNaoEncontrado):
    return JSONResponse(
        status_code=404,
        content={"erro": str(exc)}
    )

@app.exception_handler(ErroDeRegraNegocio)
def handler_regra_negocio(_, exc: ErroDeRegraNegocio):
    return JSONResponse(
        status_code=400,
        content={"erro": str(exc)}
    )