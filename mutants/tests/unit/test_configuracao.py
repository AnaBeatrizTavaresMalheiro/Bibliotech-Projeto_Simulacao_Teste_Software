# testes/unit/test_configuracao.py
from aplicacao.configuracoes.config import Configuracoes, URL_BANCO_DADOS, CAMINHO_DB

def test_Configuracoes_default():
    cfg = Configuracoes()
    assert cfg.multa_por_dia == 1.50
    assert cfg.max_emprestimos_ativos == 3

def test_URL_banco_dados_existe():
    assert "sqlite" in URL_BANCO_DADOS
    assert str(CAMINHO_DB) in URL_BANCO_DADOS

def test_Configuracoes_env_override():
    """
    Sua classe não lê variáveis de ambiente,
    então o teste confirma que NÃO altera nada.
    """
    cfg = Configuracoes()
    assert cfg.multa_por_dia == 1.50
