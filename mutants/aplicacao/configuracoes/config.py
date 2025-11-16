# configuracoes/config.py
from pydantic import BaseModel
from pathlib import Path

# --------------------------------------------------------------
# Caminhos base da aplicação
# --------------------------------------------------------------
RAIZ_PROJETO = Path(__file__).resolve().parents[2]
CAMINHO_DB = RAIZ_PROJETO / "db" / "biblioteca.db" #Projeto de Testes\db\biblioteca.db
CAMINHO_DADOS = RAIZ_PROJETO / "dados" #Projeto de Testes\dados

# --------------------------------------------------------------
# URL do banco
# --------------------------------------------------------------
URL_BANCO_DADOS = f"sqlite:///{str(CAMINHO_DB)}"
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
# Modelo de Configurações
# --------------------------------------------------------------
class Configuracoes(BaseModel):
    multa_por_dia: float = 1.50
    max_emprestimos_ativos: int = 3

# Configuração global carregada
config = Configuracoes()


# --------------------------------------------------------------
# Validar se as estruturas bases existem
# --------------------------------------------------------------
def x_validar_estrutura__mutmut_orig() -> None:
    if not CAMINHO_DADOS.exists():
        raise RuntimeError(f"Pasta de dados não encontrada: {CAMINHO_DADOS}")

    if not CAMINHO_DB.parent.exists():
        raise RuntimeError(f"Pasta do banco não encontrada: {CAMINHO_DB.parent}")


# --------------------------------------------------------------
# Validar se as estruturas bases existem
# --------------------------------------------------------------
def x_validar_estrutura__mutmut_1() -> None:
    if CAMINHO_DADOS.exists():
        raise RuntimeError(f"Pasta de dados não encontrada: {CAMINHO_DADOS}")

    if not CAMINHO_DB.parent.exists():
        raise RuntimeError(f"Pasta do banco não encontrada: {CAMINHO_DB.parent}")


# --------------------------------------------------------------
# Validar se as estruturas bases existem
# --------------------------------------------------------------
def x_validar_estrutura__mutmut_2() -> None:
    if not CAMINHO_DADOS.exists():
        raise RuntimeError(None)

    if not CAMINHO_DB.parent.exists():
        raise RuntimeError(f"Pasta do banco não encontrada: {CAMINHO_DB.parent}")


# --------------------------------------------------------------
# Validar se as estruturas bases existem
# --------------------------------------------------------------
def x_validar_estrutura__mutmut_3() -> None:
    if not CAMINHO_DADOS.exists():
        raise RuntimeError(f"Pasta de dados não encontrada: {CAMINHO_DADOS}")

    if CAMINHO_DB.parent.exists():
        raise RuntimeError(f"Pasta do banco não encontrada: {CAMINHO_DB.parent}")


# --------------------------------------------------------------
# Validar se as estruturas bases existem
# --------------------------------------------------------------
def x_validar_estrutura__mutmut_4() -> None:
    if not CAMINHO_DADOS.exists():
        raise RuntimeError(f"Pasta de dados não encontrada: {CAMINHO_DADOS}")

    if not CAMINHO_DB.parent.exists():
        raise RuntimeError(None)

x_validar_estrutura__mutmut_mutants : ClassVar[MutantDict] = {
'x_validar_estrutura__mutmut_1': x_validar_estrutura__mutmut_1, 
    'x_validar_estrutura__mutmut_2': x_validar_estrutura__mutmut_2, 
    'x_validar_estrutura__mutmut_3': x_validar_estrutura__mutmut_3, 
    'x_validar_estrutura__mutmut_4': x_validar_estrutura__mutmut_4
}

def validar_estrutura(*args, **kwargs):
    result = _mutmut_trampoline(x_validar_estrutura__mutmut_orig, x_validar_estrutura__mutmut_mutants, args, kwargs)
    return result 

validar_estrutura.__signature__ = _mutmut_signature(x_validar_estrutura__mutmut_orig)
x_validar_estrutura__mutmut_orig.__name__ = 'x_validar_estrutura'

