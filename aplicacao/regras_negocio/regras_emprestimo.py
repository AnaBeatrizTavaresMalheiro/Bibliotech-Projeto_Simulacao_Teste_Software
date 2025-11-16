from datetime import date
from sqlmodel import Session

from aplicacao.db.models import Emprestimo, Usuario, Livro
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio

from aplicacao.regras_negocio.regras_usuario import validar_usuario_para_emprestimo
from aplicacao.regras_negocio.regras_livro import garantir_livro_existe, garantir_livro_disponivel


def criar_emprestimo(
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


def processar_devolucao(
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

def calcular_multa(dias_atraso: int) -> float:
    if dias_atraso <= 0:
        return 0.0

    multa_por_dia = 1.50
    return dias_atraso * multa_por_dia
