# server/regras.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from datetime import date
from typing import NoReturn

from sqlmodel import Session, select

from src.configuracoes.configuracoes import config
from src.configuracoes.excecoes import ErroDeRegraNegocio
from src.db.modelos import Livro, Usuario, Emprestimo
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


def x_garantir_usuario_pode_emprestar__mutmut_orig(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_1(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = None
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_2(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(None, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_3(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, None)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_4(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_5(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, )
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_6(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_7(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio(None)

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_8(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("XXUsuário não encontrado.XX")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_9(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_10(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("USUÁRIO NÃO ENCONTRADO.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_11(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio(None)

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_12(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("XXUsuário possui multa pendente.XX")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_13(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_14(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("USUÁRIO POSSUI MULTA PENDENTE.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_15(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = None
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_16(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(None, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_17(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, None, 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_18(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", None)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_19(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr("max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_20(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_21(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", )
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_22(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "XXmax_emprestimos_ativosXX", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_23(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "MAX_EMPRESTIMOS_ATIVOS", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_24(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 4)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_25(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo > limite:
        raise ErroDeRegraNegocio(f"Limite de empréstimos ativos atingido (máx. {limite}).")


def x_garantir_usuario_pode_emprestar__mutmut_26(sessao: Session, usuario_id: int) -> None | NoReturn:
    """
    Regras para criar novo empréstimo:
      - usuário deve existir
      - não pode ter multa aberta
      - não pode ultrapassar o limite de empréstimos ativos (usa Usuario.qtd_emprestimo)
    """
    usuario = sessao.get(Usuario, usuario_id)
    if not usuario:
        raise ErroDeRegraNegocio("Usuário não encontrado.")

    if usuario.possui_multa_aberta:
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

    limite = getattr(config, "max_emprestimos_ativos", 3)
    if usuario.qtd_emprestimo >= limite:
        raise ErroDeRegraNegocio(None)

x_garantir_usuario_pode_emprestar__mutmut_mutants : ClassVar[MutantDict] = {
'x_garantir_usuario_pode_emprestar__mutmut_1': x_garantir_usuario_pode_emprestar__mutmut_1, 
    'x_garantir_usuario_pode_emprestar__mutmut_2': x_garantir_usuario_pode_emprestar__mutmut_2, 
    'x_garantir_usuario_pode_emprestar__mutmut_3': x_garantir_usuario_pode_emprestar__mutmut_3, 
    'x_garantir_usuario_pode_emprestar__mutmut_4': x_garantir_usuario_pode_emprestar__mutmut_4, 
    'x_garantir_usuario_pode_emprestar__mutmut_5': x_garantir_usuario_pode_emprestar__mutmut_5, 
    'x_garantir_usuario_pode_emprestar__mutmut_6': x_garantir_usuario_pode_emprestar__mutmut_6, 
    'x_garantir_usuario_pode_emprestar__mutmut_7': x_garantir_usuario_pode_emprestar__mutmut_7, 
    'x_garantir_usuario_pode_emprestar__mutmut_8': x_garantir_usuario_pode_emprestar__mutmut_8, 
    'x_garantir_usuario_pode_emprestar__mutmut_9': x_garantir_usuario_pode_emprestar__mutmut_9, 
    'x_garantir_usuario_pode_emprestar__mutmut_10': x_garantir_usuario_pode_emprestar__mutmut_10, 
    'x_garantir_usuario_pode_emprestar__mutmut_11': x_garantir_usuario_pode_emprestar__mutmut_11, 
    'x_garantir_usuario_pode_emprestar__mutmut_12': x_garantir_usuario_pode_emprestar__mutmut_12, 
    'x_garantir_usuario_pode_emprestar__mutmut_13': x_garantir_usuario_pode_emprestar__mutmut_13, 
    'x_garantir_usuario_pode_emprestar__mutmut_14': x_garantir_usuario_pode_emprestar__mutmut_14, 
    'x_garantir_usuario_pode_emprestar__mutmut_15': x_garantir_usuario_pode_emprestar__mutmut_15, 
    'x_garantir_usuario_pode_emprestar__mutmut_16': x_garantir_usuario_pode_emprestar__mutmut_16, 
    'x_garantir_usuario_pode_emprestar__mutmut_17': x_garantir_usuario_pode_emprestar__mutmut_17, 
    'x_garantir_usuario_pode_emprestar__mutmut_18': x_garantir_usuario_pode_emprestar__mutmut_18, 
    'x_garantir_usuario_pode_emprestar__mutmut_19': x_garantir_usuario_pode_emprestar__mutmut_19, 
    'x_garantir_usuario_pode_emprestar__mutmut_20': x_garantir_usuario_pode_emprestar__mutmut_20, 
    'x_garantir_usuario_pode_emprestar__mutmut_21': x_garantir_usuario_pode_emprestar__mutmut_21, 
    'x_garantir_usuario_pode_emprestar__mutmut_22': x_garantir_usuario_pode_emprestar__mutmut_22, 
    'x_garantir_usuario_pode_emprestar__mutmut_23': x_garantir_usuario_pode_emprestar__mutmut_23, 
    'x_garantir_usuario_pode_emprestar__mutmut_24': x_garantir_usuario_pode_emprestar__mutmut_24, 
    'x_garantir_usuario_pode_emprestar__mutmut_25': x_garantir_usuario_pode_emprestar__mutmut_25, 
    'x_garantir_usuario_pode_emprestar__mutmut_26': x_garantir_usuario_pode_emprestar__mutmut_26
}

def garantir_usuario_pode_emprestar(*args, **kwargs):
    result = _mutmut_trampoline(x_garantir_usuario_pode_emprestar__mutmut_orig, x_garantir_usuario_pode_emprestar__mutmut_mutants, args, kwargs)
    return result 

garantir_usuario_pode_emprestar.__signature__ = _mutmut_signature(x_garantir_usuario_pode_emprestar__mutmut_orig)
x_garantir_usuario_pode_emprestar__mutmut_orig.__name__ = 'x_garantir_usuario_pode_emprestar'


def x_garantir_livro_disponivel__mutmut_orig(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_1(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = None
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_2(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(None, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_3(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, None)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_4(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_5(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, )
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_6(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_7(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio(None)
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_8(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("XXLivro não encontrado.XX")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_9(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_10(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("LIVRO NÃO ENCONTRADO.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_11(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if livro.disponivel:
        raise ErroDeRegraNegocio("Livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_12(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio(None)


def x_garantir_livro_disponivel__mutmut_13(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("XXLivro indisponível para empréstimo.XX")


def x_garantir_livro_disponivel__mutmut_14(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("livro indisponível para empréstimo.")


def x_garantir_livro_disponivel__mutmut_15(sessao: Session, livro_id: int) -> None | NoReturn:
    """
    Regras para o livro no ato do empréstimo:
      - livro deve existir
      - livro precisa estar disponível
    """
    livro = sessao.get(Livro, livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro não encontrado.")
    if not livro.disponivel:
        raise ErroDeRegraNegocio("LIVRO INDISPONÍVEL PARA EMPRÉSTIMO.")

x_garantir_livro_disponivel__mutmut_mutants : ClassVar[MutantDict] = {
'x_garantir_livro_disponivel__mutmut_1': x_garantir_livro_disponivel__mutmut_1, 
    'x_garantir_livro_disponivel__mutmut_2': x_garantir_livro_disponivel__mutmut_2, 
    'x_garantir_livro_disponivel__mutmut_3': x_garantir_livro_disponivel__mutmut_3, 
    'x_garantir_livro_disponivel__mutmut_4': x_garantir_livro_disponivel__mutmut_4, 
    'x_garantir_livro_disponivel__mutmut_5': x_garantir_livro_disponivel__mutmut_5, 
    'x_garantir_livro_disponivel__mutmut_6': x_garantir_livro_disponivel__mutmut_6, 
    'x_garantir_livro_disponivel__mutmut_7': x_garantir_livro_disponivel__mutmut_7, 
    'x_garantir_livro_disponivel__mutmut_8': x_garantir_livro_disponivel__mutmut_8, 
    'x_garantir_livro_disponivel__mutmut_9': x_garantir_livro_disponivel__mutmut_9, 
    'x_garantir_livro_disponivel__mutmut_10': x_garantir_livro_disponivel__mutmut_10, 
    'x_garantir_livro_disponivel__mutmut_11': x_garantir_livro_disponivel__mutmut_11, 
    'x_garantir_livro_disponivel__mutmut_12': x_garantir_livro_disponivel__mutmut_12, 
    'x_garantir_livro_disponivel__mutmut_13': x_garantir_livro_disponivel__mutmut_13, 
    'x_garantir_livro_disponivel__mutmut_14': x_garantir_livro_disponivel__mutmut_14, 
    'x_garantir_livro_disponivel__mutmut_15': x_garantir_livro_disponivel__mutmut_15
}

def garantir_livro_disponivel(*args, **kwargs):
    result = _mutmut_trampoline(x_garantir_livro_disponivel__mutmut_orig, x_garantir_livro_disponivel__mutmut_mutants, args, kwargs)
    return result 

garantir_livro_disponivel.__signature__ = _mutmut_signature(x_garantir_livro_disponivel__mutmut_orig)
x_garantir_livro_disponivel__mutmut_orig.__name__ = 'x_garantir_livro_disponivel'


def x_processar_devolucao__mutmut_orig(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_1(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_2(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio(None)

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_3(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("XXEste empréstimo já foi devolvido.XX")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_4(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_5(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("ESTE EMPRÉSTIMO JÁ FOI DEVOLVIDO.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_6(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real <= emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_7(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio(None)

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_8(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("XXData de devolução não pode ser anterior à data do empréstimo.XX")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_9(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_10(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("DATA DE DEVOLUÇÃO NÃO PODE SER ANTERIOR À DATA DO EMPRÉSTIMO.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_11(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = None
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_12(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real + emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_13(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso >= 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_14(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 1:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_15(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = None
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_16(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(None)
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_17(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(None, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_18(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, None, 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_19(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", None))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_20(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr("multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_21(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_22(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", ))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_23(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "XXmulta_por_diaXX", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_24(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "MULTA_POR_DIA", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_25(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 2.5))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_26(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = None
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_27(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = None

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_28(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso / multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_29(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = None
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_30(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(None, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_31(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, None)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_32(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_33(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, )
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_34(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_35(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio(None)

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_36(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("XXUsuário do empréstimo não encontrado ao processar devolução.XX")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_37(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_38(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("USUÁRIO DO EMPRÉSTIMO NÃO ENCONTRADO AO PROCESSAR DEVOLUÇÃO.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_39(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = None

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_40(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = False

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_41(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = None

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_42(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = None
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_43(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(None, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_44(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, None)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_45(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_46(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, )
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_47(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_48(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio(None)
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_49(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("XXLivro do empréstimo não encontrado ao processar devolução.XX")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_50(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_51(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("LIVRO DO EMPRÉSTIMO NÃO ENCONTRADO AO PROCESSAR DEVOLUÇÃO.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_52(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = None

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_53(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = False

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_54(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = None
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_55(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(None, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_56(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, None)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_57(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_58(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, )
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_59(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = None


def x_processar_devolucao__mutmut_60(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(None, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_61(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, None)


def x_processar_devolucao__mutmut_62(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_63(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, )


def x_processar_devolucao__mutmut_64(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(1, int(usuario.qtd_emprestimo) - 1)


def x_processar_devolucao__mutmut_65(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) + 1)


def x_processar_devolucao__mutmut_66(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(None) - 1)


def x_processar_devolucao__mutmut_67(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
    """
    Ao devolver um empréstimo:
      - impede devolução duplicada
      - calcula atraso (dias_atraso)
      - calcula multa (valor_multa = atraso * multa_por_dia)
      - marca multa aberta no usuário quando aplicável
      - grava data_devolucao_real
      - decrementa Usuario.qtd_emprestimo (nunca abaixo de zero)
    """
    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    # Sanidade: datas coerentes
    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days
    if atraso > 0:
        # Multa configurável, com fallback seguro
        multa_por_dia = float(getattr(config, "multa_por_dia", 1.50))
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        if not usuario:
            raise ErroDeRegraNegocio("Usuário do empréstimo não encontrado ao processar devolução.")

        usuario.possui_multa_aberta = True

    # Finaliza devolução
    emprestimo.data_devolucao_real = data_devolucao_real

    # Disponibiliza o livro novamente
    livro = sessao.get(Livro, emprestimo.livro_id)
    if not livro:
        raise ErroDeRegraNegocio("Livro do empréstimo não encontrado ao processar devolução.")
    livro.disponivel = True

    # Decrementa contador de empréstimos do usuário (sem ficar negativo)
    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    if usuario:
        usuario.qtd_emprestimo = max(0, int(usuario.qtd_emprestimo) - 2)

x_processar_devolucao__mutmut_mutants : ClassVar[MutantDict] = {
'x_processar_devolucao__mutmut_1': x_processar_devolucao__mutmut_1, 
    'x_processar_devolucao__mutmut_2': x_processar_devolucao__mutmut_2, 
    'x_processar_devolucao__mutmut_3': x_processar_devolucao__mutmut_3, 
    'x_processar_devolucao__mutmut_4': x_processar_devolucao__mutmut_4, 
    'x_processar_devolucao__mutmut_5': x_processar_devolucao__mutmut_5, 
    'x_processar_devolucao__mutmut_6': x_processar_devolucao__mutmut_6, 
    'x_processar_devolucao__mutmut_7': x_processar_devolucao__mutmut_7, 
    'x_processar_devolucao__mutmut_8': x_processar_devolucao__mutmut_8, 
    'x_processar_devolucao__mutmut_9': x_processar_devolucao__mutmut_9, 
    'x_processar_devolucao__mutmut_10': x_processar_devolucao__mutmut_10, 
    'x_processar_devolucao__mutmut_11': x_processar_devolucao__mutmut_11, 
    'x_processar_devolucao__mutmut_12': x_processar_devolucao__mutmut_12, 
    'x_processar_devolucao__mutmut_13': x_processar_devolucao__mutmut_13, 
    'x_processar_devolucao__mutmut_14': x_processar_devolucao__mutmut_14, 
    'x_processar_devolucao__mutmut_15': x_processar_devolucao__mutmut_15, 
    'x_processar_devolucao__mutmut_16': x_processar_devolucao__mutmut_16, 
    'x_processar_devolucao__mutmut_17': x_processar_devolucao__mutmut_17, 
    'x_processar_devolucao__mutmut_18': x_processar_devolucao__mutmut_18, 
    'x_processar_devolucao__mutmut_19': x_processar_devolucao__mutmut_19, 
    'x_processar_devolucao__mutmut_20': x_processar_devolucao__mutmut_20, 
    'x_processar_devolucao__mutmut_21': x_processar_devolucao__mutmut_21, 
    'x_processar_devolucao__mutmut_22': x_processar_devolucao__mutmut_22, 
    'x_processar_devolucao__mutmut_23': x_processar_devolucao__mutmut_23, 
    'x_processar_devolucao__mutmut_24': x_processar_devolucao__mutmut_24, 
    'x_processar_devolucao__mutmut_25': x_processar_devolucao__mutmut_25, 
    'x_processar_devolucao__mutmut_26': x_processar_devolucao__mutmut_26, 
    'x_processar_devolucao__mutmut_27': x_processar_devolucao__mutmut_27, 
    'x_processar_devolucao__mutmut_28': x_processar_devolucao__mutmut_28, 
    'x_processar_devolucao__mutmut_29': x_processar_devolucao__mutmut_29, 
    'x_processar_devolucao__mutmut_30': x_processar_devolucao__mutmut_30, 
    'x_processar_devolucao__mutmut_31': x_processar_devolucao__mutmut_31, 
    'x_processar_devolucao__mutmut_32': x_processar_devolucao__mutmut_32, 
    'x_processar_devolucao__mutmut_33': x_processar_devolucao__mutmut_33, 
    'x_processar_devolucao__mutmut_34': x_processar_devolucao__mutmut_34, 
    'x_processar_devolucao__mutmut_35': x_processar_devolucao__mutmut_35, 
    'x_processar_devolucao__mutmut_36': x_processar_devolucao__mutmut_36, 
    'x_processar_devolucao__mutmut_37': x_processar_devolucao__mutmut_37, 
    'x_processar_devolucao__mutmut_38': x_processar_devolucao__mutmut_38, 
    'x_processar_devolucao__mutmut_39': x_processar_devolucao__mutmut_39, 
    'x_processar_devolucao__mutmut_40': x_processar_devolucao__mutmut_40, 
    'x_processar_devolucao__mutmut_41': x_processar_devolucao__mutmut_41, 
    'x_processar_devolucao__mutmut_42': x_processar_devolucao__mutmut_42, 
    'x_processar_devolucao__mutmut_43': x_processar_devolucao__mutmut_43, 
    'x_processar_devolucao__mutmut_44': x_processar_devolucao__mutmut_44, 
    'x_processar_devolucao__mutmut_45': x_processar_devolucao__mutmut_45, 
    'x_processar_devolucao__mutmut_46': x_processar_devolucao__mutmut_46, 
    'x_processar_devolucao__mutmut_47': x_processar_devolucao__mutmut_47, 
    'x_processar_devolucao__mutmut_48': x_processar_devolucao__mutmut_48, 
    'x_processar_devolucao__mutmut_49': x_processar_devolucao__mutmut_49, 
    'x_processar_devolucao__mutmut_50': x_processar_devolucao__mutmut_50, 
    'x_processar_devolucao__mutmut_51': x_processar_devolucao__mutmut_51, 
    'x_processar_devolucao__mutmut_52': x_processar_devolucao__mutmut_52, 
    'x_processar_devolucao__mutmut_53': x_processar_devolucao__mutmut_53, 
    'x_processar_devolucao__mutmut_54': x_processar_devolucao__mutmut_54, 
    'x_processar_devolucao__mutmut_55': x_processar_devolucao__mutmut_55, 
    'x_processar_devolucao__mutmut_56': x_processar_devolucao__mutmut_56, 
    'x_processar_devolucao__mutmut_57': x_processar_devolucao__mutmut_57, 
    'x_processar_devolucao__mutmut_58': x_processar_devolucao__mutmut_58, 
    'x_processar_devolucao__mutmut_59': x_processar_devolucao__mutmut_59, 
    'x_processar_devolucao__mutmut_60': x_processar_devolucao__mutmut_60, 
    'x_processar_devolucao__mutmut_61': x_processar_devolucao__mutmut_61, 
    'x_processar_devolucao__mutmut_62': x_processar_devolucao__mutmut_62, 
    'x_processar_devolucao__mutmut_63': x_processar_devolucao__mutmut_63, 
    'x_processar_devolucao__mutmut_64': x_processar_devolucao__mutmut_64, 
    'x_processar_devolucao__mutmut_65': x_processar_devolucao__mutmut_65, 
    'x_processar_devolucao__mutmut_66': x_processar_devolucao__mutmut_66, 
    'x_processar_devolucao__mutmut_67': x_processar_devolucao__mutmut_67
}

def processar_devolucao(*args, **kwargs):
    result = _mutmut_trampoline(x_processar_devolucao__mutmut_orig, x_processar_devolucao__mutmut_mutants, args, kwargs)
    return result 

processar_devolucao.__signature__ = _mutmut_signature(x_processar_devolucao__mutmut_orig)
x_processar_devolucao__mutmut_orig.__name__ = 'x_processar_devolucao'

def x_calcular_multa__mutmut_orig(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_1(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso < 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_2(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 1:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_3(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 1.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_4(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is not None:
        multa_por_dia = getattr(config, "multa_por_dia", 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_5(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = None
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_6(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(None, "multa_por_dia", 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_7(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, None, 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_8(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", None)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_9(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr("multa_por_dia", 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_10(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_11(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", )
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_12(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "XXmulta_por_diaXX", 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_13(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "MULTA_POR_DIA", 1.50)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_14(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", 2.5)
    return dias_atraso * float(multa_por_dia)

def x_calcular_multa__mutmut_15(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", 1.50)
    return dias_atraso / float(multa_por_dia)

def x_calcular_multa__mutmut_16(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", 1.50)
    return dias_atraso * float(None)

x_calcular_multa__mutmut_mutants : ClassVar[MutantDict] = {
'x_calcular_multa__mutmut_1': x_calcular_multa__mutmut_1, 
    'x_calcular_multa__mutmut_2': x_calcular_multa__mutmut_2, 
    'x_calcular_multa__mutmut_3': x_calcular_multa__mutmut_3, 
    'x_calcular_multa__mutmut_4': x_calcular_multa__mutmut_4, 
    'x_calcular_multa__mutmut_5': x_calcular_multa__mutmut_5, 
    'x_calcular_multa__mutmut_6': x_calcular_multa__mutmut_6, 
    'x_calcular_multa__mutmut_7': x_calcular_multa__mutmut_7, 
    'x_calcular_multa__mutmut_8': x_calcular_multa__mutmut_8, 
    'x_calcular_multa__mutmut_9': x_calcular_multa__mutmut_9, 
    'x_calcular_multa__mutmut_10': x_calcular_multa__mutmut_10, 
    'x_calcular_multa__mutmut_11': x_calcular_multa__mutmut_11, 
    'x_calcular_multa__mutmut_12': x_calcular_multa__mutmut_12, 
    'x_calcular_multa__mutmut_13': x_calcular_multa__mutmut_13, 
    'x_calcular_multa__mutmut_14': x_calcular_multa__mutmut_14, 
    'x_calcular_multa__mutmut_15': x_calcular_multa__mutmut_15, 
    'x_calcular_multa__mutmut_16': x_calcular_multa__mutmut_16
}

def calcular_multa(*args, **kwargs):
    result = _mutmut_trampoline(x_calcular_multa__mutmut_orig, x_calcular_multa__mutmut_mutants, args, kwargs)
    return result 

calcular_multa.__signature__ = _mutmut_signature(x_calcular_multa__mutmut_orig)
x_calcular_multa__mutmut_orig.__name__ = 'x_calcular_multa'

def x_validar_usuario__mutmut_orig(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("possui_multa_aberta", False):
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

def x_validar_usuario__mutmut_1(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get(None, False):
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

def x_validar_usuario__mutmut_2(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("possui_multa_aberta", None):
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

def x_validar_usuario__mutmut_3(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get(False):
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

def x_validar_usuario__mutmut_4(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("possui_multa_aberta", ):
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

def x_validar_usuario__mutmut_5(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("XXpossui_multa_abertaXX", False):
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

def x_validar_usuario__mutmut_6(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("POSSUI_MULTA_ABERTA", False):
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

def x_validar_usuario__mutmut_7(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("possui_multa_aberta", True):
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")

def x_validar_usuario__mutmut_8(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("possui_multa_aberta", False):
        raise ErroDeRegraNegocio(None)

def x_validar_usuario__mutmut_9(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("possui_multa_aberta", False):
        raise ErroDeRegraNegocio("XXUsuário possui multa pendente.XX")

def x_validar_usuario__mutmut_10(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("possui_multa_aberta", False):
        raise ErroDeRegraNegocio("usuário possui multa pendente.")

def x_validar_usuario__mutmut_11(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("possui_multa_aberta", False):
        raise ErroDeRegraNegocio("USUÁRIO POSSUI MULTA PENDENTE.")

x_validar_usuario__mutmut_mutants : ClassVar[MutantDict] = {
'x_validar_usuario__mutmut_1': x_validar_usuario__mutmut_1, 
    'x_validar_usuario__mutmut_2': x_validar_usuario__mutmut_2, 
    'x_validar_usuario__mutmut_3': x_validar_usuario__mutmut_3, 
    'x_validar_usuario__mutmut_4': x_validar_usuario__mutmut_4, 
    'x_validar_usuario__mutmut_5': x_validar_usuario__mutmut_5, 
    'x_validar_usuario__mutmut_6': x_validar_usuario__mutmut_6, 
    'x_validar_usuario__mutmut_7': x_validar_usuario__mutmut_7, 
    'x_validar_usuario__mutmut_8': x_validar_usuario__mutmut_8, 
    'x_validar_usuario__mutmut_9': x_validar_usuario__mutmut_9, 
    'x_validar_usuario__mutmut_10': x_validar_usuario__mutmut_10, 
    'x_validar_usuario__mutmut_11': x_validar_usuario__mutmut_11
}

def validar_usuario(*args, **kwargs):
    result = _mutmut_trampoline(x_validar_usuario__mutmut_orig, x_validar_usuario__mutmut_mutants, args, kwargs)
    return result 

validar_usuario.__signature__ = _mutmut_signature(x_validar_usuario__mutmut_orig)
x_validar_usuario__mutmut_orig.__name__ = 'x_validar_usuario'


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_orig(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_1(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = None
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_2(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo and date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_3(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = None

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_4(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista and date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_5(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(None, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_6(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, None)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_7(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_8(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, )
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_9(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(None, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_10(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, None)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_11(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_12(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, )

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_13(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = None
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_14(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(None, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_15(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, None)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_16(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_17(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, )
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_18(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = None

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_19(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_20(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = None
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_21(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(None, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_22(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, None)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_23(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_24(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, )
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_25(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo = 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_26(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo -= 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_27(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 2

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_28(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = None

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_29(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=None,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_30(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=None,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_31(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=None,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_32(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=None
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_33(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_34(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_35(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_36(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_37(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(None)
    sessao.commit()
    sessao.refresh(emprestimo)

    return emprestimo


# def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int) -> Emprestimo:
#     """
#     Cria um novo empréstimo:
#       - valida usuário
#       - valida livro
#       - marca livro como indisponível
#       - incrementa qtd_emprestimo do usuário
#       - cria e retorna o objeto Emprestimo
#     """
#     # valida regras
#     garantir_usuario_pode_emprestar(sessao, usuario_id)
#     garantir_livro_disponivel(sessao, livro_id)

#     # marca livro como indisponível
#     livro = sessao.get(Livro, livro_id)
#     livro.disponivel = False

#     # incrementa empréstimos do usuário
#     usuario = sessao.get(Usuario, usuario_id)
#     usuario.qtd_emprestimo += 1

#     # cria empréstimo
#     emprestimo = Emprestimo(
#         usuario_id=usuario.id,
#         livro_id=livro.id,
#         data_emprestimo=date.today(),
#         data_devolucao_prevista=date.today()  # ou use alguma lógica de prazo padrão
#     )

#     sessao.add(emprestimo)
#     sessao.commit()
#     sessao.refresh(emprestimo)

#     return emprestimo


def x_criar_emprestimo__mutmut_38(sessao: Session, usuario_id: int, livro_id: int,
                     data_emprestimo: date = None,
                     data_devolucao_prevista: date = None) -> Emprestimo:
    data_emprestimo = data_emprestimo or date.today()
    data_devolucao_prevista = data_devolucao_prevista or date.today()

    # valida regras
    garantir_usuario_pode_emprestar(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(None)

    return emprestimo

x_criar_emprestimo__mutmut_mutants : ClassVar[MutantDict] = {
'x_criar_emprestimo__mutmut_1': x_criar_emprestimo__mutmut_1, 
    'x_criar_emprestimo__mutmut_2': x_criar_emprestimo__mutmut_2, 
    'x_criar_emprestimo__mutmut_3': x_criar_emprestimo__mutmut_3, 
    'x_criar_emprestimo__mutmut_4': x_criar_emprestimo__mutmut_4, 
    'x_criar_emprestimo__mutmut_5': x_criar_emprestimo__mutmut_5, 
    'x_criar_emprestimo__mutmut_6': x_criar_emprestimo__mutmut_6, 
    'x_criar_emprestimo__mutmut_7': x_criar_emprestimo__mutmut_7, 
    'x_criar_emprestimo__mutmut_8': x_criar_emprestimo__mutmut_8, 
    'x_criar_emprestimo__mutmut_9': x_criar_emprestimo__mutmut_9, 
    'x_criar_emprestimo__mutmut_10': x_criar_emprestimo__mutmut_10, 
    'x_criar_emprestimo__mutmut_11': x_criar_emprestimo__mutmut_11, 
    'x_criar_emprestimo__mutmut_12': x_criar_emprestimo__mutmut_12, 
    'x_criar_emprestimo__mutmut_13': x_criar_emprestimo__mutmut_13, 
    'x_criar_emprestimo__mutmut_14': x_criar_emprestimo__mutmut_14, 
    'x_criar_emprestimo__mutmut_15': x_criar_emprestimo__mutmut_15, 
    'x_criar_emprestimo__mutmut_16': x_criar_emprestimo__mutmut_16, 
    'x_criar_emprestimo__mutmut_17': x_criar_emprestimo__mutmut_17, 
    'x_criar_emprestimo__mutmut_18': x_criar_emprestimo__mutmut_18, 
    'x_criar_emprestimo__mutmut_19': x_criar_emprestimo__mutmut_19, 
    'x_criar_emprestimo__mutmut_20': x_criar_emprestimo__mutmut_20, 
    'x_criar_emprestimo__mutmut_21': x_criar_emprestimo__mutmut_21, 
    'x_criar_emprestimo__mutmut_22': x_criar_emprestimo__mutmut_22, 
    'x_criar_emprestimo__mutmut_23': x_criar_emprestimo__mutmut_23, 
    'x_criar_emprestimo__mutmut_24': x_criar_emprestimo__mutmut_24, 
    'x_criar_emprestimo__mutmut_25': x_criar_emprestimo__mutmut_25, 
    'x_criar_emprestimo__mutmut_26': x_criar_emprestimo__mutmut_26, 
    'x_criar_emprestimo__mutmut_27': x_criar_emprestimo__mutmut_27, 
    'x_criar_emprestimo__mutmut_28': x_criar_emprestimo__mutmut_28, 
    'x_criar_emprestimo__mutmut_29': x_criar_emprestimo__mutmut_29, 
    'x_criar_emprestimo__mutmut_30': x_criar_emprestimo__mutmut_30, 
    'x_criar_emprestimo__mutmut_31': x_criar_emprestimo__mutmut_31, 
    'x_criar_emprestimo__mutmut_32': x_criar_emprestimo__mutmut_32, 
    'x_criar_emprestimo__mutmut_33': x_criar_emprestimo__mutmut_33, 
    'x_criar_emprestimo__mutmut_34': x_criar_emprestimo__mutmut_34, 
    'x_criar_emprestimo__mutmut_35': x_criar_emprestimo__mutmut_35, 
    'x_criar_emprestimo__mutmut_36': x_criar_emprestimo__mutmut_36, 
    'x_criar_emprestimo__mutmut_37': x_criar_emprestimo__mutmut_37, 
    'x_criar_emprestimo__mutmut_38': x_criar_emprestimo__mutmut_38
}

def criar_emprestimo(*args, **kwargs):
    result = _mutmut_trampoline(x_criar_emprestimo__mutmut_orig, x_criar_emprestimo__mutmut_mutants, args, kwargs)
    return result 

criar_emprestimo.__signature__ = _mutmut_signature(x_criar_emprestimo__mutmut_orig)
x_criar_emprestimo__mutmut_orig.__name__ = 'x_criar_emprestimo'
