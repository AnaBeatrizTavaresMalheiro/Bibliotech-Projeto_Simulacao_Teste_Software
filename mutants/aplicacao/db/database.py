# aplicacao/db/database.py
import json
from pathlib import Path
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy import text
from datetime import date

from aplicacao.db.models import Livro, Usuario, Emprestimo

# -------------------------------------------------------------
# Caminhos
# -------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "dados"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "biblioteca.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

LIVROS_JSON = DATA_DIR / "livros.json"
USUARIOS_JSON = DATA_DIR / "usuarios.json"
EMPRESTIMO_JSON = DATA_DIR / "emprestimo.json"

# -------------------------------------------------------------
# Engine
# -------------------------------------------------------------
engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result

# -------------------------------------------------------------
# Criar tabelas
# -------------------------------------------------------------
def x_criar_tabelas__mutmut_orig():
    SQLModel.metadata.create_all(engine)

# -------------------------------------------------------------
# Criar tabelas
# -------------------------------------------------------------
def x_criar_tabelas__mutmut_1():
    SQLModel.metadata.create_all(None)

x_criar_tabelas__mutmut_mutants : ClassVar[MutantDict] = {
'x_criar_tabelas__mutmut_1': x_criar_tabelas__mutmut_1
}

def criar_tabelas(*args, **kwargs):
    result = _mutmut_trampoline(x_criar_tabelas__mutmut_orig, x_criar_tabelas__mutmut_mutants, args, kwargs)
    return result 

criar_tabelas.__signature__ = _mutmut_signature(x_criar_tabelas__mutmut_orig)
x_criar_tabelas__mutmut_orig.__name__ = 'x_criar_tabelas'

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_orig():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_1():
    with Session(None) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_2():
    with Session(engine) as session:
        session.exec(None)
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_3():
    with Session(engine) as session:
        session.exec(text(None))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_4():
    with Session(engine) as session:
        session.exec(text("XXCREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);XX"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_5():
    with Session(engine) as session:
        session.exec(text("create index if not exists ix_livro_titulo on livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_6():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS IX_LIVRO_TITULO ON LIVRO (TITULO);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_7():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(None)
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_8():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text(None))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_9():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("XXCREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);XX"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_10():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("create index if not exists ix_usuario_nome on usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_11():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS IX_USUARIO_NOME ON USUARIO (NOME);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_12():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(None)
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_13():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text(None))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_14():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("XXCREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);XX"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_15():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("create index if not exists ix_emp_user on emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_16():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS IX_EMP_USER ON EMPRESTIMO (USUARIO_ID);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_17():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(None)

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_18():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text(None))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_19():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("XXCREATE INDEX IF NOT EXISTS ix_emp_livro ON emprestimo (livro_id);XX"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_20():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("create index if not exists ix_emp_livro on emprestimo (livro_id);"))

# -------------------------------------------------------------
# Criar índices
# -------------------------------------------------------------
def x_criar_indices__mutmut_21():
    with Session(engine) as session:
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS ix_emp_user ON emprestimo (usuario_id);"))
        session.exec(text("CREATE INDEX IF NOT EXISTS IX_EMP_LIVRO ON EMPRESTIMO (LIVRO_ID);"))

x_criar_indices__mutmut_mutants : ClassVar[MutantDict] = {
'x_criar_indices__mutmut_1': x_criar_indices__mutmut_1, 
    'x_criar_indices__mutmut_2': x_criar_indices__mutmut_2, 
    'x_criar_indices__mutmut_3': x_criar_indices__mutmut_3, 
    'x_criar_indices__mutmut_4': x_criar_indices__mutmut_4, 
    'x_criar_indices__mutmut_5': x_criar_indices__mutmut_5, 
    'x_criar_indices__mutmut_6': x_criar_indices__mutmut_6, 
    'x_criar_indices__mutmut_7': x_criar_indices__mutmut_7, 
    'x_criar_indices__mutmut_8': x_criar_indices__mutmut_8, 
    'x_criar_indices__mutmut_9': x_criar_indices__mutmut_9, 
    'x_criar_indices__mutmut_10': x_criar_indices__mutmut_10, 
    'x_criar_indices__mutmut_11': x_criar_indices__mutmut_11, 
    'x_criar_indices__mutmut_12': x_criar_indices__mutmut_12, 
    'x_criar_indices__mutmut_13': x_criar_indices__mutmut_13, 
    'x_criar_indices__mutmut_14': x_criar_indices__mutmut_14, 
    'x_criar_indices__mutmut_15': x_criar_indices__mutmut_15, 
    'x_criar_indices__mutmut_16': x_criar_indices__mutmut_16, 
    'x_criar_indices__mutmut_17': x_criar_indices__mutmut_17, 
    'x_criar_indices__mutmut_18': x_criar_indices__mutmut_18, 
    'x_criar_indices__mutmut_19': x_criar_indices__mutmut_19, 
    'x_criar_indices__mutmut_20': x_criar_indices__mutmut_20, 
    'x_criar_indices__mutmut_21': x_criar_indices__mutmut_21
}

def criar_indices(*args, **kwargs):
    result = _mutmut_trampoline(x_criar_indices__mutmut_orig, x_criar_indices__mutmut_mutants, args, kwargs)
    return result 

criar_indices.__signature__ = _mutmut_signature(x_criar_indices__mutmut_orig)
x_criar_indices__mutmut_orig.__name__ = 'x_criar_indices'

# -------------------------------------------------------------
# Parse de datas
# -------------------------------------------------------------
def x_parse_date__mutmut_orig(value):
    if value is None:
        return None
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)

# -------------------------------------------------------------
# Parse de datas
# -------------------------------------------------------------
def x_parse_date__mutmut_1(value):
    if value is not None:
        return None
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)

# -------------------------------------------------------------
# Parse de datas
# -------------------------------------------------------------
def x_parse_date__mutmut_2(value):
    if value is None:
        return None
    if isinstance(value, date):
        return value
    return date.fromisoformat(None)

x_parse_date__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_date__mutmut_1': x_parse_date__mutmut_1, 
    'x_parse_date__mutmut_2': x_parse_date__mutmut_2
}

def parse_date(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_date__mutmut_orig, x_parse_date__mutmut_mutants, args, kwargs)
    return result 

parse_date.__signature__ = _mutmut_signature(x_parse_date__mutmut_orig)
x_parse_date__mutmut_orig.__name__ = 'x_parse_date'

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_orig():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_1():
    with Session(None) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_2():
    with Session(engine) as session:
        tabela_livro_vazia = None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_3():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(None).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_4():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text(None)).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_5():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("XXSELECT 1 FROM livro LIMIT 1;XX")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_6():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("select 1 from livro limit 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_7():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM LIVRO LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_8():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is not None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_9():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_10():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(None).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_11():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text(None)).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_12():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("XXSELECT 1 FROM usuario LIMIT 1;XX")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_13():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("select 1 from usuario limit 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_14():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM USUARIO LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_15():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is not None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_16():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_17():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(None).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_18():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text(None)).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_19():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("XXSELECT 1 FROM emprestimo LIMIT 1;XX")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_20():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("select 1 from emprestimo limit 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_21():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM EMPRESTIMO LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_22():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is not None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_23():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_24():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia or tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_25():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia or tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_26():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open(None, encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_27():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding=None) as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_28():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open(encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_29():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", ) as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_30():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("XXrXX", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_31():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("R", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_32():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="XXutf-8XX") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_33():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="UTF-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_34():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = None

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_35():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(None)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_36():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open(None, encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_37():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding=None) as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_38():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open(encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_39():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", ) as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_40():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("XXrXX", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_41():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("R", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_42():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="XXutf-8XX") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_43():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="UTF-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_44():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = None

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_45():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(None)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_46():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open(None, encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_47():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding=None) as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_48():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open(encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_49():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", ) as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_50():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("XXrXX", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_51():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("R", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_52():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="XXutf-8XX") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_53():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="UTF-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_54():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = None

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_55():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(None)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_56():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = None
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_57():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["XXdata_emprestimoXX"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_58():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["DATA_EMPRESTIMO"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_59():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(None)
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_60():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["XXdata_emprestimoXX"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_61():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["DATA_EMPRESTIMO"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_62():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = None
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_63():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["XXdata_devolucao_previstaXX"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_64():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["DATA_DEVOLUCAO_PREVISTA"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_65():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(None)
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_66():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["XXdata_devolucao_previstaXX"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_67():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["DATA_DEVOLUCAO_PREVISTA"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_68():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = None

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_69():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["XXdata_devolucao_realXX"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_70():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["DATA_DEVOLUCAO_REAL"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_71():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(None)

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_72():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get(None))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_73():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("XXdata_devolucao_realXX"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_74():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("DATA_DEVOLUCAO_REAL"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_75():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all(None)
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_76():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all(None)
        session.add_all([Emprestimo(**e) for e in emprestimos])
        session.commit()

# -------------------------------------------------------------
# Seed
# -------------------------------------------------------------
def x_carregar_seed__mutmut_77():
    with Session(engine) as session:
        tabela_livro_vazia = session.exec(text("SELECT 1 FROM livro LIMIT 1;")).first() is None
        tabela_usuario_vazia = session.exec(text("SELECT 1 FROM usuario LIMIT 1;")).first() is None
        tabela_emprestimo_vazia = session.exec(text("SELECT 1 FROM emprestimo LIMIT 1;")).first() is None

        if not (tabela_livro_vazia and tabela_usuario_vazia and tabela_emprestimo_vazia):
            return

        with LIVROS_JSON.open("r", encoding="utf-8") as f:
            livros = json.load(f)

        with USUARIOS_JSON.open("r", encoding="utf-8") as f:
            usuarios = json.load(f)

        with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
            emprestimos = json.load(f)

        for e in emprestimos:
            e["data_emprestimo"] = parse_date(e["data_emprestimo"])
            e["data_devolucao_prevista"] = parse_date(e["data_devolucao_prevista"])
            e["data_devolucao_real"] = parse_date(e.get("data_devolucao_real"))

        session.add_all([Livro(**l) for l in livros])
        session.add_all([Usuario(**u) for u in usuarios])
        session.add_all(None)
        session.commit()

x_carregar_seed__mutmut_mutants : ClassVar[MutantDict] = {
'x_carregar_seed__mutmut_1': x_carregar_seed__mutmut_1, 
    'x_carregar_seed__mutmut_2': x_carregar_seed__mutmut_2, 
    'x_carregar_seed__mutmut_3': x_carregar_seed__mutmut_3, 
    'x_carregar_seed__mutmut_4': x_carregar_seed__mutmut_4, 
    'x_carregar_seed__mutmut_5': x_carregar_seed__mutmut_5, 
    'x_carregar_seed__mutmut_6': x_carregar_seed__mutmut_6, 
    'x_carregar_seed__mutmut_7': x_carregar_seed__mutmut_7, 
    'x_carregar_seed__mutmut_8': x_carregar_seed__mutmut_8, 
    'x_carregar_seed__mutmut_9': x_carregar_seed__mutmut_9, 
    'x_carregar_seed__mutmut_10': x_carregar_seed__mutmut_10, 
    'x_carregar_seed__mutmut_11': x_carregar_seed__mutmut_11, 
    'x_carregar_seed__mutmut_12': x_carregar_seed__mutmut_12, 
    'x_carregar_seed__mutmut_13': x_carregar_seed__mutmut_13, 
    'x_carregar_seed__mutmut_14': x_carregar_seed__mutmut_14, 
    'x_carregar_seed__mutmut_15': x_carregar_seed__mutmut_15, 
    'x_carregar_seed__mutmut_16': x_carregar_seed__mutmut_16, 
    'x_carregar_seed__mutmut_17': x_carregar_seed__mutmut_17, 
    'x_carregar_seed__mutmut_18': x_carregar_seed__mutmut_18, 
    'x_carregar_seed__mutmut_19': x_carregar_seed__mutmut_19, 
    'x_carregar_seed__mutmut_20': x_carregar_seed__mutmut_20, 
    'x_carregar_seed__mutmut_21': x_carregar_seed__mutmut_21, 
    'x_carregar_seed__mutmut_22': x_carregar_seed__mutmut_22, 
    'x_carregar_seed__mutmut_23': x_carregar_seed__mutmut_23, 
    'x_carregar_seed__mutmut_24': x_carregar_seed__mutmut_24, 
    'x_carregar_seed__mutmut_25': x_carregar_seed__mutmut_25, 
    'x_carregar_seed__mutmut_26': x_carregar_seed__mutmut_26, 
    'x_carregar_seed__mutmut_27': x_carregar_seed__mutmut_27, 
    'x_carregar_seed__mutmut_28': x_carregar_seed__mutmut_28, 
    'x_carregar_seed__mutmut_29': x_carregar_seed__mutmut_29, 
    'x_carregar_seed__mutmut_30': x_carregar_seed__mutmut_30, 
    'x_carregar_seed__mutmut_31': x_carregar_seed__mutmut_31, 
    'x_carregar_seed__mutmut_32': x_carregar_seed__mutmut_32, 
    'x_carregar_seed__mutmut_33': x_carregar_seed__mutmut_33, 
    'x_carregar_seed__mutmut_34': x_carregar_seed__mutmut_34, 
    'x_carregar_seed__mutmut_35': x_carregar_seed__mutmut_35, 
    'x_carregar_seed__mutmut_36': x_carregar_seed__mutmut_36, 
    'x_carregar_seed__mutmut_37': x_carregar_seed__mutmut_37, 
    'x_carregar_seed__mutmut_38': x_carregar_seed__mutmut_38, 
    'x_carregar_seed__mutmut_39': x_carregar_seed__mutmut_39, 
    'x_carregar_seed__mutmut_40': x_carregar_seed__mutmut_40, 
    'x_carregar_seed__mutmut_41': x_carregar_seed__mutmut_41, 
    'x_carregar_seed__mutmut_42': x_carregar_seed__mutmut_42, 
    'x_carregar_seed__mutmut_43': x_carregar_seed__mutmut_43, 
    'x_carregar_seed__mutmut_44': x_carregar_seed__mutmut_44, 
    'x_carregar_seed__mutmut_45': x_carregar_seed__mutmut_45, 
    'x_carregar_seed__mutmut_46': x_carregar_seed__mutmut_46, 
    'x_carregar_seed__mutmut_47': x_carregar_seed__mutmut_47, 
    'x_carregar_seed__mutmut_48': x_carregar_seed__mutmut_48, 
    'x_carregar_seed__mutmut_49': x_carregar_seed__mutmut_49, 
    'x_carregar_seed__mutmut_50': x_carregar_seed__mutmut_50, 
    'x_carregar_seed__mutmut_51': x_carregar_seed__mutmut_51, 
    'x_carregar_seed__mutmut_52': x_carregar_seed__mutmut_52, 
    'x_carregar_seed__mutmut_53': x_carregar_seed__mutmut_53, 
    'x_carregar_seed__mutmut_54': x_carregar_seed__mutmut_54, 
    'x_carregar_seed__mutmut_55': x_carregar_seed__mutmut_55, 
    'x_carregar_seed__mutmut_56': x_carregar_seed__mutmut_56, 
    'x_carregar_seed__mutmut_57': x_carregar_seed__mutmut_57, 
    'x_carregar_seed__mutmut_58': x_carregar_seed__mutmut_58, 
    'x_carregar_seed__mutmut_59': x_carregar_seed__mutmut_59, 
    'x_carregar_seed__mutmut_60': x_carregar_seed__mutmut_60, 
    'x_carregar_seed__mutmut_61': x_carregar_seed__mutmut_61, 
    'x_carregar_seed__mutmut_62': x_carregar_seed__mutmut_62, 
    'x_carregar_seed__mutmut_63': x_carregar_seed__mutmut_63, 
    'x_carregar_seed__mutmut_64': x_carregar_seed__mutmut_64, 
    'x_carregar_seed__mutmut_65': x_carregar_seed__mutmut_65, 
    'x_carregar_seed__mutmut_66': x_carregar_seed__mutmut_66, 
    'x_carregar_seed__mutmut_67': x_carregar_seed__mutmut_67, 
    'x_carregar_seed__mutmut_68': x_carregar_seed__mutmut_68, 
    'x_carregar_seed__mutmut_69': x_carregar_seed__mutmut_69, 
    'x_carregar_seed__mutmut_70': x_carregar_seed__mutmut_70, 
    'x_carregar_seed__mutmut_71': x_carregar_seed__mutmut_71, 
    'x_carregar_seed__mutmut_72': x_carregar_seed__mutmut_72, 
    'x_carregar_seed__mutmut_73': x_carregar_seed__mutmut_73, 
    'x_carregar_seed__mutmut_74': x_carregar_seed__mutmut_74, 
    'x_carregar_seed__mutmut_75': x_carregar_seed__mutmut_75, 
    'x_carregar_seed__mutmut_76': x_carregar_seed__mutmut_76, 
    'x_carregar_seed__mutmut_77': x_carregar_seed__mutmut_77
}

def carregar_seed(*args, **kwargs):
    result = _mutmut_trampoline(x_carregar_seed__mutmut_orig, x_carregar_seed__mutmut_mutants, args, kwargs)
    return result 

carregar_seed.__signature__ = _mutmut_signature(x_carregar_seed__mutmut_orig)
x_carregar_seed__mutmut_orig.__name__ = 'x_carregar_seed'

# -------------------------------------------------------------
# Inicializar banco (startup)
# -------------------------------------------------------------
def inicializar_banco():
    criar_tabelas()
    criar_indices()
    carregar_seed()

# -------------------------------------------------------------
# Resetar banco (rollback para testes)
# -------------------------------------------------------------
def x_resetar_banco__mutmut_orig():
    from aplicacao.db.sessao import engine as eng

    # fecha conexões
    eng.dispose()

    import time
    time.sleep(0.3)  # Windows precisa disso para soltar o arquivo

    # apaga arquivo antigo
    if DB_PATH.exists():
        try:
            DB_PATH.unlink()
        except PermissionError:
            time.sleep(0.5)
            DB_PATH.unlink()

    # recria tabelas
    SQLModel.metadata.create_all(eng)

# -------------------------------------------------------------
# Resetar banco (rollback para testes)
# -------------------------------------------------------------
def x_resetar_banco__mutmut_1():
    from aplicacao.db.sessao import engine as eng

    # fecha conexões
    eng.dispose()

    import time
    time.sleep(None)  # Windows precisa disso para soltar o arquivo

    # apaga arquivo antigo
    if DB_PATH.exists():
        try:
            DB_PATH.unlink()
        except PermissionError:
            time.sleep(0.5)
            DB_PATH.unlink()

    # recria tabelas
    SQLModel.metadata.create_all(eng)

# -------------------------------------------------------------
# Resetar banco (rollback para testes)
# -------------------------------------------------------------
def x_resetar_banco__mutmut_2():
    from aplicacao.db.sessao import engine as eng

    # fecha conexões
    eng.dispose()

    import time
    time.sleep(1.3)  # Windows precisa disso para soltar o arquivo

    # apaga arquivo antigo
    if DB_PATH.exists():
        try:
            DB_PATH.unlink()
        except PermissionError:
            time.sleep(0.5)
            DB_PATH.unlink()

    # recria tabelas
    SQLModel.metadata.create_all(eng)

# -------------------------------------------------------------
# Resetar banco (rollback para testes)
# -------------------------------------------------------------
def x_resetar_banco__mutmut_3():
    from aplicacao.db.sessao import engine as eng

    # fecha conexões
    eng.dispose()

    import time
    time.sleep(0.3)  # Windows precisa disso para soltar o arquivo

    # apaga arquivo antigo
    if DB_PATH.exists():
        try:
            DB_PATH.unlink()
        except PermissionError:
            time.sleep(None)
            DB_PATH.unlink()

    # recria tabelas
    SQLModel.metadata.create_all(eng)

# -------------------------------------------------------------
# Resetar banco (rollback para testes)
# -------------------------------------------------------------
def x_resetar_banco__mutmut_4():
    from aplicacao.db.sessao import engine as eng

    # fecha conexões
    eng.dispose()

    import time
    time.sleep(0.3)  # Windows precisa disso para soltar o arquivo

    # apaga arquivo antigo
    if DB_PATH.exists():
        try:
            DB_PATH.unlink()
        except PermissionError:
            time.sleep(1.5)
            DB_PATH.unlink()

    # recria tabelas
    SQLModel.metadata.create_all(eng)

# -------------------------------------------------------------
# Resetar banco (rollback para testes)
# -------------------------------------------------------------
def x_resetar_banco__mutmut_5():
    from aplicacao.db.sessao import engine as eng

    # fecha conexões
    eng.dispose()

    import time
    time.sleep(0.3)  # Windows precisa disso para soltar o arquivo

    # apaga arquivo antigo
    if DB_PATH.exists():
        try:
            DB_PATH.unlink()
        except PermissionError:
            time.sleep(0.5)
            DB_PATH.unlink()

    # recria tabelas
    SQLModel.metadata.create_all(None)

x_resetar_banco__mutmut_mutants : ClassVar[MutantDict] = {
'x_resetar_banco__mutmut_1': x_resetar_banco__mutmut_1, 
    'x_resetar_banco__mutmut_2': x_resetar_banco__mutmut_2, 
    'x_resetar_banco__mutmut_3': x_resetar_banco__mutmut_3, 
    'x_resetar_banco__mutmut_4': x_resetar_banco__mutmut_4, 
    'x_resetar_banco__mutmut_5': x_resetar_banco__mutmut_5
}

def resetar_banco(*args, **kwargs):
    result = _mutmut_trampoline(x_resetar_banco__mutmut_orig, x_resetar_banco__mutmut_mutants, args, kwargs)
    return result 

resetar_banco.__signature__ = _mutmut_signature(x_resetar_banco__mutmut_orig)
x_resetar_banco__mutmut_orig.__name__ = 'x_resetar_banco'
