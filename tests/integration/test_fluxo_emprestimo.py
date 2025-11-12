import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from datetime import date, timedelta
from src.server import regras
from src.configuracoes.excecoes import ErroDeRegraNegocio
from src.db.modelos import Usuario, Livro

# ----------------------------
# Sessão fake para testes sem banco real
# ----------------------------
class SessaoFake:
    def __init__(self):
        self._objetos = {}
        self._added = []

    def add(self, obj):
        self._added.append(obj)

    def commit(self):
        pass

    def refresh(self, obj):
        pass

    def get(self, cls, obj_id):
        return self._objetos.get((cls, obj_id))

    def cadastrar(self, obj):
        self._objetos[(obj.__class__, obj.id)] = obj

# ----------------------------
# Fixtures
# ----------------------------
@pytest.fixture
def sessao_fake():
    return SessaoFake()

@pytest.fixture
def usuario_sem_multa():
    return Usuario(id=1, nome="Alice", possui_multa_aberta=False, qtd_emprestimo=0)

@pytest.fixture
def livro_disponivel():
    return Livro(id=10, titulo="Livro de Teste", disponivel=True)

@pytest.fixture
def datas():
    return {
        "data_emprestimo": date(2025, 11, 4),
        "data_devolucao_prevista": date(2025, 11, 11),
        "data_devolucao_real_no_prazo": date(2025, 11, 11),
        "data_devolucao_real_atrasada": date(2025, 11, 13)
    }

# ----------------------------
# Testes de fluxo de empréstimo e devolução
# ----------------------------
def test_fluxo_completo_emprestimo_devolucao(sessao_fake, usuario_sem_multa, livro_disponivel, datas):
    sessao_fake.cadastrar(usuario_sem_multa)
    sessao_fake.cadastrar(livro_disponivel)

    emprestimo = regras.criar_emprestimo(sessao_fake, usuario_sem_multa.id, livro_disponivel.id)
    assert emprestimo.usuario_id == usuario_sem_multa.id
    assert emprestimo.livro_id == livro_disponivel.id
    assert not livro_disponivel.disponivel
    assert usuario_sem_multa.qtd_emprestimo == 1

    regras.processar_devolucao(sessao_fake, emprestimo, datas["data_devolucao_real_no_prazo"])
    assert emprestimo.data_devolucao_real == datas["data_devolucao_real_no_prazo"]
    assert livro_disponivel.disponivel
    assert usuario_sem_multa.qtd_emprestimo == 0

def test_emprestimo_usuario_com_multa(sessao_fake, livro_disponivel):
    usuario = Usuario(id=2, nome="Bob", possui_multa_aberta=True, qtd_emprestimo=0)
    sessao_fake.cadastrar(usuario)
    sessao_fake.cadastrar(livro_disponivel)

    with pytest.raises(ErroDeRegraNegocio, match="multa pendente"):
        regras.criar_emprestimo(sessao_fake, usuario.id, livro_disponivel.id)

def test_emprestimo_livro_indisponivel(sessao_fake, usuario_sem_multa):
    livro = Livro(id=20, titulo="Livro Ocupado", disponivel=False)
    sessao_fake.cadastrar(usuario_sem_multa)
    sessao_fake.cadastrar(livro)

    with pytest.raises(ErroDeRegraNegocio, match="indisponível"):
        regras.criar_emprestimo(sessao_fake, usuario_sem_multa.id, livro.id)

def test_devolucao_atrasada(sessao_fake, usuario_sem_multa, livro_disponivel, datas):
    sessao_fake.cadastrar(usuario_sem_multa)
    sessao_fake.cadastrar(livro_disponivel)

    emprestimo = regras.criar_emprestimo(
        sessao_fake,
        usuario_sem_multa.id,
        livro_disponivel.id,
        data_emprestimo=datas["data_emprestimo"],
        data_devolucao_prevista=datas["data_devolucao_prevista"]
    )

    regras.processar_devolucao(sessao_fake, emprestimo, datas["data_devolucao_real_atrasada"])
    assert emprestimo.dias_atraso == 2
    assert emprestimo.valor_multa > 0
    assert usuario_sem_multa.qtd_emprestimo == 0
    assert livro_disponivel.disponivel

def test_devolucao_duplicada(sessao_fake, usuario_sem_multa, livro_disponivel, datas):
    sessao_fake.cadastrar(usuario_sem_multa)
    sessao_fake.cadastrar(livro_disponivel)

    emprestimo = regras.criar_emprestimo(
        sessao_fake,
        usuario_sem_multa.id,
        livro_disponivel.id,
        data_emprestimo=datas["data_emprestimo"],
        data_devolucao_prevista=datas["data_devolucao_prevista"]
    )

    regras.processar_devolucao(sessao_fake, emprestimo, datas["data_devolucao_real_no_prazo"])
    with pytest.raises(ErroDeRegraNegocio, match="já foi devolvido"):
        regras.processar_devolucao(sessao_fake, emprestimo, datas["data_devolucao_real_no_prazo"])

def test_devolucao_data_invalida(sessao_fake, usuario_sem_multa, livro_disponivel, datas):
    sessao_fake.cadastrar(usuario_sem_multa)
    sessao_fake.cadastrar(livro_disponivel)

    emprestimo = regras.criar_emprestimo(
        sessao_fake,
        usuario_sem_multa.id,
        livro_disponivel.id,
        data_emprestimo=datas["data_emprestimo"],
        data_devolucao_prevista=datas["data_devolucao_prevista"]
    )

    data_invalida = datas["data_emprestimo"] - timedelta(days=1)
    with pytest.raises(ErroDeRegraNegocio, match="Data de devolução não pode ser anterior"):
        regras.processar_devolucao(sessao_fake, emprestimo, data_invalida)
