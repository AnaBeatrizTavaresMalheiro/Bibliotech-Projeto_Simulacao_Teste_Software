import pytest
from datetime import date, timedelta
from aplicacao.db.models import Usuario, Livro, Emprestimo


# -------------------------
# USUÁRIO
# -------------------------
def test_usuario_criacao_basica():
    u = Usuario(nome="Ana Beatriz", email="a@b.com")
    assert u.nome == "Ana Beatriz"
    assert u.email == "a@b.com"
    assert u.qtd_emprestimo == 0
    assert u.possui_multa_aberta is False


def test_usuario_inicial_com_multa():
    u = Usuario(nome="Ana", email="a@a.com", possui_multa_aberta=True)
    assert u.possui_multa_aberta is True


def test_usuario_qtd_emprestimo_limite():
    u = Usuario(nome="Teste", email="t@t.com", qtd_emprestimo=3)
    assert u.qtd_emprestimo == 3


def test_usuario_str_repr():
    u = Usuario(id=10, nome="Ana Beatriz", email="a@b.com")
    s = str(u)
    assert "Ana Beatriz" in s
    assert "10" in s


# -------------------------
# LIVRO
# -------------------------
def test_livro_criacao_basica():
    l = Livro(titulo="RDR2", isbn="12345")
    assert l.titulo == "RDR2"
    assert l.isbn == "12345"
    assert l.disponivel is True


def test_livro_indisponivel_padrao_false():
    l = Livro(titulo="TLOU", isbn="xxxxx", disponivel=False)
    assert l.disponivel is False


def test_livro_repr():
    l = Livro(id=1, titulo="Cyberpunk", isbn="999")
    assert "Cyberpunk" in str(l)


def test_livro_aceita_isbn_string_vazia():
    l = Livro(titulo="AAA", isbn="")
    assert l.isbn == ""


# -------------------------
# EMPRÉSTIMO
# -------------------------
def test_emprestimo_criacao_basica():
    hoje = date.today()
    e = Emprestimo(
        usuario_id=1,
        livro_id=1,
        data_emprestimo=hoje,
        data_devolucao_prevista=hoje + timedelta(days=7),
    )
    assert e.usuario_id == 1
    assert e.livro_id == 1
    assert e.data_devolucao_real is None
    assert e.dias_atraso == 0
    assert e.valor_multa == 0


def test_emprestimo_atrasado_manual():
    e = Emprestimo(
        usuario_id=2,
        livro_id=3,
        data_emprestimo=date.today(),
        data_devolucao_prevista=date.today() - timedelta(days=3),
        data_devolucao_real=None,
        dias_atraso=3,
        valor_multa=4.5,
    )
    assert e.dias_atraso == 3
    assert e.valor_multa == 4.5


def test_emprestimo_repr():
    e = Emprestimo(usuario_id=1, livro_id=2, data_emprestimo=date.today(),
                   data_devolucao_prevista=date.today())
    assert "usuario_id=1" in str(e)
