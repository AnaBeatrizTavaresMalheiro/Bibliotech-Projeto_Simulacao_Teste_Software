import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# import pytest
# from configuracoes.excecoes import ErroDeRegraNegocio
# from server import regras

# class SessaoFake:
#     def __init__(self, usuario):
#         self._usuario = usuario

#     def get(self, modelo, id):
#         # Ignora o modelo e id — só retorna o usuário fake
#         return self._usuario

# @pytest.mark.parametrize("qtd_emprestimo", [0, 2, 3])
# def test_limite_de_emprestimos(qtd_emprestimo):
#     usuario = type("UsuarioFake", (), {
#         "id": 1,
#         "qtd_emprestimo": qtd_emprestimo,
#         "possui_multa_aberta": False
#     })()

#     sessao = SessaoFake(usuario)

#     if qtd_emprestimo >= 3:
#         with pytest.raises(ErroDeRegraNegocio):
#             regras.garantir_usuario_pode_emprestar(sessao, usuario_id=usuario.id)
#     else:
#         # não deve lançar exceção
#         try:
#             regras.garantir_usuario_pode_emprestar(sessao, usuario_id=usuario.id)
#         except ErroDeRegraNegocio as e:
#             pytest.fail(f"ErroDeRegraNegocio não era esperado aqui: {e}")

# def test_usuario_inexistente():
#     class SessaoFakeVazia:
#         def get(self, modelo, id):
#             return None

#     sessao = SessaoFakeVazia()
#     with pytest.raises(ErroDeRegraNegocio, match="Usuário não encontrado"):
#         regras.garantir_usuario_pode_emprestar(sessao, usuario_id=999)

# testes/unit/test_regras.py
import pytest
from datetime import date, timedelta
from server import regras
from configuracoes.excecoes import ErroDeRegraNegocio

# =========================================================
# Fixtures de Usuário e Livro
# =========================================================
@pytest.fixture
def usuario_sem_multa():
    class Usuario:
        id = 1
        qtd_emprestimo = 0
        possui_multa_aberta = False
    return Usuario()

@pytest.fixture
def usuario_com_multa():
    class Usuario:
        id = 2
        qtd_emprestimo = 0
        possui_multa_aberta = True
    return Usuario()

@pytest.fixture
def usuario_com_limite():
    class Usuario:
        id = 3
        qtd_emprestimo = 3
        possui_multa_aberta = False
    return Usuario()

@pytest.fixture
def livro_disponivel():
    class Livro:
        id = 10
        disponivel = True
    return Livro()

@pytest.fixture
def livro_indisponivel():
    class Livro:
        id = 11
        disponivel = False
    return Livro()

# =========================================================
# Fixture de Sessão Fake
# =========================================================
class SessaoFake:
    def __init__(self, obj):
        self.obj = obj
    def get(self, modelo, id):
        return self.obj

# =========================================================
# Testes garantir_usuario_pode_emprestar
# =========================================================
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

# =========================================================
# Testes garantir_livro_disponivel
# =========================================================
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

# =========================================================
# Testes calcular_multa
# =========================================================
@pytest.mark.parametrize("dias,esperado", [(0, 0.0), (-5, 0.0), (3, 4.5)])
def test_calcular_multa_default(dias, esperado):
    assert regras.calcular_multa(dias) == esperado

def test_calcular_multa_personalizada():
    assert regras.calcular_multa(2, multa_por_dia=5.0) == 10.0

# =========================================================
# Fixture para Emprestimo fake
# =========================================================
@pytest.fixture
def emprestimo_fake(usuario_sem_multa, livro_disponivel):
    class Emprestimo:
        usuario_id = usuario_sem_multa.id
        livro_id = livro_disponivel.id
        data_emprestimo = date.today()
        data_devolucao_prevista = date.today() + timedelta(days=7)
        data_devolucao_real = None
        dias_atraso = 0
        valor_multa = 0.0
    return Emprestimo()

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

# =========================================================
# Testes processar_devolucao
# =========================================================
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

# =========================================================
# Testes validar_usuario
# =========================================================
def test_validar_usuario_sem_multa(usuario_sem_multa):
    usuario = {"possui_multa_aberta": False}
    regras.validar_usuario(usuario)

def test_validar_usuario_com_multa(usuario_com_multa):
    usuario = {"possui_multa_aberta": True}
    with pytest.raises(ErroDeRegraNegocio):
        regras.validar_usuario(usuario)
