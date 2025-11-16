from fastapi import status
from fastapi.responses import JSONResponse


# --------------------------------------------------------------
# Base para erros personalizados
# --------------------------------------------------------------
class ErroBase(Exception):
    """Classe base para exceções da aplicação."""

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    mensagem_padrao: str = "Erro interno"

    def __init__(self, detalhe: str | None = None):
        super().__init__(detalhe or self.mensagem_padrao)
        self.detalhe = detalhe or self.mensagem_padrao


# --------------------------------------------------------------
# Exceções específicas da aplicação
# --------------------------------------------------------------
class ErroDeRegraNegocio(ErroBase):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    mensagem_padrao = "Regra de negócio violada"


class ErroNaoEncontrado(ErroBase):
    status_code = status.HTTP_404_NOT_FOUND
    mensagem_padrao = "Recurso não encontrado"


# --------------------------------------------------------------
# Genérico para qualquer erro customizado
# --------------------------------------------------------------
def tratar_erro_personalizado(_, exc: ErroBase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "erro": exc.__class__.__name__,
            "detalhe": exc.detalhe,
        },
    )
