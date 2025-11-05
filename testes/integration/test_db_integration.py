import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from db import conexao, modelos

def test_criar_tabelas_sqlite(tmp_path):
    db_path = tmp_path / "test.db"
    engine = conexao.criar_engine(f"sqlite:///{db_path}")
    assert engine is not None

def test_inserir_usuario_simplificado():
    usuario = modelos.Usuario(nome="Maria", email="maria@test.com")
    assert usuario.nome == "Maria"
