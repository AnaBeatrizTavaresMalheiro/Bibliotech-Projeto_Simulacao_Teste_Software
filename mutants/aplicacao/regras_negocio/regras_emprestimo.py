# aplicacao/regras_negocio/regras_emprestimo.py

from datetime import date
from sqlmodel import Session

from aplicacao.db.models import Emprestimo, Usuario, Livro
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio

from aplicacao.regras_negocio.regras_usuario import validar_usuario_para_emprestimo
from aplicacao.regras_negocio.regras_livro import garantir_livro_existe, garantir_livro_disponivel
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


def x_criar_emprestimo__mutmut_orig(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_1(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(None, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_2(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, None)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_3(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_4(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, )
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_5(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(None, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_6(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, None)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_7(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_8(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, )

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_9(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = None
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_10(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(None, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_11(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, None)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_12(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_13(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, )
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_14(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = None

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_15(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_16(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = None
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_17(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(None, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_18(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, None)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_19(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_20(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, )
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_21(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo = 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_22(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo -= 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_23(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 2

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_24(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
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


def x_criar_emprestimo__mutmut_25(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=None,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_26(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=None,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_27(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=None,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_28(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=None
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_29(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_30(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_31(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_32(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        )

    sessao.add(emprestimo)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_33(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
        data_emprestimo=data_emprestimo,
        data_devolucao_prevista=data_devolucao_prevista
    )

    sessao.add(None)
    sessao.commit()
    sessao.refresh(emprestimo)
    return emprestimo


def x_criar_emprestimo__mutmut_34(
    sessao: Session,
    usuario_id: int,
    livro_id: int,
    data_emprestimo: date,
    data_devolucao_prevista: date
) -> Emprestimo:

    validar_usuario_para_emprestimo(sessao, usuario_id)
    garantir_livro_disponivel(sessao, livro_id)

    livro = sessao.get(Livro, livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, usuario_id)
    usuario.qtd_emprestimo += 1

    emprestimo = Emprestimo(
        usuario_id=usuario_id,
        livro_id=livro_id,
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
    'x_criar_emprestimo__mutmut_34': x_criar_emprestimo__mutmut_34
}

def criar_emprestimo(*args, **kwargs):
    result = _mutmut_trampoline(x_criar_emprestimo__mutmut_orig, x_criar_emprestimo__mutmut_mutants, args, kwargs)
    return result 

criar_emprestimo.__signature__ = _mutmut_signature(x_criar_emprestimo__mutmut_orig)
x_criar_emprestimo__mutmut_orig.__name__ = 'x_criar_emprestimo'


def x_processar_devolucao__mutmut_orig(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_1(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_2(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio(None)

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_3(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("XXEste empréstimo já foi devolvido.XX")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_4(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_5(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("ESTE EMPRÉSTIMO JÁ FOI DEVOLVIDO.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_6(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real <= emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_7(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio(None)

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_8(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("XXData de devolução não pode ser anterior à data do empréstimo.XX")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_9(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_10(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("DATA DE DEVOLUÇÃO NÃO PODE SER ANTERIOR À DATA DO EMPRÉSTIMO.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_11(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = None

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_12(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real + emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_13(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso >= 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_14(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 1:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_15(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = None
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_16(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 2.5
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_17(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = None
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_18(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = None

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_19(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso / multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_20(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = None
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_21(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(None, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_22(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, None)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_23(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_24(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, )
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_25(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = None

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_26(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = False

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_27(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = None

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_28(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = None
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_29(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(None, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_30(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, None)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_31(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_32(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, )
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_33(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = None

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_34(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = False

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_35(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = None
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_36(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(None, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_37(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, None)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_38(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_39(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, )
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_40(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = None

    sessao.commit()


def x_processar_devolucao__mutmut_41(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(None, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_42(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, None)

    sessao.commit()


def x_processar_devolucao__mutmut_43(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_44(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, )

    sessao.commit()


def x_processar_devolucao__mutmut_45(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(1, usuario.qtd_emprestimo - 1)

    sessao.commit()


def x_processar_devolucao__mutmut_46(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo + 1)

    sessao.commit()


def x_processar_devolucao__mutmut_47(
    sessao: Session,
    emprestimo: Emprestimo,
    data_devolucao_real: date
) -> None:

    if emprestimo.data_devolucao_real is not None:
        raise ErroDeRegraNegocio("Este empréstimo já foi devolvido.")

    if data_devolucao_real < emprestimo.data_emprestimo:
        raise ErroDeRegraNegocio("Data de devolução não pode ser anterior à data do empréstimo.")

    atraso = (data_devolucao_real - emprestimo.data_devolucao_prevista).days

    if atraso > 0:
        multa_por_dia = 1.50
        emprestimo.dias_atraso = atraso
        emprestimo.valor_multa = atraso * multa_por_dia

        usuario = sessao.get(Usuario, emprestimo.usuario_id)
        usuario.possui_multa_aberta = True

    emprestimo.data_devolucao_real = data_devolucao_real

    livro = garantir_livro_existe(sessao, emprestimo.livro_id)
    livro.disponivel = True

    usuario = sessao.get(Usuario, emprestimo.usuario_id)
    usuario.qtd_emprestimo = max(0, usuario.qtd_emprestimo - 2)

    sessao.commit()

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
    'x_processar_devolucao__mutmut_47': x_processar_devolucao__mutmut_47
}

def processar_devolucao(*args, **kwargs):
    result = _mutmut_trampoline(x_processar_devolucao__mutmut_orig, x_processar_devolucao__mutmut_mutants, args, kwargs)
    return result 

processar_devolucao.__signature__ = _mutmut_signature(x_processar_devolucao__mutmut_orig)
x_processar_devolucao__mutmut_orig.__name__ = 'x_processar_devolucao'
