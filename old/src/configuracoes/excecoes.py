from fastapi import status
from fastapi.responses import JSONResponse

# Exceção para erros de regra de negócio
class ErroDeRegraNegocio(Exception):
    def __init__(self, detalhe: str):
        self.detalhe = detalhe

# Exceção para recurso não encontrado
class ErroNaoEncontrado(Exception):
    def __init__(self, detalhe: str):
        self.detalhe = detalhe


# Handlers para transformar exceções em respostas HTTP
def tratar_regra(_, exc: ErroDeRegraNegocio):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content={"detalhe": exc.detalhe})

def tratar_nao_encontrado(_, exc: ErroNaoEncontrado):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={"detalhe": exc.detalhe})

