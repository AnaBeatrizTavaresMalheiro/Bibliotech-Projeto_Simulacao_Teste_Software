import pytest
from datetime import date, timedelta
from aplicacao.regras_negocio.regras_emprestimo import criar_emprestimo, processar_devolucao,calcular_multa
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio


def test_criar_emprestimo_sucesso(sessao_fake, usuario_sem_multa, livro_disponivel):
    hoje = date.today()

    sessao_fake.get.side_effect = lambda model, id: {
        usuario_sem_multa.id: usuario_sem_multa,
        livro_disponivel.id: livro_disponivel
    }[id]

    criar_emprestimo(
        sessao_fake,
        usuario_sem_multa.id,
        livro_disponivel.id,
        hoje,
        hoje + timedelta(days=7)
    )

    assert usuario_sem_multa.qtd_emprestimo == 1
    assert livro_disponivel.disponivel is False


def test_criar_emprestimo_usuario_com_3(sessao_fake, usuario_com_3, livro_disponivel):
    hoje = date.today()

    sessao_fake.get.side_effect = lambda model, id: {
        usuario_com_3.id: usuario_com_3,
        livro_disponivel.id: livro_disponivel
    }[id]

    with pytest.raises(ErroDeRegraNegocio):
        criar_emprestimo(
            sessao_fake,
            usuario_com_3.id,
            livro_disponivel.id,
            hoje,
            hoje + timedelta(days=7)
        )


def test_criar_emprestimo_livro_indisponivel(sessao_fake, usuario_sem_multa, livro_indisponivel):
    hoje = date.today()

    sessao_fake.get.side_effect = lambda model, id: {
        usuario_sem_multa.id: usuario_sem_multa,
        livro_indisponivel.id: livro_indisponivel
    }[id]

    with pytest.raises(ErroDeRegraNegocio):
        criar_emprestimo(
            sessao_fake,
            usuario_sem_multa.id,
            livro_indisponivel.id,
            hoje,
            hoje + timedelta(days=7)
        )


def test_devolver_sucesso(sessao_fake, emprestimo_ativo, livro_disponivel, usuario_sem_multa):
    hoje = date.today()

    sessao_fake.get.side_effect = lambda model, id: {
        livro_disponivel.id: livro_disponivel,
        usuario_sem_multa.id: usuario_sem_multa
    }[id]

    processar_devolucao(sessao_fake, emprestimo_ativo, hoje)

    assert emprestimo_ativo.data_devolucao_real == hoje
    assert livro_disponivel.disponivel is True
    assert usuario_sem_multa.qtd_emprestimo == 0
    assert usuario_sem_multa.possui_multa_aberta is False


def test_devolver_com_atraso(sessao_fake, emprestimo_atrasado, livro_disponivel, usuario_sem_multa):
    dias = 5
    hoje = emprestimo_atrasado.data_devolucao_prevista + timedelta(days=dias)

    sessao_fake.get.side_effect = lambda model, id: {
        livro_disponivel.id: livro_disponivel,
        usuario_sem_multa.id: usuario_sem_multa
    }[id]

    processar_devolucao(sessao_fake, emprestimo_atrasado, hoje)

    assert emprestimo_atrasado.dias_atraso == dias
    assert usuario_sem_multa.possui_multa_aberta is True


def test_devolver_sem_atraso(sessao_fake, emprestimo_ativo, livro_disponivel, usuario_sem_multa):
    hoje = emprestimo_ativo.data_devolucao_prevista

    sessao_fake.get.side_effect = lambda model, id: {
        livro_disponivel.id: livro_disponivel,
        usuario_sem_multa.id: usuario_sem_multa
    }[id]

    processar_devolucao(sessao_fake, emprestimo_ativo, hoje)

    assert emprestimo_ativo.dias_atraso == 0
    assert usuario_sem_multa.possui_multa_aberta is False


# Testes calcular_multa
@pytest.mark.parametrize(
    "dias, esperado",
    [
        (0, 0.0),   # Sem atraso
        (-5, 0.0),  # Atraso negativo → trata como zero
        (3, 4.5)    # 3 dias × 1.5 = 4.5
    ]
)
def test_calcular_multa_default(dias, esperado):
    assert calcular_multa(dias) == esperado
