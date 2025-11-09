import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from configuracoes.configuracoes import config, Configuracoes
import pytest

# =========================================================
# Teste básico de carregamento do config
# =========================================================
def test_carregar_config():
    assert isinstance(config, Configuracoes)
    assert config.nome_app == "Sistema de Empréstimos da Biblioteca"
    assert config.multa_por_dia == 1.50
    assert config.max_emprestimos_ativos == 3

# =========================================================
# Testes de tipos dos atributos
# =========================================================
def test_tipos_atributos():
    assert isinstance(config.nome_app, str)
    assert isinstance(config.multa_por_dia, float)
    assert isinstance(config.max_emprestimos_ativos, int)

# =========================================================
# Teste de instância direta e alteração de valores
# =========================================================
def test_instancia_config_personalizada():
    conf = Configuracoes()
    conf.nome_app = "Teste App"
    conf.multa_por_dia = 2.5
    conf.max_emprestimos_ativos = 5

    assert conf.nome_app == "Teste App"
    assert conf.multa_por_dia == 2.5
    assert conf.max_emprestimos_ativos == 5

def test_alteracao_de_atributos():
    conf = Configuracoes()
    conf.nome_app = "Nova App"
    conf.multa_por_dia = 3.0
    conf.max_emprestimos_ativos = 10

    assert conf.nome_app == "Nova App"
    assert conf.multa_por_dia == 3.0
    assert conf.max_emprestimos_ativos == 10

# =========================================================
# Teste de AttributeError para atributo inexistente
# =========================================================
def test_acesso_atributo_inexistente():
    conf = Configuracoes()
    with pytest.raises(AttributeError):
        _ = conf.atributo_inexistente

# =========================================================
# Teste de valores inválidos
# =========================================================
@pytest.mark.parametrize("valor_invalido", [-1, -100, 0])
def test_multa_por_dia_invalida(valor_invalido):
    conf = Configuracoes()
    conf.multa_por_dia = valor_invalido
    assert conf.multa_por_dia <= 0

# =========================================================
# Teste de valores nulos ou vazios
# =========================================================
@pytest.mark.parametrize("nome", [None, "", " "])
def test_nome_app_nulo_vazio(nome):
    conf = Configuracoes()
    conf.nome_app = nome
    assert conf.nome_app is None or isinstance(conf.nome_app, str)

# =========================================================
# Teste de múltiplas instâncias
# =========================================================
def test_multiplas_instancias():
    c1 = Configuracoes()
    c2 = Configuracoes()

    c1.nome_app = "App1"
    c2.nome_app = "App2"

    assert c1.nome_app == "App1"
    assert c2.nome_app == "App2"
    assert c1 is not c2

# =========================================================
# Teste de mutabilidade dos atributos
# =========================================================
def test_mutabilidade_atributos():
    conf = Configuracoes()
    conf.nome_app = "Teste Mutabilidade"
    conf.multa_por_dia = 10.0
    conf.max_emprestimos_ativos = 7

    conf.nome_app = "Novo Nome"
    conf.multa_por_dia = 15.0
    conf.max_emprestimos_ativos = 20

    assert conf.nome_app == "Novo Nome"
    assert conf.multa_por_dia == 15.0
    assert conf.max_emprestimos_ativos == 20

# =========================================================
# Testes de leitura e escrita rápida (sanity)
# =========================================================
@pytest.mark.parametrize("nome,multa,max_emprestimos", [
    ("App A", 1.0, 3),
    ("App B", 2.5, 5),
    ("App C", 0.0, 1),
])
def test_parametrizacao_atributos(nome, multa, max_emprestimos):
    conf = Configuracoes()
    conf.nome_app = nome
    conf.multa_por_dia = multa
    conf.max_emprestimos_ativos = max_emprestimos

    assert conf.nome_app == nome
    assert conf.multa_por_dia == multa
    assert conf.max_emprestimos_ativos == max_emprestimos
