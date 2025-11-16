# server/regras.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from datetime import date
from typing import NoReturn

from sqlmodel import Session, select

from src.configuracoes.configuracoes import config
from src.configuracoes.excecoes import ErroDeRegraNegocio
from src.db.modelos import Livro, Usuario, Emprestimo


def garantir_usuario_pode_emprestar(sessao: Session, usuario_id: int) -> None | NoReturn:
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


def garantir_livro_disponivel(sessao: Session, livro_id: int) -> None | NoReturn:
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


def processar_devolucao(sessao: Session, emprestimo: Emprestimo, data_devolucao_real: date) -> None:
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

def calcular_multa(dias_atraso: int, multa_por_dia: float | None = None) -> float:
    """
    Calcula o valor total da multa com base nos dias de atraso e no valor por dia.
    Usa o valor configurado em config.multa_por_dia se não for informado.
    """
    if dias_atraso <= 0:
        return 0.0
    if multa_por_dia is None:
        multa_por_dia = getattr(config, "multa_por_dia", 1.50)
    return dias_atraso * float(multa_por_dia)

def validar_usuario(usuario: dict) -> None:
    """
    Valida se o usuário pode fazer empréstimos.
    Lança ErroDeRegraNegocio se houver multa aberta.
    """
    if usuario.get("possui_multa_aberta", False):
        raise ErroDeRegraNegocio("Usuário possui multa pendente.")


def criar_emprestimo(sessao: Session, usuario_id: int, livro_id: int,
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
