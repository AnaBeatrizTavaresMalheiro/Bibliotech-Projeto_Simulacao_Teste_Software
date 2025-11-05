import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from configuracoes.configuracoes import config, Configuracoes

def test_carregar_config():
    assert isinstance(config, Configuracoes)
    assert config.nome_app == "Sistema de Empréstimos da Biblioteca"
    assert config.multa_por_dia == 1.50
    assert config.max_emprestimos_ativos == 3
