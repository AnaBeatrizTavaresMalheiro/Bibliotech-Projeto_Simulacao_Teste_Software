import pytest
from datetime import date, timedelta
from sqlmodel import Session, SQLModel, create_engine

from aplicacao.regras_negocio.regras_emprestimo import criar_emprestimo, processar_devolucao
from aplicacao.db.models import Usuario, Livro, Emprestimo
from aplicacao.configuracoes.exceptions import ErroDeRegraNegocio


# -------------------------
# FIXTURES
# -------------------------

@pytest.fixture
def sessao_memoria():
    engine = create_engine("sqlite:///:memory:", echo=False)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture
def usuario(sessao_memoria):
    user = Usuario(
        nome="Teste",
        email="teste@x.com",
        qtd_emprestimo=0,
        possui_multa_aberta=False
    )
    sessao_memoria.add(user)
    sessao_memoria.commit()
    sessao_memoria.refresh(user)
    return user


@pytest.fixture
def livro(sessao_memoria):
    book = Livro(
        titulo="Livro A",
        isbn="123",
        disponivel=True
    )
    sessao_memoria.add(book)
    sessao_memoria.commit()
    sessao_memoria.refresh(book)
    return book


@pytest.fixture
def emprestimo(sessao_memoria, usuario, livro):
    e = Emprestimo(
        usuario_id=usuario.id,
        livro_id=livro.id,
        data_emprestimo=date.today(),
        data_devolucao_prevista=date.today() + timedelta(days=7)
    )
    livro.disponivel = False
    sessao_memoria.add(e)
    sessao_memoria.commit()
    sessao_memoria.refresh(e)
    return e


# ============================================================
# TESTES criar_emprestimo
# ============================================================

def test_criar_emprestimo_sucesso(sessao_memoria, usuario, livro):
    hoje = date.today()
    devolucao = hoje + timedelta(days=7)

    emprestimo = criar_emprestimo(
        sessao_memoria,
        usuario.id,
        livro.id,
        hoje,
        devolucao,
    )

    assert emprestimo.id is not None
    assert emprestimo.usuario_id == usuario.id
    assert emprestimo.livro_id == livro.id
    assert sessao_memoria.get(Livro, livro.id).disponivel is False
    assert sessao_memoria.get(Usuario, usuario.id).qtd_emprestimo == 1


def test_criar_emprestimo_usuario_invalido(sessao_memoria, livro):
    with pytest.raises(Exception):
        criar_emprestimo(sessao_memoria, 999, livro.id, date.today(), date.today())


def test_criar_emprestimo_livro_indisponivel(sessao_memoria, usuario, livro):
    livro.disponivel = False
    sessao_memoria.commit()

    with pytest.raises(Exception):
        criar_emprestimo(sessao_memoria, usuario.id, livro.id, date.today(), date.today())


# ============================================================
# TESTES processar_devolucao
# ============================================================

def test_processar_devolucao_sucesso_sem_atraso(sessao_memoria, emprestimo, usuario, livro):
    hoje = emprestimo.data_emprestimo + timedelta(days=1)

    processar_devolucao(sessao_memoria, emprestimo, hoje)

    assert emprestimo.data_devolucao_real == hoje
    assert emprestimo.dias_atraso == 0
    assert emprestimo.valor_multa == 0
    assert sessao_memoria.get(Livro, livro.id).disponivel is True
    assert sessao_memoria.get(Usuario, usuario.id).qtd_emprestimo == 0


def test_processar_devolucao_com_atraso(sessao_memoria, emprestimo, usuario):
    data_devolucao = emprestimo.data_devolucao_prevista + timedelta(days=3)

    processar_devolucao(sessao_memoria, emprestimo, data_devolucao)

    assert emprestimo.dias_atraso == 3
    assert emprestimo.valor_multa == 3 * 1.5
    assert sessao_memoria.get(Usuario, usuario.id).possui_multa_aberta is True


def test_processar_devolucao_ja_devolvido(sessao_memoria, emprestimo):
    emprestimo.data_devolucao_real = date.today()
    sessao_memoria.commit()

    with pytest.raises(ErroDeRegraNegocio):
        processar_devolucao(sessao_memoria, emprestimo, date.today())


def test_processar_devolucao_data_invalida(sessao_memoria, emprestimo):
    data_invalida = emprestimo.data_emprestimo - timedelta(days=1)

    with pytest.raises(ErroDeRegraNegocio):
        processar_devolucao(sessao_memoria, emprestimo, data_invalida)
