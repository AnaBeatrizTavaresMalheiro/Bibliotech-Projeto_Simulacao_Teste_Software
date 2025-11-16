# configuracoes/exceptions.py

from fastapi import status
from fastapi.responses import JSONResponse
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


# --------------------------------------------------------------
# Base para erros personalizados
# --------------------------------------------------------------
class ErroBase(Exception):
    """Classe base para exceções da aplicação."""

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    mensagem_padrao: str = "Erro interno"

    def xǁErroBaseǁ__init____mutmut_orig(self, detalhe: str | None = None):
        super().__init__(detalhe or self.mensagem_padrao)
        self.detalhe = detalhe or self.mensagem_padrao

    def xǁErroBaseǁ__init____mutmut_1(self, detalhe: str | None = None):
        super().__init__(None)
        self.detalhe = detalhe or self.mensagem_padrao

    def xǁErroBaseǁ__init____mutmut_2(self, detalhe: str | None = None):
        super().__init__(detalhe and self.mensagem_padrao)
        self.detalhe = detalhe or self.mensagem_padrao

    def xǁErroBaseǁ__init____mutmut_3(self, detalhe: str | None = None):
        super().__init__(detalhe or self.mensagem_padrao)
        self.detalhe = None

    def xǁErroBaseǁ__init____mutmut_4(self, detalhe: str | None = None):
        super().__init__(detalhe or self.mensagem_padrao)
        self.detalhe = detalhe and self.mensagem_padrao
    
    xǁErroBaseǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁErroBaseǁ__init____mutmut_1': xǁErroBaseǁ__init____mutmut_1, 
        'xǁErroBaseǁ__init____mutmut_2': xǁErroBaseǁ__init____mutmut_2, 
        'xǁErroBaseǁ__init____mutmut_3': xǁErroBaseǁ__init____mutmut_3, 
        'xǁErroBaseǁ__init____mutmut_4': xǁErroBaseǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁErroBaseǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁErroBaseǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁErroBaseǁ__init____mutmut_orig)
    xǁErroBaseǁ__init____mutmut_orig.__name__ = 'xǁErroBaseǁ__init__'


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
def x_tratar_erro_personalizado__mutmut_orig(_, exc: ErroBase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "erro": exc.__class__.__name__,
            "detalhe": exc.detalhe,
        },
    )


# --------------------------------------------------------------
# Genérico para qualquer erro customizado
# --------------------------------------------------------------
def x_tratar_erro_personalizado__mutmut_1(_, exc: ErroBase):
    return JSONResponse(
        status_code=None,
        content={
            "erro": exc.__class__.__name__,
            "detalhe": exc.detalhe,
        },
    )


# --------------------------------------------------------------
# Genérico para qualquer erro customizado
# --------------------------------------------------------------
def x_tratar_erro_personalizado__mutmut_2(_, exc: ErroBase):
    return JSONResponse(
        status_code=exc.status_code,
        content=None,
    )


# --------------------------------------------------------------
# Genérico para qualquer erro customizado
# --------------------------------------------------------------
def x_tratar_erro_personalizado__mutmut_3(_, exc: ErroBase):
    return JSONResponse(
        content={
            "erro": exc.__class__.__name__,
            "detalhe": exc.detalhe,
        },
    )


# --------------------------------------------------------------
# Genérico para qualquer erro customizado
# --------------------------------------------------------------
def x_tratar_erro_personalizado__mutmut_4(_, exc: ErroBase):
    return JSONResponse(
        status_code=exc.status_code,
        )


# --------------------------------------------------------------
# Genérico para qualquer erro customizado
# --------------------------------------------------------------
def x_tratar_erro_personalizado__mutmut_5(_, exc: ErroBase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "XXerroXX": exc.__class__.__name__,
            "detalhe": exc.detalhe,
        },
    )


# --------------------------------------------------------------
# Genérico para qualquer erro customizado
# --------------------------------------------------------------
def x_tratar_erro_personalizado__mutmut_6(_, exc: ErroBase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "ERRO": exc.__class__.__name__,
            "detalhe": exc.detalhe,
        },
    )


# --------------------------------------------------------------
# Genérico para qualquer erro customizado
# --------------------------------------------------------------
def x_tratar_erro_personalizado__mutmut_7(_, exc: ErroBase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "erro": exc.__class__.__name__,
            "XXdetalheXX": exc.detalhe,
        },
    )


# --------------------------------------------------------------
# Genérico para qualquer erro customizado
# --------------------------------------------------------------
def x_tratar_erro_personalizado__mutmut_8(_, exc: ErroBase):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "erro": exc.__class__.__name__,
            "DETALHE": exc.detalhe,
        },
    )

x_tratar_erro_personalizado__mutmut_mutants : ClassVar[MutantDict] = {
'x_tratar_erro_personalizado__mutmut_1': x_tratar_erro_personalizado__mutmut_1, 
    'x_tratar_erro_personalizado__mutmut_2': x_tratar_erro_personalizado__mutmut_2, 
    'x_tratar_erro_personalizado__mutmut_3': x_tratar_erro_personalizado__mutmut_3, 
    'x_tratar_erro_personalizado__mutmut_4': x_tratar_erro_personalizado__mutmut_4, 
    'x_tratar_erro_personalizado__mutmut_5': x_tratar_erro_personalizado__mutmut_5, 
    'x_tratar_erro_personalizado__mutmut_6': x_tratar_erro_personalizado__mutmut_6, 
    'x_tratar_erro_personalizado__mutmut_7': x_tratar_erro_personalizado__mutmut_7, 
    'x_tratar_erro_personalizado__mutmut_8': x_tratar_erro_personalizado__mutmut_8
}

def tratar_erro_personalizado(*args, **kwargs):
    result = _mutmut_trampoline(x_tratar_erro_personalizado__mutmut_orig, x_tratar_erro_personalizado__mutmut_mutants, args, kwargs)
    return result 

tratar_erro_personalizado.__signature__ = _mutmut_signature(x_tratar_erro_personalizado__mutmut_orig)
x_tratar_erro_personalizado__mutmut_orig.__name__ = 'x_tratar_erro_personalizado'
