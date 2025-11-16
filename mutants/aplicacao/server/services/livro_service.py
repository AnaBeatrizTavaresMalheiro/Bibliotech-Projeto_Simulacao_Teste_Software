# server/services/livro_service.py
from sqlmodel import Session, select
from aplicacao.db.models import Livro
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado, ErroDeRegraNegocio
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


class LivroService:
    def xǁLivroServiceǁ__init____mutmut_orig(self, session: Session):
        self.session = session
    def xǁLivroServiceǁ__init____mutmut_1(self, session: Session):
        self.session = None
    
    xǁLivroServiceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLivroServiceǁ__init____mutmut_1': xǁLivroServiceǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLivroServiceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁLivroServiceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁLivroServiceǁ__init____mutmut_orig)
    xǁLivroServiceǁ__init____mutmut_orig.__name__ = 'xǁLivroServiceǁ__init__'

    def xǁLivroServiceǁlistar__mutmut_orig(self):
        return self.session.exec(select(Livro)).all()

    def xǁLivroServiceǁlistar__mutmut_1(self):
        return self.session.exec(None).all()

    def xǁLivroServiceǁlistar__mutmut_2(self):
        return self.session.exec(select(None)).all()
    
    xǁLivroServiceǁlistar__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLivroServiceǁlistar__mutmut_1': xǁLivroServiceǁlistar__mutmut_1, 
        'xǁLivroServiceǁlistar__mutmut_2': xǁLivroServiceǁlistar__mutmut_2
    }
    
    def listar(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLivroServiceǁlistar__mutmut_orig"), object.__getattribute__(self, "xǁLivroServiceǁlistar__mutmut_mutants"), args, kwargs, self)
        return result 
    
    listar.__signature__ = _mutmut_signature(xǁLivroServiceǁlistar__mutmut_orig)
    xǁLivroServiceǁlistar__mutmut_orig.__name__ = 'xǁLivroServiceǁlistar'

    def xǁLivroServiceǁobter__mutmut_orig(self, livro_id: int):
        livro = self.session.get(Livro, livro_id)
        if not livro:
            raise ErroNaoEncontrado(f"Livro {livro_id} não encontrado")
        return livro

    def xǁLivroServiceǁobter__mutmut_1(self, livro_id: int):
        livro = None
        if not livro:
            raise ErroNaoEncontrado(f"Livro {livro_id} não encontrado")
        return livro

    def xǁLivroServiceǁobter__mutmut_2(self, livro_id: int):
        livro = self.session.get(None, livro_id)
        if not livro:
            raise ErroNaoEncontrado(f"Livro {livro_id} não encontrado")
        return livro

    def xǁLivroServiceǁobter__mutmut_3(self, livro_id: int):
        livro = self.session.get(Livro, None)
        if not livro:
            raise ErroNaoEncontrado(f"Livro {livro_id} não encontrado")
        return livro

    def xǁLivroServiceǁobter__mutmut_4(self, livro_id: int):
        livro = self.session.get(livro_id)
        if not livro:
            raise ErroNaoEncontrado(f"Livro {livro_id} não encontrado")
        return livro

    def xǁLivroServiceǁobter__mutmut_5(self, livro_id: int):
        livro = self.session.get(Livro, )
        if not livro:
            raise ErroNaoEncontrado(f"Livro {livro_id} não encontrado")
        return livro

    def xǁLivroServiceǁobter__mutmut_6(self, livro_id: int):
        livro = self.session.get(Livro, livro_id)
        if livro:
            raise ErroNaoEncontrado(f"Livro {livro_id} não encontrado")
        return livro

    def xǁLivroServiceǁobter__mutmut_7(self, livro_id: int):
        livro = self.session.get(Livro, livro_id)
        if not livro:
            raise ErroNaoEncontrado(None)
        return livro
    
    xǁLivroServiceǁobter__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLivroServiceǁobter__mutmut_1': xǁLivroServiceǁobter__mutmut_1, 
        'xǁLivroServiceǁobter__mutmut_2': xǁLivroServiceǁobter__mutmut_2, 
        'xǁLivroServiceǁobter__mutmut_3': xǁLivroServiceǁobter__mutmut_3, 
        'xǁLivroServiceǁobter__mutmut_4': xǁLivroServiceǁobter__mutmut_4, 
        'xǁLivroServiceǁobter__mutmut_5': xǁLivroServiceǁobter__mutmut_5, 
        'xǁLivroServiceǁobter__mutmut_6': xǁLivroServiceǁobter__mutmut_6, 
        'xǁLivroServiceǁobter__mutmut_7': xǁLivroServiceǁobter__mutmut_7
    }
    
    def obter(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLivroServiceǁobter__mutmut_orig"), object.__getattribute__(self, "xǁLivroServiceǁobter__mutmut_mutants"), args, kwargs, self)
        return result 
    
    obter.__signature__ = _mutmut_signature(xǁLivroServiceǁobter__mutmut_orig)
    xǁLivroServiceǁobter__mutmut_orig.__name__ = 'xǁLivroServiceǁobter'

    def xǁLivroServiceǁcriar__mutmut_orig(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_1(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = None

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_2(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            None
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_3(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(None)
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_4(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(None).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_5(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn != dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_6(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["XXisbnXX"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_7(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["ISBN"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_8(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio(None)

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_9(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("XXISBN já existe na baseXX")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_10(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("isbn já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_11(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN JÁ EXISTE NA BASE")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_12(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = None
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_13(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(None)
        self.session.commit()
        self.session.refresh(livro)
        return livro

    def xǁLivroServiceǁcriar__mutmut_14(self, dados: dict):
        # Regra: ISBN único
        isbn_existente = self.session.exec(
            select(Livro).where(Livro.isbn == dados["isbn"])
        ).first()

        if isbn_existente:
            raise ErroDeRegraNegocio("ISBN já existe na base")

        livro = Livro(**dados)
        self.session.add(livro)
        self.session.commit()
        self.session.refresh(None)
        return livro
    
    xǁLivroServiceǁcriar__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLivroServiceǁcriar__mutmut_1': xǁLivroServiceǁcriar__mutmut_1, 
        'xǁLivroServiceǁcriar__mutmut_2': xǁLivroServiceǁcriar__mutmut_2, 
        'xǁLivroServiceǁcriar__mutmut_3': xǁLivroServiceǁcriar__mutmut_3, 
        'xǁLivroServiceǁcriar__mutmut_4': xǁLivroServiceǁcriar__mutmut_4, 
        'xǁLivroServiceǁcriar__mutmut_5': xǁLivroServiceǁcriar__mutmut_5, 
        'xǁLivroServiceǁcriar__mutmut_6': xǁLivroServiceǁcriar__mutmut_6, 
        'xǁLivroServiceǁcriar__mutmut_7': xǁLivroServiceǁcriar__mutmut_7, 
        'xǁLivroServiceǁcriar__mutmut_8': xǁLivroServiceǁcriar__mutmut_8, 
        'xǁLivroServiceǁcriar__mutmut_9': xǁLivroServiceǁcriar__mutmut_9, 
        'xǁLivroServiceǁcriar__mutmut_10': xǁLivroServiceǁcriar__mutmut_10, 
        'xǁLivroServiceǁcriar__mutmut_11': xǁLivroServiceǁcriar__mutmut_11, 
        'xǁLivroServiceǁcriar__mutmut_12': xǁLivroServiceǁcriar__mutmut_12, 
        'xǁLivroServiceǁcriar__mutmut_13': xǁLivroServiceǁcriar__mutmut_13, 
        'xǁLivroServiceǁcriar__mutmut_14': xǁLivroServiceǁcriar__mutmut_14
    }
    
    def criar(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLivroServiceǁcriar__mutmut_orig"), object.__getattribute__(self, "xǁLivroServiceǁcriar__mutmut_mutants"), args, kwargs, self)
        return result 
    
    criar.__signature__ = _mutmut_signature(xǁLivroServiceǁcriar__mutmut_orig)
    xǁLivroServiceǁcriar__mutmut_orig.__name__ = 'xǁLivroServiceǁcriar'
