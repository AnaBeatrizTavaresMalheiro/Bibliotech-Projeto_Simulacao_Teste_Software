import aplicacao.db.sessao

def _safe_get_session():
    from sqlmodel import Session
    from aplicacao.db.database import engine
    with Session(engine) as session:
        yield session

aplicacao.db.sessao.get_session = _safe_get_session
