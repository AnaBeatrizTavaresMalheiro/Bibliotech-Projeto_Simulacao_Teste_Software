# server/main.py
from fastapi import FastAPI

# Configurações e exceções
from configuracoes.configuracoes import config
from configuracoes.excecoes import (
    ErroDeRegraNegocio,
    ErroNaoEncontrado,
    tratar_regra,
    tratar_nao_encontrado,
)

# Banco e rotas
from db.inicializar import inicializar_banco
from db.criar_schemas import carregar_seed_se_vazio
from server.rotas import app_rotas

# Instância principal do FastAPI (com fallback de nome)
app = FastAPI(title=getattr(config, "nome_app", "Biblioteca API"))

# Rotas e handlers de erro
app.include_router(app_rotas)
app.add_exception_handler(ErroDeRegraNegocio, tratar_regra)
app.add_exception_handler(ErroNaoEncontrado, tratar_nao_encontrado)

# (Opcional) endpoint raiz amigável
@app.get("/")
def raiz():
    return {
        "nome": getattr(config, "nome_app", "Biblioteca API"),
        "docs": "/docs",
        "endpoints": ["/livros", "/usuarios", "/emprestimos"],
    }

# Startup: cria tabelas/índices e carrega seed se vazio
@app.on_event("startup")
def startup():
    carregar_seed_se_vazio()
    inicializar_banco()
    
