from typing import Optional, List
from datetime import date
from sqlmodel import SQLModel, Field, Relationship
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

# ============================================================
# Modelo Livro
# Representa um registro da tabela 'livro'
# ============================================================
class Livro(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str
    isbn: str
    disponivel: bool = True


# ============================================================
# Modelo Usuario
# Representa um usuário que pode pegar livros emprestados
# ============================================================
class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    email: str
    qtd_emprestimo: int = 0
    possui_multa_aberta: bool = False

# ============================================================
# Modelo Emprestimo
# Tabela de junção entre Livro e Usuário
# Representa cada empréstimo realizado
# ============================================================
class Emprestimo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    livro_id: int = Field(foreign_key="livro.id")
    usuario_id: int = Field(foreign_key="usuario.id")

    data_emprestimo: date
    data_devolucao_prevista: date
    data_devolucao_real: Optional[date] = None

    dias_atraso: int = 0
    valor_multa: float = 0.0
