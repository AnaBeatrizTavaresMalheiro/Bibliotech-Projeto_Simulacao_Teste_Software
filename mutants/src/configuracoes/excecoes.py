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

# Exceção para erros de regra de negócio
class ErroDeRegraNegocio(Exception):
    def xǁErroDeRegraNegocioǁ__init____mutmut_orig(self, detalhe: str):
        self.detalhe = detalhe
    def xǁErroDeRegraNegocioǁ__init____mutmut_1(self, detalhe: str):
        self.detalhe = None
    
    xǁErroDeRegraNegocioǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁErroDeRegraNegocioǁ__init____mutmut_1': xǁErroDeRegraNegocioǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁErroDeRegraNegocioǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁErroDeRegraNegocioǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁErroDeRegraNegocioǁ__init____mutmut_orig)
    xǁErroDeRegraNegocioǁ__init____mutmut_orig.__name__ = 'xǁErroDeRegraNegocioǁ__init__'

# Exceção para recurso não encontrado
class ErroNaoEncontrado(Exception):
    def xǁErroNaoEncontradoǁ__init____mutmut_orig(self, detalhe: str):
        self.detalhe = detalhe
    def xǁErroNaoEncontradoǁ__init____mutmut_1(self, detalhe: str):
        self.detalhe = None
    
    xǁErroNaoEncontradoǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁErroNaoEncontradoǁ__init____mutmut_1': xǁErroNaoEncontradoǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁErroNaoEncontradoǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁErroNaoEncontradoǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁErroNaoEncontradoǁ__init____mutmut_orig)
    xǁErroNaoEncontradoǁ__init____mutmut_orig.__name__ = 'xǁErroNaoEncontradoǁ__init__'


# Handlers para transformar exceções em respostas HTTP
def x_tratar_regra__mutmut_orig(_, exc: ErroDeRegraNegocio):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content={"detalhe": exc.detalhe})


# Handlers para transformar exceções em respostas HTTP
def x_tratar_regra__mutmut_1(_, exc: ErroDeRegraNegocio):
    return JSONResponse(status_code=None,
                        content={"detalhe": exc.detalhe})


# Handlers para transformar exceções em respostas HTTP
def x_tratar_regra__mutmut_2(_, exc: ErroDeRegraNegocio):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=None)


# Handlers para transformar exceções em respostas HTTP
def x_tratar_regra__mutmut_3(_, exc: ErroDeRegraNegocio):
    return JSONResponse(content={"detalhe": exc.detalhe})


# Handlers para transformar exceções em respostas HTTP
def x_tratar_regra__mutmut_4(_, exc: ErroDeRegraNegocio):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        )


# Handlers para transformar exceções em respostas HTTP
def x_tratar_regra__mutmut_5(_, exc: ErroDeRegraNegocio):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content={"XXdetalheXX": exc.detalhe})


# Handlers para transformar exceções em respostas HTTP
def x_tratar_regra__mutmut_6(_, exc: ErroDeRegraNegocio):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content={"DETALHE": exc.detalhe})

x_tratar_regra__mutmut_mutants : ClassVar[MutantDict] = {
'x_tratar_regra__mutmut_1': x_tratar_regra__mutmut_1, 
    'x_tratar_regra__mutmut_2': x_tratar_regra__mutmut_2, 
    'x_tratar_regra__mutmut_3': x_tratar_regra__mutmut_3, 
    'x_tratar_regra__mutmut_4': x_tratar_regra__mutmut_4, 
    'x_tratar_regra__mutmut_5': x_tratar_regra__mutmut_5, 
    'x_tratar_regra__mutmut_6': x_tratar_regra__mutmut_6
}

def tratar_regra(*args, **kwargs):
    result = _mutmut_trampoline(x_tratar_regra__mutmut_orig, x_tratar_regra__mutmut_mutants, args, kwargs)
    return result 

tratar_regra.__signature__ = _mutmut_signature(x_tratar_regra__mutmut_orig)
x_tratar_regra__mutmut_orig.__name__ = 'x_tratar_regra'

def x_tratar_nao_encontrado__mutmut_orig(_, exc: ErroNaoEncontrado):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={"detalhe": exc.detalhe})

def x_tratar_nao_encontrado__mutmut_1(_, exc: ErroNaoEncontrado):
    return JSONResponse(status_code=None,
                        content={"detalhe": exc.detalhe})

def x_tratar_nao_encontrado__mutmut_2(_, exc: ErroNaoEncontrado):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content=None)

def x_tratar_nao_encontrado__mutmut_3(_, exc: ErroNaoEncontrado):
    return JSONResponse(content={"detalhe": exc.detalhe})

def x_tratar_nao_encontrado__mutmut_4(_, exc: ErroNaoEncontrado):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        )

def x_tratar_nao_encontrado__mutmut_5(_, exc: ErroNaoEncontrado):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={"XXdetalheXX": exc.detalhe})

def x_tratar_nao_encontrado__mutmut_6(_, exc: ErroNaoEncontrado):
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={"DETALHE": exc.detalhe})

x_tratar_nao_encontrado__mutmut_mutants : ClassVar[MutantDict] = {
'x_tratar_nao_encontrado__mutmut_1': x_tratar_nao_encontrado__mutmut_1, 
    'x_tratar_nao_encontrado__mutmut_2': x_tratar_nao_encontrado__mutmut_2, 
    'x_tratar_nao_encontrado__mutmut_3': x_tratar_nao_encontrado__mutmut_3, 
    'x_tratar_nao_encontrado__mutmut_4': x_tratar_nao_encontrado__mutmut_4, 
    'x_tratar_nao_encontrado__mutmut_5': x_tratar_nao_encontrado__mutmut_5, 
    'x_tratar_nao_encontrado__mutmut_6': x_tratar_nao_encontrado__mutmut_6
}

def tratar_nao_encontrado(*args, **kwargs):
    result = _mutmut_trampoline(x_tratar_nao_encontrado__mutmut_orig, x_tratar_nao_encontrado__mutmut_mutants, args, kwargs)
    return result 

tratar_nao_encontrado.__signature__ = _mutmut_signature(x_tratar_nao_encontrado__mutmut_orig)
x_tratar_nao_encontrado__mutmut_orig.__name__ = 'x_tratar_nao_encontrado'

