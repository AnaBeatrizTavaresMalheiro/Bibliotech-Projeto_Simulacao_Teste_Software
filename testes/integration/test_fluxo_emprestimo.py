import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


import pytest
from datetime import timedelta
from server import regras

# def test_fluxo_completo_emprestimo_devolucao(usuario_sem_multa, livro_disponivel, datas):
#     # Criação do empréstimo
    
#     emprestimo = regras.criar_emprestimo(
#     usuario_sem_multa, 
#     livro_disponivel, 
#     datas["data_emprestimo"], 
#     datas["data_devolucao_prevista"]
#     )
    
#     assert emprestimo["livro"]["disponivel"] is False

#     # Devolução atrasada
#     devolucao = regras.devolver_livro(emprestimo, datas["devolucao_atrasada"])
#     assert devolucao["usuario"]["possui_multa_aberta"] is True
#     assert devolucao["livro"]["disponivel"] is True

import pytest
from datetime import date
from server import regras
from configuracoes.excecoes import ErroDeRegraNegocio
from db.modelos import Usuario, Livro, Emprestimo

# Sessão fake para testes sem banco real
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
        # Retorna objeto previamente cadastrado
        return self._objetos.get((cls, obj_id))

    def cadastrar(self, obj):
        self._objetos[(obj.__class__, obj.id)] = obj


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


def test_fluxo_completo_emprestimo_devolucao(sessao_fake, usuario_sem_multa, livro_disponivel, datas):
    # Cadastra usuário e livro na sessão fake
    sessao_fake.cadastrar(usuario_sem_multa)
    sessao_fake.cadastrar(livro_disponivel)

    # Criação do empréstimo usando função real
    emprestimo = regras.criar_emprestimo(sessao_fake, usuario_sem_multa.id, livro_disponivel.id)

    assert emprestimo.usuario_id == usuario_sem_multa.id
    assert emprestimo.livro_id == livro_disponivel.id
    assert not livro_disponivel.disponivel
    assert usuario_sem_multa.qtd_emprestimo == 1

    # Processa devolução no prazo
    regras.processar_devolucao(sessao_fake, emprestimo, datas["data_devolucao_real_no_prazo"])
    assert emprestimo.data_devolucao_real == datas["data_devolucao_real_no_prazo"]
    assert livro_disponivel.disponivel
    assert usuario_sem_multa.qtd_emprestimo == 0
