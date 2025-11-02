# server/regras.py
from datetime import date
from typing import NoReturn

from sqlmodel import Session, select

from configuracoes.configuracoes import config
from configuracoes.excecoes import ErroDeRegraNegocio
from db.modelos import Livro, Usuario, Emprestimo


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
