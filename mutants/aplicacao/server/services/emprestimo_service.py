# server/services/emprestimo_service.py
from sqlmodel import Session, select
from datetime import date

from aplicacao.db.models import Emprestimo, Livro, Usuario
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado, ErroDeRegraNegocio
from aplicacao.configuracoes.config import config
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


class EmprestimoService:
    def xǁEmprestimoServiceǁ__init____mutmut_orig(self, session: Session):
        self.session = session
    def xǁEmprestimoServiceǁ__init____mutmut_1(self, session: Session):
        self.session = None
    
    xǁEmprestimoServiceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEmprestimoServiceǁ__init____mutmut_1': xǁEmprestimoServiceǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEmprestimoServiceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁEmprestimoServiceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁEmprestimoServiceǁ__init____mutmut_orig)
    xǁEmprestimoServiceǁ__init____mutmut_orig.__name__ = 'xǁEmprestimoServiceǁ__init__'

    def xǁEmprestimoServiceǁcriar__mutmut_orig(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_1(self, dados: dict):
        usuario = None
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_2(self, dados: dict):
        usuario = self.session.get(None, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_3(self, dados: dict):
        usuario = self.session.get(Usuario, None)
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_4(self, dados: dict):
        usuario = self.session.get(dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_5(self, dados: dict):
        usuario = self.session.get(Usuario, )
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_6(self, dados: dict):
        usuario = self.session.get(Usuario, dados["XXusuario_idXX"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_7(self, dados: dict):
        usuario = self.session.get(Usuario, dados["USUARIO_ID"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_8(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = None

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_9(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(None, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_10(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, None)

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_11(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_12(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, )

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_13(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["XXlivro_idXX"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_14(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["LIVRO_ID"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_15(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_16(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado(None)

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_17(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("XXUsuário não encontradoXX")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_18(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_19(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("USUÁRIO NÃO ENCONTRADO")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_20(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_21(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado(None)

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_22(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("XXLivro não encontradoXX")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_23(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_24(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("LIVRO NÃO ENCONTRADO")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_25(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_26(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio(None)

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_27(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("XXLivro já está emprestadoXX")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_28(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_29(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("LIVRO JÁ ESTÁ EMPRESTADO")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_30(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo > config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_31(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio(None)

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_32(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("XXUsuário atingiu o limite de empréstimosXX")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_33(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_34(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("USUÁRIO ATINGIU O LIMITE DE EMPRÉSTIMOS")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_35(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = None
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_36(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = None
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_37(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = True
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_38(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo = 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_39(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo -= 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_40(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 2

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_41(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(None)
        self.session.commit()
        self.session.refresh(emprestimo)

        return emprestimo

    def xǁEmprestimoServiceǁcriar__mutmut_42(self, dados: dict):
        usuario = self.session.get(Usuario, dados["usuario_id"])
        livro = self.session.get(Livro, dados["livro_id"])

        if not usuario:
            raise ErroNaoEncontrado("Usuário não encontrado")

        if not livro:
            raise ErroNaoEncontrado("Livro não encontrado")

        if not livro.disponivel:
            raise ErroDeRegraNegocio("Livro já está emprestado")

        if usuario.qtd_emprestimo >= config.max_emprestimos_ativos:
            raise ErroDeRegraNegocio("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(**dados)
        livro.disponivel = False
        usuario.qtd_emprestimo += 1

        self.session.add(emprestimo)
        self.session.commit()
        self.session.refresh(None)

        return emprestimo
    
    xǁEmprestimoServiceǁcriar__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEmprestimoServiceǁcriar__mutmut_1': xǁEmprestimoServiceǁcriar__mutmut_1, 
        'xǁEmprestimoServiceǁcriar__mutmut_2': xǁEmprestimoServiceǁcriar__mutmut_2, 
        'xǁEmprestimoServiceǁcriar__mutmut_3': xǁEmprestimoServiceǁcriar__mutmut_3, 
        'xǁEmprestimoServiceǁcriar__mutmut_4': xǁEmprestimoServiceǁcriar__mutmut_4, 
        'xǁEmprestimoServiceǁcriar__mutmut_5': xǁEmprestimoServiceǁcriar__mutmut_5, 
        'xǁEmprestimoServiceǁcriar__mutmut_6': xǁEmprestimoServiceǁcriar__mutmut_6, 
        'xǁEmprestimoServiceǁcriar__mutmut_7': xǁEmprestimoServiceǁcriar__mutmut_7, 
        'xǁEmprestimoServiceǁcriar__mutmut_8': xǁEmprestimoServiceǁcriar__mutmut_8, 
        'xǁEmprestimoServiceǁcriar__mutmut_9': xǁEmprestimoServiceǁcriar__mutmut_9, 
        'xǁEmprestimoServiceǁcriar__mutmut_10': xǁEmprestimoServiceǁcriar__mutmut_10, 
        'xǁEmprestimoServiceǁcriar__mutmut_11': xǁEmprestimoServiceǁcriar__mutmut_11, 
        'xǁEmprestimoServiceǁcriar__mutmut_12': xǁEmprestimoServiceǁcriar__mutmut_12, 
        'xǁEmprestimoServiceǁcriar__mutmut_13': xǁEmprestimoServiceǁcriar__mutmut_13, 
        'xǁEmprestimoServiceǁcriar__mutmut_14': xǁEmprestimoServiceǁcriar__mutmut_14, 
        'xǁEmprestimoServiceǁcriar__mutmut_15': xǁEmprestimoServiceǁcriar__mutmut_15, 
        'xǁEmprestimoServiceǁcriar__mutmut_16': xǁEmprestimoServiceǁcriar__mutmut_16, 
        'xǁEmprestimoServiceǁcriar__mutmut_17': xǁEmprestimoServiceǁcriar__mutmut_17, 
        'xǁEmprestimoServiceǁcriar__mutmut_18': xǁEmprestimoServiceǁcriar__mutmut_18, 
        'xǁEmprestimoServiceǁcriar__mutmut_19': xǁEmprestimoServiceǁcriar__mutmut_19, 
        'xǁEmprestimoServiceǁcriar__mutmut_20': xǁEmprestimoServiceǁcriar__mutmut_20, 
        'xǁEmprestimoServiceǁcriar__mutmut_21': xǁEmprestimoServiceǁcriar__mutmut_21, 
        'xǁEmprestimoServiceǁcriar__mutmut_22': xǁEmprestimoServiceǁcriar__mutmut_22, 
        'xǁEmprestimoServiceǁcriar__mutmut_23': xǁEmprestimoServiceǁcriar__mutmut_23, 
        'xǁEmprestimoServiceǁcriar__mutmut_24': xǁEmprestimoServiceǁcriar__mutmut_24, 
        'xǁEmprestimoServiceǁcriar__mutmut_25': xǁEmprestimoServiceǁcriar__mutmut_25, 
        'xǁEmprestimoServiceǁcriar__mutmut_26': xǁEmprestimoServiceǁcriar__mutmut_26, 
        'xǁEmprestimoServiceǁcriar__mutmut_27': xǁEmprestimoServiceǁcriar__mutmut_27, 
        'xǁEmprestimoServiceǁcriar__mutmut_28': xǁEmprestimoServiceǁcriar__mutmut_28, 
        'xǁEmprestimoServiceǁcriar__mutmut_29': xǁEmprestimoServiceǁcriar__mutmut_29, 
        'xǁEmprestimoServiceǁcriar__mutmut_30': xǁEmprestimoServiceǁcriar__mutmut_30, 
        'xǁEmprestimoServiceǁcriar__mutmut_31': xǁEmprestimoServiceǁcriar__mutmut_31, 
        'xǁEmprestimoServiceǁcriar__mutmut_32': xǁEmprestimoServiceǁcriar__mutmut_32, 
        'xǁEmprestimoServiceǁcriar__mutmut_33': xǁEmprestimoServiceǁcriar__mutmut_33, 
        'xǁEmprestimoServiceǁcriar__mutmut_34': xǁEmprestimoServiceǁcriar__mutmut_34, 
        'xǁEmprestimoServiceǁcriar__mutmut_35': xǁEmprestimoServiceǁcriar__mutmut_35, 
        'xǁEmprestimoServiceǁcriar__mutmut_36': xǁEmprestimoServiceǁcriar__mutmut_36, 
        'xǁEmprestimoServiceǁcriar__mutmut_37': xǁEmprestimoServiceǁcriar__mutmut_37, 
        'xǁEmprestimoServiceǁcriar__mutmut_38': xǁEmprestimoServiceǁcriar__mutmut_38, 
        'xǁEmprestimoServiceǁcriar__mutmut_39': xǁEmprestimoServiceǁcriar__mutmut_39, 
        'xǁEmprestimoServiceǁcriar__mutmut_40': xǁEmprestimoServiceǁcriar__mutmut_40, 
        'xǁEmprestimoServiceǁcriar__mutmut_41': xǁEmprestimoServiceǁcriar__mutmut_41, 
        'xǁEmprestimoServiceǁcriar__mutmut_42': xǁEmprestimoServiceǁcriar__mutmut_42
    }
    
    def criar(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEmprestimoServiceǁcriar__mutmut_orig"), object.__getattribute__(self, "xǁEmprestimoServiceǁcriar__mutmut_mutants"), args, kwargs, self)
        return result 
    
    criar.__signature__ = _mutmut_signature(xǁEmprestimoServiceǁcriar__mutmut_orig)
    xǁEmprestimoServiceǁcriar__mutmut_orig.__name__ = 'xǁEmprestimoServiceǁcriar'

    def xǁEmprestimoServiceǁdevolver__mutmut_orig(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_1(self, emp_id: int):
        emp = None
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_2(self, emp_id: int):
        emp = self.session.get(None, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_3(self, emp_id: int):
        emp = self.session.get(Emprestimo, None)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_4(self, emp_id: int):
        emp = self.session.get(emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_5(self, emp_id: int):
        emp = self.session.get(Emprestimo, )
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_6(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_7(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado(None)

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_8(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("XXEmpréstimo não encontradoXX")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_9(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_10(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("EMPRÉSTIMO NÃO ENCONTRADO")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_11(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio(None)

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_12(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("XXEste empréstimo já foi devolvidoXX")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_13(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_14(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("ESTE EMPRÉSTIMO JÁ FOI DEVOLVIDO")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_15(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = None
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_16(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(None, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_17(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, None)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_18(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_19(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, )
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_20(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = None

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_21(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(None, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_22(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, None)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_23(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_24(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, )

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_25(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = None
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_26(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(None)
        livro.disponivel = True
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_27(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = None
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_28(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = False
        usuario.qtd_emprestimo -= 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_29(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo = 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_30(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo += 1

        self.session.commit()
        return emp

    def xǁEmprestimoServiceǁdevolver__mutmut_31(self, emp_id: int):
        emp = self.session.get(Emprestimo, emp_id)
        if not emp:
            raise ErroNaoEncontrado("Empréstimo não encontrado")

        if emp.data_devolucao_real:
            raise ErroDeRegraNegocio("Este empréstimo já foi devolvido")

        livro = self.session.get(Livro, emp.livro_id)
        usuario = self.session.get(Usuario, emp.usuario_id)

        # Devolução
        emp.data_devolucao_real = str(date.today())
        livro.disponivel = True
        usuario.qtd_emprestimo -= 2

        self.session.commit()
        return emp
    
    xǁEmprestimoServiceǁdevolver__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEmprestimoServiceǁdevolver__mutmut_1': xǁEmprestimoServiceǁdevolver__mutmut_1, 
        'xǁEmprestimoServiceǁdevolver__mutmut_2': xǁEmprestimoServiceǁdevolver__mutmut_2, 
        'xǁEmprestimoServiceǁdevolver__mutmut_3': xǁEmprestimoServiceǁdevolver__mutmut_3, 
        'xǁEmprestimoServiceǁdevolver__mutmut_4': xǁEmprestimoServiceǁdevolver__mutmut_4, 
        'xǁEmprestimoServiceǁdevolver__mutmut_5': xǁEmprestimoServiceǁdevolver__mutmut_5, 
        'xǁEmprestimoServiceǁdevolver__mutmut_6': xǁEmprestimoServiceǁdevolver__mutmut_6, 
        'xǁEmprestimoServiceǁdevolver__mutmut_7': xǁEmprestimoServiceǁdevolver__mutmut_7, 
        'xǁEmprestimoServiceǁdevolver__mutmut_8': xǁEmprestimoServiceǁdevolver__mutmut_8, 
        'xǁEmprestimoServiceǁdevolver__mutmut_9': xǁEmprestimoServiceǁdevolver__mutmut_9, 
        'xǁEmprestimoServiceǁdevolver__mutmut_10': xǁEmprestimoServiceǁdevolver__mutmut_10, 
        'xǁEmprestimoServiceǁdevolver__mutmut_11': xǁEmprestimoServiceǁdevolver__mutmut_11, 
        'xǁEmprestimoServiceǁdevolver__mutmut_12': xǁEmprestimoServiceǁdevolver__mutmut_12, 
        'xǁEmprestimoServiceǁdevolver__mutmut_13': xǁEmprestimoServiceǁdevolver__mutmut_13, 
        'xǁEmprestimoServiceǁdevolver__mutmut_14': xǁEmprestimoServiceǁdevolver__mutmut_14, 
        'xǁEmprestimoServiceǁdevolver__mutmut_15': xǁEmprestimoServiceǁdevolver__mutmut_15, 
        'xǁEmprestimoServiceǁdevolver__mutmut_16': xǁEmprestimoServiceǁdevolver__mutmut_16, 
        'xǁEmprestimoServiceǁdevolver__mutmut_17': xǁEmprestimoServiceǁdevolver__mutmut_17, 
        'xǁEmprestimoServiceǁdevolver__mutmut_18': xǁEmprestimoServiceǁdevolver__mutmut_18, 
        'xǁEmprestimoServiceǁdevolver__mutmut_19': xǁEmprestimoServiceǁdevolver__mutmut_19, 
        'xǁEmprestimoServiceǁdevolver__mutmut_20': xǁEmprestimoServiceǁdevolver__mutmut_20, 
        'xǁEmprestimoServiceǁdevolver__mutmut_21': xǁEmprestimoServiceǁdevolver__mutmut_21, 
        'xǁEmprestimoServiceǁdevolver__mutmut_22': xǁEmprestimoServiceǁdevolver__mutmut_22, 
        'xǁEmprestimoServiceǁdevolver__mutmut_23': xǁEmprestimoServiceǁdevolver__mutmut_23, 
        'xǁEmprestimoServiceǁdevolver__mutmut_24': xǁEmprestimoServiceǁdevolver__mutmut_24, 
        'xǁEmprestimoServiceǁdevolver__mutmut_25': xǁEmprestimoServiceǁdevolver__mutmut_25, 
        'xǁEmprestimoServiceǁdevolver__mutmut_26': xǁEmprestimoServiceǁdevolver__mutmut_26, 
        'xǁEmprestimoServiceǁdevolver__mutmut_27': xǁEmprestimoServiceǁdevolver__mutmut_27, 
        'xǁEmprestimoServiceǁdevolver__mutmut_28': xǁEmprestimoServiceǁdevolver__mutmut_28, 
        'xǁEmprestimoServiceǁdevolver__mutmut_29': xǁEmprestimoServiceǁdevolver__mutmut_29, 
        'xǁEmprestimoServiceǁdevolver__mutmut_30': xǁEmprestimoServiceǁdevolver__mutmut_30, 
        'xǁEmprestimoServiceǁdevolver__mutmut_31': xǁEmprestimoServiceǁdevolver__mutmut_31
    }
    
    def devolver(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEmprestimoServiceǁdevolver__mutmut_orig"), object.__getattribute__(self, "xǁEmprestimoServiceǁdevolver__mutmut_mutants"), args, kwargs, self)
        return result 
    
    devolver.__signature__ = _mutmut_signature(xǁEmprestimoServiceǁdevolver__mutmut_orig)
    xǁEmprestimoServiceǁdevolver__mutmut_orig.__name__ = 'xǁEmprestimoServiceǁdevolver'
