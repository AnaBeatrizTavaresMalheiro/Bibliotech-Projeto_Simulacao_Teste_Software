# server/main.py
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

# -------------------------------------------
# Startup – executa apenas UMA VEZ
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