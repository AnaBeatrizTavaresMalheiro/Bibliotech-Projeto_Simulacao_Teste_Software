import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.db import conexao
from sqlmodel import Session
from sqlalchemy.engine import Engine


def test_motor_existe_e_sqlite():
    """Verifica se a engine principal foi criada corretamente."""
    assert isinstance(conexao.motor, Engine)
    assert "sqlite" in str(conexao.motor.url)


def test_obter_sessao_retorna_sessao_valida():
    """Verifica se o gerador de sessão funciona e retorna uma instância Session."""
    sessao_gen = conexao.obter_sessao()
    sessao = next(sessao_gen)
    assert isinstance(sessao, Session)
    sessao.close()


def test_criar_engine_personalizada():
    """Verifica se a função criar_engine retorna uma engine SQLite funcional."""
    engine = conexao.criar_engine("sqlite:///teste_mutacao.db", echo=False)
    assert isinstance(engine, Engine)
    assert "sqlite" in str(engine.url)
