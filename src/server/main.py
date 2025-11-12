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
