# server/services/usuario_service.py
from sqlmodel import Session, select
from aplicacao.db.models import Usuario
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado
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

class UsuarioService:
    def xǁUsuarioServiceǁ__init____mutmut_orig(self, session: Session):
        self.session = session
    def xǁUsuarioServiceǁ__init____mutmut_1(self, session: Session):
        self.session = None
    
    xǁUsuarioServiceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsuarioServiceǁ__init____mutmut_1': xǁUsuarioServiceǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsuarioServiceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁUsuarioServiceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁUsuarioServiceǁ__init____mutmut_orig)
    xǁUsuarioServiceǁ__init____mutmut_orig.__name__ = 'xǁUsuarioServiceǁ__init__'

    def xǁUsuarioServiceǁlistar__mutmut_orig(self):
        return self.session.exec(select(Usuario)).all()

    def xǁUsuarioServiceǁlistar__mutmut_1(self):
        return self.session.exec(None).all()

    def xǁUsuarioServiceǁlistar__mutmut_2(self):
        return self.session.exec(select(None)).all()
    
    xǁUsuarioServiceǁlistar__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsuarioServiceǁlistar__mutmut_1': xǁUsuarioServiceǁlistar__mutmut_1, 
        'xǁUsuarioServiceǁlistar__mutmut_2': xǁUsuarioServiceǁlistar__mutmut_2
    }
    
    def listar(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsuarioServiceǁlistar__mutmut_orig"), object.__getattribute__(self, "xǁUsuarioServiceǁlistar__mutmut_mutants"), args, kwargs, self)
        return result 
    
    listar.__signature__ = _mutmut_signature(xǁUsuarioServiceǁlistar__mutmut_orig)
    xǁUsuarioServiceǁlistar__mutmut_orig.__name__ = 'xǁUsuarioServiceǁlistar'

    def xǁUsuarioServiceǁcriar__mutmut_orig(self, dados: dict):
        usuario = Usuario(**dados)
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def xǁUsuarioServiceǁcriar__mutmut_1(self, dados: dict):
        usuario = None
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def xǁUsuarioServiceǁcriar__mutmut_2(self, dados: dict):
        usuario = Usuario(**dados)
        self.session.add(None)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def xǁUsuarioServiceǁcriar__mutmut_3(self, dados: dict):
        usuario = Usuario(**dados)
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(None)
        return usuario
    
    xǁUsuarioServiceǁcriar__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUsuarioServiceǁcriar__mutmut_1': xǁUsuarioServiceǁcriar__mutmut_1, 
        'xǁUsuarioServiceǁcriar__mutmut_2': xǁUsuarioServiceǁcriar__mutmut_2, 
        'xǁUsuarioServiceǁcriar__mutmut_3': xǁUsuarioServiceǁcriar__mutmut_3
    }
    
    def criar(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUsuarioServiceǁcriar__mutmut_orig"), object.__getattribute__(self, "xǁUsuarioServiceǁcriar__mutmut_mutants"), args, kwargs, self)
        return result 
    
    criar.__signature__ = _mutmut_signature(xǁUsuarioServiceǁcriar__mutmut_orig)
    xǁUsuarioServiceǁcriar__mutmut_orig.__name__ = 'xǁUsuarioServiceǁcriar'
