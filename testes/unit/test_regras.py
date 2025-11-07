import pytest
from datetime import date, timedelta
from server import regras
from configuracoes.excecoes import ErroDeRegraNegocio
from testes.fixtures.conftest_unit import (
    usuario_sem_multa,
    usuario_com_multa,
    usuario_com_limite,
    livro_disponivel,
    livro_indisponivel,
    emprestimo_fake
)

# Sessão Fake mínima para simular acesso
class SessaoFake:
    def __init__(self, obj):
        self.obj = obj
    def get(self, modelo, id):
        return self.obj

# Testes garantir_usuario_pode_emprestar
def test_usuario_sem_multa_sem_limite(usuario_sem_multa):
    sessao = SessaoFake(usuario_sem_multa)
    regras.garantir_usuario_pode_emprestar(sessao, usuario_id=usuario_sem_multa.id)

def test_usuario_com_multa(usuario_com_multa):
    sessao = SessaoFake(usuario_com_multa)
    with pytest.raises(ErroDeRegraNegocio, match="multa pendente"):
        regras.garantir_usuario_pode_emprestar(sessao, usuario_id=usuario_com_multa.id)

def test_usuario_no_limite(usuario_com_limite):
    sessao = SessaoFake(usuario_com_limite)
    with pytest.raises(ErroDeRegraNegocio, match="Limite"):
        regras.garantir_usuario_pode_emprestar(sessao, usuario_id=usuario_com_limite.id)

def test_usuario_inexistente():
    sessao = SessaoFake(None)
    with pytest.raises(ErroDeRegraNegocio, match="Usuário não encontrado"):
        regras.garantir_usuario_pode_emprestar(sessao, usuario_id=999)

# Testes garantir_livro_disponivel
def test_livro_disponivel_funciona(livro_disponivel):
    sessao = SessaoFake(livro_disponivel)
    regras.garantir_livro_disponivel(sessao, livro_id=livro_disponivel.id)

def test_livro_indisponivel_funciona(livro_indisponivel):
    sessao = SessaoFake(livro_indisponivel)
    with pytest.raises(ErroDeRegraNegocio, match="indisponível"):
        regras.garantir_livro_disponivel(sessao, livro_id=livro_indisponivel.id)

def test_livro_inexistente():
    sessao = SessaoFake(None)
    with pytest.raises(ErroDeRegraNegocio):
        regras.garantir_livro_disponivel(sessao, livro_id=999)

# Testes calcular_multa
@pytest.mark.parametrize("dias,esperado", [(0, 0.0), (-5, 0.0), (3, 4.5)])
def test_calcular_multa_default(dias, esperado):
    assert regras.calcular_multa(dias) == esperado

def test_calcular_multa_personalizada():
    assert regras.calcular_multa(2, multa_por_dia=5.0) == 10.0

# Testes processar_devolucao unitários com SessaoEmprestimoFake
class SessaoEmprestimoFake:
    def __init__(self, usuario, livro, emprestimo=None):
        self.usuario = usuario
        self.livro = livro
        self.emprestimo = emprestimo
        self.commits = 0
    def get(self, modelo, id):
        if modelo.__name__ == "Usuario":
            return self.usuario
        if modelo.__name__ == "Livro":
            return self.livro
        if modelo.__name__ == "Emprestimo":
            return self.emprestimo
    def add(self, obj): pass
    def commit(self): self.commits +=1
    def refresh(self, obj): pass

def test_devolucao_no_prazo(emprestimo_fake, usuario_sem_multa, livro_disponivel):
    sessao = SessaoEmprestimoFake(usuario_sem_multa, livro_disponivel, emprestimo_fake)
    regras.processar_devolucao(sessao, emprestimo_fake, emprestimo_fake.data_devolucao_prevista)
    assert emprestimo_fake.dias_atraso == 0
    assert emprestimo_fake.valor_multa == 0.0
    assert livro_disponivel.disponivel

def test_devolucao_atrasada(emprestimo_fake, usuario_sem_multa, livro_disponivel):
    sessao = SessaoEmprestimoFake(usuario_sem_multa, livro_disponivel, emprestimo_fake)
    data_real = emprestimo_fake.data_devolucao_prevista + timedelta(days=3)
    regras.processar_devolucao(sessao, emprestimo_fake, data_real)
    assert emprestimo_fake.dias_atraso == 3
    assert emprestimo_fake.valor_multa > 0
    assert livro_disponivel.disponivel

def test_devolucao_duplicada(emprestimo_fake, usuario_sem_multa, livro_disponivel):
    emprestimo_fake.data_devolucao_real = date.today()
    sessao = SessaoEmprestimoFake(usuario_sem_multa, livro_disponivel, emprestimo_fake)
    with pytest.raises(ErroDeRegraNegocio):
        regras.processar_devolucao(sessao, emprestimo_fake, date.today())

def test_devolucao_data_invalida(emprestimo_fake, usuario_sem_multa, livro_disponivel):
    data_invalida = emprestimo_fake.data_emprestimo - timedelta(days=1)
    sessao = SessaoEmprestimoFake(usuario_sem_multa, livro_disponivel, emprestimo_fake)
    with pytest.raises(ErroDeRegraNegocio):
        regras.processar_devolucao(sessao, emprestimo_fake, data_invalida)

# Testes validar_usuario
def test_validar_usuario_sem_multa(usuario_sem_multa):
    usuario = {"possui_multa_aberta": False}
    regras.validar_usuario(usuario)

def test_validar_usuario_com_multa(usuario_com_multa):
    usuario = {"possui_multa_aberta": True}
    with pytest.raises(ErroDeRegraNegocio):
        regras.validar_usuario(usuario)


