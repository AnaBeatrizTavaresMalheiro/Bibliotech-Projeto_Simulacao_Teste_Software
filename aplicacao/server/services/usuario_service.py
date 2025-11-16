from sqlmodel import Session, select
from aplicacao.db.models import Usuario
from aplicacao.configuracoes.exceptions import ErroNaoEncontrado

class UsuarioService:
    def __init__(self, session: Session):
        self.session = session

    def listar(self):
        return self.session.exec(select(Usuario)).all()

    def criar(self, dados: dict):
        usuario = Usuario(**dados)
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario
