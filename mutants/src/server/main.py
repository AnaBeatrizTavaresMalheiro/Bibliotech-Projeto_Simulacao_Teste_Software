# server/main.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from fastapi import FastAPI

# Configurações e exceções
from src.configuracoes.configuracoes import config
from src.configuracoes.excecoes import (
    ErroDeRegraNegocio,
    ErroNaoEncontrado,
    tratar_regra,
    tratar_nao_encontrado,
)

# Banco e rotas
from src.db.inicializar import inicializar_banco
from src.db.criar_schemas import carregar_seed_se_vazio
from src.server.rotas import app_rotas

from src.server.web_ui import carregar_dados_json

# Instância principal do FastAPI (com fallback de nome)
app = FastAPI(title=getattr(config, "nome_app", "Biblioteca API"))

# Rotas e handlers de erro
app.include_router(app_rotas)
app.add_exception_handler(ErroDeRegraNegocio, tratar_regra)
app.add_exception_handler(ErroNaoEncontrado, tratar_nao_encontrado)
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

@app.get("/")
def redirecionar_para_web():
    return RedirectResponse(url="/web")

# (Opcional) endpoint raiz amigável
@app.get("/")
def raiz():
    return {
        "nome": getattr(config, "nome_app", "Biblioteca API"),
        "docs": "/docs",
        "endpoints": ["/livros", "/usuarios", "/emprestimos"],
    }

# Startup: cria tabelas/índices e carrega seed se vazio
# @app.on_event("startup")
# def startup():
#     carregar_seed_se_vazio()
#     inicializar_banco()
    

# @app.on_event("startup")
# def startup():
#     if not os.environ.get("TESTING"):  # ⚡️ só roda se não estivermos testando
#         carregar_seed_se_vazio()
#         inicializar_banco()


from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from src.db.conexao import obter_sessao


# Monta a pasta de arquivos estáticos
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

# Configura os templates
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))


# 🔹 Inicialização do banco só se não for teste

@app.on_event("startup")
def startup():
    if not os.environ.get("TESTING"):
        carregar_seed_se_vazio()
        inicializar_banco()
        sessao = next(obter_sessao())
        carregar_dados_json(sessao)


# 🔹 Importa e inclui as rotas web
from src.server.web_ui import router as web_router
print("✅ Router WEB carregado:", web_router)
app.include_router(web_router)
print("✅ Router WEB incluído com prefixo:", web_router.prefix)

from fastapi.responses import RedirectResponse

@app.get("/")
def redirecionar_para_interface():
    """Redireciona automaticamente da raiz / para /web"""
    return RedirectResponse(url="/web")
