import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sqlmodel import Session, SQLModel
from src.db.conexao import criar_engine
from src.db import conexao, modelos

def test_criar_tabelas_sqlite(tmp_path):
    db_path = tmp_path / "test.db"
    engine = conexao.criar_engine(f"sqlite:///{db_path}")
    assert engine is not None

def test_inserir_usuario_simplificado():
    usuario = modelos.Usuario(nome="Maria", email="maria@test.com")
    assert usuario.nome == "Maria"
    assert usuario.email == "maria@test.com"

def test_inserir_e_consultar_usuario_sqlmodel():
    # Cria engine em memória
    engine = criar_engine("sqlite:///:memory:")

    # Cria todas as tabelas a partir dos modelos
    SQLModel.metadata.create_all(engine)

    # Cria sessão
    with Session(engine) as session:
        # Cria usuário
        user = modelos.Usuario(nome="TesteDB", email="testedb@test.com")
        session.add(user)
        session.commit()
        session.refresh(user)

        # Recupera e testa
        retrieved = session.get(modelos.Usuario, user.id)
        assert retrieved is not None
        assert retrieved.nome == "TesteDB"
        assert retrieved.email == "testedb@test.com"

def test_inserir_e_consultar_livro_sqlmodel():
    engine = criar_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        livro = modelos.Livro(titulo="LivroDB", isbn="12345")
        session.add(livro)
        session.commit()
        session.refresh(livro)

        retrieved = session.get(modelos.Livro, livro.id)
        assert retrieved is not None
        assert retrieved.titulo == "LivroDB"
        assert retrieved.isbn == "12345"
