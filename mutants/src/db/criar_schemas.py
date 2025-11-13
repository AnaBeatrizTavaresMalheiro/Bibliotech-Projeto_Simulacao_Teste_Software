import json
import sqlite3
from pathlib import Path
from typing import Optional, List

ROOT_DIR = Path(__file__).resolve().parents[1]
DB_PATH = ROOT_DIR / "biblioteca.db"
DATA_DIR = ROOT_DIR / "data"
LIVROS_JSON = DATA_DIR / "livros.json"
USUARIOS_JSON = DATA_DIR / "usuarios.json"
EMPRESTIMO_JSON = DATA_DIR / "emprestimo.json"
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

class CriadorDeSchemasBiblioteca:
    def xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_orig(self, caminho_db: Path = DB_PATH) -> None:
        self.caminho_db: Path = caminho_db
        self.conexao: Optional[sqlite3.Connection] = None
    def xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_1(self, caminho_db: Path = DB_PATH) -> None:
        self.caminho_db: Path = None
        self.conexao: Optional[sqlite3.Connection] = None
    def xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_2(self, caminho_db: Path = DB_PATH) -> None:
        self.caminho_db: Path = caminho_db
        self.conexao: Optional[sqlite3.Connection] = ""
    
    xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_1': xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_2': xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_2
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁ__init____mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁ__init__'

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_orig(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, check_same_thread=False)
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_1(self) -> None:
        if self.conexao:
            return
        self.conexao = None
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_2(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(None, check_same_thread=False)
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_3(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, check_same_thread=None)
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_4(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(check_same_thread=False)
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_5(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, )
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_6(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, check_same_thread=True)
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_7(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, check_same_thread=False)
        self.conexao.execute(None)
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_8(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, check_same_thread=False)
        self.conexao.execute("XXPRAGMA foreign_keys = ON;XX")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_9(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, check_same_thread=False)
        self.conexao.execute("pragma foreign_keys = on;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_10(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, check_same_thread=False)
        self.conexao.execute("PRAGMA FOREIGN_KEYS = ON;")
        self.conexao.commit()
        print(f"[OK] Conectado a {self.caminho_db.name} (foreign_keys=ON)")

    # ----------------------------------------------------------
    # CONEXÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_11(self) -> None:
        if self.conexao:
            return
        self.conexao = sqlite3.connect(self.caminho_db, check_same_thread=False)
        self.conexao.execute("PRAGMA foreign_keys = ON;")
        self.conexao.commit()
        print(None)
    
    xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_1': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_2': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_2, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_3': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_3, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_4': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_4, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_5': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_5, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_6': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_6, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_7': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_7, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_8': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_8, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_9': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_9, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_10': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_10, 
        'xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_11': xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_11
    }
    
    def abrir(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_mutants"), args, kwargs, self)
        return result 
    
    abrir.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁabrir__mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁabrir'

    def xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_orig(self) -> None:
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            print("[OK] Conexão fechada.")

    def xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_1(self) -> None:
        if self.conexao:
            self.conexao.close()
            self.conexao = ""
            print("[OK] Conexão fechada.")

    def xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_2(self) -> None:
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            print(None)

    def xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_3(self) -> None:
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            print("XX[OK] Conexão fechada.XX")

    def xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_4(self) -> None:
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            print("[ok] conexão fechada.")

    def xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_5(self) -> None:
        if self.conexao:
            self.conexao.close()
            self.conexao = None
            print("[OK] CONEXÃO FECHADA.")
    
    xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_1': xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_2': xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_2, 
        'xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_3': xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_3, 
        'xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_4': xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_4, 
        'xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_5': xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_5
    }
    
    def fechar(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_mutants"), args, kwargs, self)
        return result 
    
    fechar.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁfechar__mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁfechar'

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_orig(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_1(self) -> None:
        assert self.conexao, "XXConexão não aberta. Use .abrir().XX"

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_2(self) -> None:
        assert self.conexao, "conexão não aberta. use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_3(self) -> None:
        assert self.conexao, "CONEXÃO NÃO ABERTA. USE .ABRIR()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_4(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = None

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_5(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = None

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_6(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = None

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_7(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = None
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_8(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute(None)
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_9(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("XXBEGIN;XX")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_10(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("begin;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_11(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(None)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_12(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(None)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_13(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(None)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_14(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print(None)
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_15(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("XX[OK] Tabelas criadas (ou já existiam).XX")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_16(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[ok] tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_17(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] TABELAS CRIADAS (OU JÁ EXISTIAM).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_18(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print(None, e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_19(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", None)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_20(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print(e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_21(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar tabelas:", )
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_22(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("XX[ERRO] Falha ao criar tabelas:XX", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_23(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[erro] falha ao criar tabelas:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DAS TABELAS
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_24(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        sql_livro = """
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            isbn TEXT NOT NULL UNIQUE,
            disponivel INTEGER NOT NULL DEFAULT 1
        );
        """

        sql_usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            qtd_emprestimo INTEGER NOT NULL DEFAULT 0,
            possui_multa_aberta INTEGER NOT NULL DEFAULT 0
        );
        """

        sql_emprestimo = """
        CREATE TABLE IF NOT EXISTS emprestimo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            livro_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL,
            data_emprestimo TEXT NOT NULL,
            data_devolucao_prevista TEXT NOT NULL,
            data_devolucao_real TEXT,
            dias_atraso INTEGER NOT NULL DEFAULT 0,
            valor_multa REAL NOT NULL DEFAULT 0.0,
            FOREIGN KEY (livro_id) REFERENCES livro(id),
            FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        );
        """

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            cur.execute(sql_livro)
            cur.execute(sql_usuario)
            cur.execute(sql_emprestimo)
            self.conexao.commit()
            print("[OK] Tabelas criadas (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] FALHA AO CRIAR TABELAS:", e)
            raise
    
    xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_1': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_2': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_2, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_3': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_3, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_4': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_4, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_5': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_5, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_6': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_6, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_7': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_7, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_8': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_8, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_9': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_9, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_10': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_10, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_11': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_11, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_12': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_12, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_13': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_13, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_14': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_14, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_15': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_15, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_16': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_16, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_17': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_17, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_18': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_18, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_19': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_19, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_20': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_20, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_21': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_21, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_22': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_22, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_23': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_23, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_24': xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_24
    }
    
    def criar_tabelas(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_mutants"), args, kwargs, self)
        return result 
    
    criar_tabelas.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁcriar_tabelas__mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁcriar_tabelas'

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_orig(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_1(self) -> None:
        assert self.conexao, "XXConexão não aberta. Use .abrir().XX"
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_2(self) -> None:
        assert self.conexao, "conexão não aberta. use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_3(self) -> None:
        assert self.conexao, "CONEXÃO NÃO ABERTA. USE .ABRIR()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_4(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = None
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_5(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "XXCREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);XX",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_6(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "create index if not exists ix_livro_titulo on livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_7(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS IX_LIVRO_TITULO ON LIVRO (TITULO);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_8(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "XXCREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);XX",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_9(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "create index if not exists ix_usuario_nome on usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_10(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS IX_USUARIO_NOME ON USUARIO (NOME);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_11(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "XXCREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);XX",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_12(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "create index if not exists ix_emprestimo_usuario on emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_13(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS IX_EMPRESTIMO_USUARIO ON EMPRESTIMO (USUARIO_ID);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_14(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "XXCREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);XX"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_15(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "create index if not exists ix_emprestimo_livro on emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_16(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS IX_EMPRESTIMO_LIVRO ON EMPRESTIMO (LIVRO_ID);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_17(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = None
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_18(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute(None)
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_19(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("XXBEGIN;XX")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_20(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("begin;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_21(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(None)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_22(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print(None)
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_23(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("XX[OK] Índices criados (ou já existiam).XX")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_24(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[ok] índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_25(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] ÍNDICES CRIADOS (OU JÁ EXISTIAM).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_26(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print(None, e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_27(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", None)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_28(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print(e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_29(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao criar índices:", )
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_30(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("XX[ERRO] Falha ao criar índices:XX", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_31(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[erro] falha ao criar índices:", e)
            raise

    # ----------------------------------------------------------
    # CRIAÇÃO DE ÍNDICES
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_32(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        indices = [
            "CREATE INDEX IF NOT EXISTS ix_livro_titulo ON livro (titulo);",
            "CREATE INDEX IF NOT EXISTS ix_usuario_nome ON usuario (nome);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_usuario ON emprestimo (usuario_id);",
            "CREATE INDEX IF NOT EXISTS ix_emprestimo_livro ON emprestimo (livro_id);"
        ]
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            for ddl in indices:
                cur.execute(ddl)
            self.conexao.commit()
            print("[OK] Índices criados (ou já existiam).")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] FALHA AO CRIAR ÍNDICES:", e)
            raise
    
    xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_1': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_2': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_2, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_3': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_3, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_4': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_4, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_5': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_5, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_6': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_6, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_7': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_7, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_8': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_8, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_9': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_9, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_10': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_10, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_11': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_11, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_12': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_12, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_13': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_13, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_14': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_14, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_15': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_15, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_16': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_16, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_17': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_17, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_18': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_18, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_19': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_19, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_20': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_20, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_21': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_21, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_22': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_22, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_23': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_23, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_24': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_24, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_25': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_25, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_26': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_26, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_27': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_27, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_28': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_28, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_29': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_29, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_30': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_30, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_31': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_31, 
        'xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_32': xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_32
    }
    
    def criar_indices(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_mutants"), args, kwargs, self)
        return result 
    
    criar_indices.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁcriar_indices__mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁcriar_indices'

    # ----------------------------------------------------------
    # SEED — INSERIR DADOS SE VAZIO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_orig(self, nome_tabela: str) -> bool:
        assert self.conexao
        cur = self.conexao.execute(f"SELECT 1 FROM {nome_tabela} LIMIT 1;")
        return cur.fetchone() is None

    # ----------------------------------------------------------
    # SEED — INSERIR DADOS SE VAZIO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_1(self, nome_tabela: str) -> bool:
        assert self.conexao
        cur = None
        return cur.fetchone() is None

    # ----------------------------------------------------------
    # SEED — INSERIR DADOS SE VAZIO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_2(self, nome_tabela: str) -> bool:
        assert self.conexao
        cur = self.conexao.execute(None)
        return cur.fetchone() is None

    # ----------------------------------------------------------
    # SEED — INSERIR DADOS SE VAZIO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_3(self, nome_tabela: str) -> bool:
        assert self.conexao
        cur = self.conexao.execute(f"SELECT 1 FROM {nome_tabela} LIMIT 1;")
        return cur.fetchone() is not None
    
    xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_1': xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_2': xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_2, 
        'xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_3': xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_3
    }
    
    def _tabela_vazia(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _tabela_vazia.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia__mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁ_tabela_vazia'

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_orig(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_1(self) -> None:
        assert self.conexao, "XXConexão não aberta. Use .abrir().XX"

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_2(self) -> None:
        assert self.conexao, "conexão não aberta. use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_3(self) -> None:
        assert self.conexao, "CONEXÃO NÃO ABERTA. USE .ABRIR()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_4(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = None
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_5(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia(None)
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_6(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("XXlivroXX")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_7(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("LIVRO")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_8(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = None
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_9(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia(None)
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_10(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("XXusuarioXX")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_11(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("USUARIO")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_12(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = None

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_13(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia(None)

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_14(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("XXemprestimoXX")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_15(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("EMPRESTIMO")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_16(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios or not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_17(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios or not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_18(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_19(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_20(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_21(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print(None)
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_22(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("XX[INFO] Seed: tabelas já possuem dados. Nada a fazer.XX")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_23(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[info] seed: tabelas já possuem dados. nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_24(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] SEED: TABELAS JÁ POSSUEM DADOS. NADA A FAZER.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_25(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = None
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_26(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = None

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_27(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open(None, encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_28(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding=None) as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_29(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open(encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_30(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", ) as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_31(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("XXrXX", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_32(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("R", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_33(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="XXutf-8XX") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_34(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="UTF-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_35(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = None
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_36(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(None)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_37(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open(None, encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_38(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding=None) as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_39(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open(encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_40(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", ) as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_41(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("XXrXX", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_42(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("R", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_43(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="XXutf-8XX") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_44(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="UTF-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_45(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = None
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_46(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(None)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_47(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open(None, encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_48(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding=None) as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_49(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open(encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_50(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", ) as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_51(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("XXrXX", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_52(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("R", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_53(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="XXutf-8XX") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_54(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="UTF-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_55(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = None

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_56(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(None)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_57(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = None
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_58(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute(None)
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_59(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("XXBEGIN;XX")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_60(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("begin;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_61(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios or livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_62(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    None,
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_63(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    None,
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_64(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_65(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_66(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "XXINSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);XX",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_67(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "insert into livro (titulo, isbn, disponivel) values (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_68(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO LIVRO (TITULO, ISBN, DISPONIVEL) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_69(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["XXtituloXX"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_70(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["TITULO"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_71(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["XXisbnXX"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_72(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["ISBN"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_73(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 2 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_74(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get(None, True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_75(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", None) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_76(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get(True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_77(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", ) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_78(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("XXdisponivelXX", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_79(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("DISPONIVEL", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_80(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", False) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_81(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 1) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_82(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(None)

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_83(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios or usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_84(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    None,
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_85(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    None,
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_86(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_87(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_88(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "XXINSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);XX",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_89(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "insert into usuario (nome, email, possui_multa_aberta) values (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_90(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO USUARIO (NOME, EMAIL, POSSUI_MULTA_ABERTA) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_91(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["XXnomeXX"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_92(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["NOME"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_93(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["XXemailXX"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_94(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["EMAIL"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_95(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 2 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_96(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get(None, False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_97(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", None) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_98(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get(False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_99(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", ) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_100(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("XXpossui_multa_abertaXX", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_101(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("POSSUI_MULTA_ABERTA", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_102(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", True) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_103(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 1) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_104(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(None)

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_105(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios or emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_106(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    None,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_107(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    None,
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_108(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_109(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_110(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["XXlivro_idXX"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_111(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["LIVRO_ID"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_112(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["XXusuario_idXX"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_113(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["USUARIO_ID"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_114(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["XXdata_emprestimoXX"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_115(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["DATA_EMPRESTIMO"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_116(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["XXdata_devolucao_previstaXX"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_117(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["DATA_DEVOLUCAO_PREVISTA"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_118(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get(None),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_119(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("XXdata_devolucao_realXX"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_120(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("DATA_DEVOLUCAO_REAL"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_121(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get(None, 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_122(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", None),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_123(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get(0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_124(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", ),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_125(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("XXdias_atrasoXX", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_126(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("DIAS_ATRASO", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_127(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 1),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_128(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get(None, 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_129(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", None),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_130(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get(0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_131(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", ),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_132(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("XXvalor_multaXX", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_133(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("VALOR_MULTA", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_134(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 1.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_135(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(None)

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(f"[ERRO] Falha ao inserir seed: {e}")

    def xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_136(self) -> None:
        assert self.conexao, "Conexão não aberta. Use .abrir()."

        livros_vazios = self._tabela_vazia("livro")
        usuarios_vazios = self._tabela_vazia("usuario")
        emprestimos_vazios = self._tabela_vazia("emprestimo")

        if not livros_vazios and not usuarios_vazios and not emprestimos_vazios:
            print("[INFO] Seed: tabelas já possuem dados. Nada a fazer.")
            return

        # Lê os arquivos JSON
        livros = []
        usuarios = []

        if LIVROS_JSON.exists():
            with LIVROS_JSON.open("r", encoding="utf-8") as f:
                livros = json.load(f)
        if USUARIOS_JSON.exists():
            with USUARIOS_JSON.open("r", encoding="utf-8") as f:
                usuarios = json.load(f)
        if EMPRESTIMO_JSON.exists():
            with EMPRESTIMO_JSON.open("r", encoding="utf-8") as f:
                emprestimos = json.load(f)

        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            if livros_vazios and livros:
                cur.executemany(
                    "INSERT INTO livro (titulo, isbn, disponivel) VALUES (?, ?, ?);",
                    [(l["titulo"], l["isbn"], 1 if l.get("disponivel", True) else 0) for l in livros],
                )
                print(f"[OK] Seed de livros inserido: {len(livros)} registros.")

            if usuarios_vazios and usuarios:
                cur.executemany(
                    "INSERT INTO usuario (nome, email, possui_multa_aberta) VALUES (?, ?, ?);",
                    [(u["nome"], u["email"], 1 if u.get("possui_multa_aberta", False) else 0) for u in usuarios],
                )
                print(f"[OK] Seed de usuários inserido: {len(usuarios)} registros.")

            if emprestimos_vazios and emprestimos:
                cur.executemany(
                    """
                    INSERT INTO emprestimo
                        (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista,
                        data_devolucao_real, dias_atraso, valor_multa)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    [
                        (
                            e["livro_id"],
                            e["usuario_id"],
                            e["data_emprestimo"],
                            e["data_devolucao_prevista"],
                            e.get("data_devolucao_real"),
                            e.get("dias_atraso", 0),
                            e.get("valor_multa", 0.0),
                        )
                        for e in emprestimos
                    ],
                )
                print(f"[OK] Seed de empréstimos inserido: {len(emprestimos)} registros.")

            self.conexao.commit()

        except Exception as e:
            self.conexao.rollback()
            print(None)
    
    xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_1': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_2': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_2, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_3': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_3, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_4': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_4, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_5': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_5, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_6': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_6, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_7': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_7, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_8': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_8, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_9': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_9, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_10': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_10, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_11': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_11, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_12': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_12, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_13': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_13, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_14': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_14, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_15': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_15, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_16': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_16, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_17': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_17, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_18': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_18, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_19': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_19, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_20': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_20, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_21': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_21, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_22': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_22, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_23': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_23, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_24': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_24, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_25': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_25, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_26': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_26, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_27': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_27, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_28': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_28, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_29': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_29, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_30': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_30, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_31': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_31, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_32': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_32, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_33': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_33, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_34': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_34, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_35': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_35, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_36': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_36, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_37': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_37, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_38': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_38, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_39': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_39, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_40': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_40, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_41': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_41, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_42': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_42, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_43': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_43, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_44': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_44, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_45': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_45, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_46': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_46, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_47': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_47, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_48': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_48, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_49': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_49, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_50': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_50, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_51': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_51, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_52': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_52, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_53': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_53, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_54': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_54, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_55': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_55, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_56': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_56, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_57': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_57, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_58': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_58, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_59': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_59, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_60': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_60, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_61': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_61, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_62': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_62, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_63': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_63, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_64': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_64, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_65': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_65, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_66': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_66, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_67': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_67, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_68': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_68, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_69': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_69, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_70': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_70, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_71': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_71, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_72': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_72, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_73': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_73, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_74': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_74, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_75': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_75, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_76': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_76, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_77': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_77, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_78': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_78, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_79': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_79, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_80': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_80, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_81': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_81, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_82': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_82, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_83': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_83, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_84': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_84, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_85': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_85, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_86': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_86, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_87': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_87, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_88': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_88, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_89': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_89, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_90': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_90, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_91': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_91, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_92': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_92, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_93': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_93, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_94': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_94, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_95': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_95, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_96': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_96, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_97': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_97, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_98': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_98, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_99': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_99, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_100': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_100, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_101': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_101, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_102': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_102, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_103': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_103, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_104': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_104, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_105': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_105, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_106': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_106, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_107': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_107, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_108': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_108, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_109': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_109, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_110': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_110, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_111': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_111, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_112': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_112, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_113': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_113, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_114': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_114, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_115': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_115, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_116': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_116, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_117': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_117, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_118': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_118, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_119': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_119, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_120': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_120, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_121': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_121, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_122': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_122, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_123': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_123, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_124': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_124, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_125': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_125, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_126': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_126, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_127': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_127, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_128': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_128, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_129': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_129, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_130': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_130, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_131': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_131, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_132': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_132, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_133': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_133, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_134': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_134, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_135': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_135, 
        'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_136': xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_136
    }
    
    def inserir_seed_se_vazio(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_mutants"), args, kwargs, self)
        return result 
    
    inserir_seed_se_vazio.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio__mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁinserir_seed_se_vazio'


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_orig(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_1(self) -> None:
        assert self.conexao
        tabelas = None
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_2(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            None
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_3(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "XXSELECT name FROM sqlite_master WHERE type='table' ORDER BY name;XX"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_4(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "select name from sqlite_master where type='table' order by name;"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_5(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT NAME FROM SQLITE_MASTER WHERE TYPE='TABLE' ORDER BY NAME;"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_6(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print(None)
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_7(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("XX\n=== Tabelas ===XX")
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_8(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("\n=== tabelas ===")
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_9(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("\n=== TABELAS ===")
        for (nome,) in tabelas:
            print(" -", nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_10(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(None, nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_11(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(" -", None)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_12(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(nome)


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_13(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print(" -", )


    # ----------------------------------------------------------
    # INSPEÇÃO
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_14(self) -> None:
        assert self.conexao
        tabelas = self.conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        ).fetchall()
        print("\n=== Tabelas ===")
        for (nome,) in tabelas:
            print("XX -XX", nome)
    
    xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_1': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_2': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_2, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_3': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_3, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_4': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_4, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_5': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_5, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_6': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_6, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_7': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_7, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_8': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_8, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_9': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_9, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_10': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_10, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_11': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_11, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_12': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_12, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_13': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_13, 
        'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_14': xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_14
    }
    
    def mostrar_resumo(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_mutants"), args, kwargs, self)
        return result 
    
    mostrar_resumo.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁmostrar_resumo__mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁmostrar_resumo'

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_orig(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_1(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "XXConexão não aberta. Use .abrir().XX"
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_2(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "conexão não aberta. use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_3(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "CONEXÃO NÃO ABERTA. USE .ABRIR()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_4(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = None
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_5(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute(None)
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_6(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("XXBEGIN;XX")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_7(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("begin;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_8(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute(None)

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_9(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("XXPRAGMA foreign_keys = OFF;XX")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_10(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("pragma foreign_keys = off;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_11(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA FOREIGN_KEYS = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_12(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute(None)
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_13(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("XXDELETE FROM emprestimo;XX")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_14(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("delete from emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_15(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM EMPRESTIMO;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_16(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute(None)
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_17(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("XXDELETE FROM usuario;XX")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_18(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("delete from usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_19(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM USUARIO;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_20(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute(None)

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_21(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("XXDELETE FROM livro;XX")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_22(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("delete from livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_23(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM LIVRO;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_24(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute(None)

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_25(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("XXDELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');XX")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_26(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("delete from sqlite_sequence where name in ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_27(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME IN ('EMPRESTIMO','USUARIO','LIVRO');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_28(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute(None)
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_29(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("XXPRAGMA foreign_keys = ON;XX")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_30(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("pragma foreign_keys = on;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_31(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA FOREIGN_KEYS = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_32(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print(None)
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_33(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("XX[OK] Banco limpo: todas as tabelas truncadas.XX")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_34(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[ok] banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_35(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] BANCO LIMPO: TODAS AS TABELAS TRUNCADAS.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_36(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print(None, e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_37(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", None)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_38(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print(e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_39(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] Falha ao limpar banco:", )
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_40(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("XX[ERRO] Falha ao limpar banco:XX", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_41(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[erro] falha ao limpar banco:", e)
            raise

    # ----------------------------------------------------------
    # LIMPEZA / RESET
    # ----------------------------------------------------------
    def xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_42(self) -> None:
        """
        Apaga todo o conteúdo das tabelas e reseta autoincrement,
        preservando o schema.
        """
        assert self.conexao, "Conexão não aberta. Use .abrir()."
        cur = self.conexao.cursor()
        cur.execute("BEGIN;")
        try:
            # Desabilita FK temporariamente para truncar sem ordem
            cur.execute("PRAGMA foreign_keys = OFF;")

            # Limpa tabelas conhecidas (mais seguro do que varrer sqlite_master)
            cur.execute("DELETE FROM emprestimo;")
            cur.execute("DELETE FROM usuario;")
            cur.execute("DELETE FROM livro;")

            # Reseta AUTOINCREMENT
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('emprestimo','usuario','livro');")

            # Reabilita FK
            cur.execute("PRAGMA foreign_keys = ON;")
            self.conexao.commit()
            print("[OK] Banco limpo: todas as tabelas truncadas.")
        except Exception as e:
            self.conexao.rollback()
            print("[ERRO] FALHA AO LIMPAR BANCO:", e)
            raise
    
    xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_1': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_2': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_2, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_3': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_3, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_4': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_4, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_5': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_5, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_6': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_6, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_7': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_7, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_8': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_8, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_9': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_9, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_10': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_10, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_11': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_11, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_12': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_12, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_13': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_13, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_14': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_14, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_15': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_15, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_16': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_16, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_17': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_17, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_18': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_18, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_19': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_19, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_20': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_20, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_21': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_21, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_22': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_22, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_23': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_23, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_24': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_24, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_25': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_25, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_26': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_26, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_27': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_27, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_28': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_28, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_29': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_29, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_30': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_30, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_31': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_31, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_32': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_32, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_33': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_33, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_34': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_34, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_35': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_35, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_36': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_36, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_37': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_37, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_38': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_38, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_39': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_39, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_40': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_40, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_41': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_41, 
        'xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_42': xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_42
    }
    
    def limpar_banco(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_mutants"), args, kwargs, self)
        return result 
    
    limpar_banco.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁlimpar_banco__mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁlimpar_banco'

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_orig(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_1(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_2(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute(None)
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_3(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("XXVACUUM;XX")
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_4(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("vacuum;")
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_5(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print(None)
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_6(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("XX[OK] VACUUM executado (reset lógico concluído).XX")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_7(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("[ok] vacuum executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_8(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("[OK] VACUUM EXECUTADO (RESET LÓGICO CONCLUÍDO).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_9(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(None)

        print("[OK] Banco resetado (truncate + VACUUM).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_10(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print(None)

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_11(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("XX[OK] Banco resetado (truncate + VACUUM).XX")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_12(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[ok] banco resetado (truncate + vacuum).")

    def xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_13(self) -> None:
        """
        Reset “seguro” para Windows: em vez de apagar o arquivo (que pode estar em uso),
        limpa todas as tabelas, reseta autoincrement e roda VACUUM.
        Resultado final: banco vazio e compactado.
        """
        # Garante conexão aberta
        if not self.conexao:
            self.abrir()

        # Limpa conteúdo
        self.limpar_banco()

        # Compacta/zera páginas órfãs
        try:
            self.conexao.execute("VACUUM;")
            self.conexao.commit()
            print("[OK] VACUUM executado (reset lógico concluído).")
        except Exception as e:
            # Se VACUUM falhar, o banco já está limpo; não precisa quebrar o fluxo.
            print(f"[WARN] Falha no VACUUM (seguindo adiante): {e}")

        print("[OK] BANCO RESETADO (TRUNCATE + VACUUM).")
    
    xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_1': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_1, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_2': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_2, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_3': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_3, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_4': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_4, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_5': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_5, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_6': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_6, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_7': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_7, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_8': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_8, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_9': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_9, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_10': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_10, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_11': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_11, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_12': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_12, 
        'xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_13': xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_13
    }
    
    def resetar_banco(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_orig"), object.__getattribute__(self, "xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_mutants"), args, kwargs, self)
        return result 
    
    resetar_banco.__signature__ = _mutmut_signature(xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_orig)
    xǁCriadorDeSchemasBibliotecaǁresetar_banco__mutmut_orig.__name__ = 'xǁCriadorDeSchemasBibliotecaǁresetar_banco'


# --- Funções de fachada para usar no FastAPI ---

def x_inicializar_banco__mutmut_orig() -> None:
    """
    Cria tabelas e índices. Não insere dados.
    Útil para ser chamado no evento de startup da API.
    """
    ddl = CriadorDeSchemasBiblioteca()
    ddl.abrir()
    ddl.criar_tabelas()
    ddl.criar_indices()
    ddl.fechar()
    print("[OK] Banco inicializado (tabelas + índices).")


# --- Funções de fachada para usar no FastAPI ---

def x_inicializar_banco__mutmut_1() -> None:
    """
    Cria tabelas e índices. Não insere dados.
    Útil para ser chamado no evento de startup da API.
    """
    ddl = None
    ddl.abrir()
    ddl.criar_tabelas()
    ddl.criar_indices()
    ddl.fechar()
    print("[OK] Banco inicializado (tabelas + índices).")


# --- Funções de fachada para usar no FastAPI ---

def x_inicializar_banco__mutmut_2() -> None:
    """
    Cria tabelas e índices. Não insere dados.
    Útil para ser chamado no evento de startup da API.
    """
    ddl = CriadorDeSchemasBiblioteca()
    ddl.abrir()
    ddl.criar_tabelas()
    ddl.criar_indices()
    ddl.fechar()
    print(None)


# --- Funções de fachada para usar no FastAPI ---

def x_inicializar_banco__mutmut_3() -> None:
    """
    Cria tabelas e índices. Não insere dados.
    Útil para ser chamado no evento de startup da API.
    """
    ddl = CriadorDeSchemasBiblioteca()
    ddl.abrir()
    ddl.criar_tabelas()
    ddl.criar_indices()
    ddl.fechar()
    print("XX[OK] Banco inicializado (tabelas + índices).XX")


# --- Funções de fachada para usar no FastAPI ---

def x_inicializar_banco__mutmut_4() -> None:
    """
    Cria tabelas e índices. Não insere dados.
    Útil para ser chamado no evento de startup da API.
    """
    ddl = CriadorDeSchemasBiblioteca()
    ddl.abrir()
    ddl.criar_tabelas()
    ddl.criar_indices()
    ddl.fechar()
    print("[ok] banco inicializado (tabelas + índices).")


# --- Funções de fachada para usar no FastAPI ---

def x_inicializar_banco__mutmut_5() -> None:
    """
    Cria tabelas e índices. Não insere dados.
    Útil para ser chamado no evento de startup da API.
    """
    ddl = CriadorDeSchemasBiblioteca()
    ddl.abrir()
    ddl.criar_tabelas()
    ddl.criar_indices()
    ddl.fechar()
    print("[OK] BANCO INICIALIZADO (TABELAS + ÍNDICES).")

x_inicializar_banco__mutmut_mutants : ClassVar[MutantDict] = {
'x_inicializar_banco__mutmut_1': x_inicializar_banco__mutmut_1, 
    'x_inicializar_banco__mutmut_2': x_inicializar_banco__mutmut_2, 
    'x_inicializar_banco__mutmut_3': x_inicializar_banco__mutmut_3, 
    'x_inicializar_banco__mutmut_4': x_inicializar_banco__mutmut_4, 
    'x_inicializar_banco__mutmut_5': x_inicializar_banco__mutmut_5
}

def inicializar_banco(*args, **kwargs):
    result = _mutmut_trampoline(x_inicializar_banco__mutmut_orig, x_inicializar_banco__mutmut_mutants, args, kwargs)
    return result 

inicializar_banco.__signature__ = _mutmut_signature(x_inicializar_banco__mutmut_orig)
x_inicializar_banco__mutmut_orig.__name__ = 'x_inicializar_banco'

def x_carregar_seed_se_vazio__mutmut_orig() -> None:
    """
    Insere dados do data/livros.json e data/usuarios.json
    apenas se as tabelas estiverem vazias.
    """
    ddl = CriadorDeSchemasBiblioteca()
    try:
        # garante que as tabelas existem antes de checar se estão vazias
        ddl.abrir()
        ddl.criar_tabelas()
        ddl.criar_indices()
        ddl.inserir_seed_se_vazio()
    finally:
        ddl.fechar()

def x_carregar_seed_se_vazio__mutmut_1() -> None:
    """
    Insere dados do data/livros.json e data/usuarios.json
    apenas se as tabelas estiverem vazias.
    """
    ddl = None
    try:
        # garante que as tabelas existem antes de checar se estão vazias
        ddl.abrir()
        ddl.criar_tabelas()
        ddl.criar_indices()
        ddl.inserir_seed_se_vazio()
    finally:
        ddl.fechar()

x_carregar_seed_se_vazio__mutmut_mutants : ClassVar[MutantDict] = {
'x_carregar_seed_se_vazio__mutmut_1': x_carregar_seed_se_vazio__mutmut_1
}

def carregar_seed_se_vazio(*args, **kwargs):
    result = _mutmut_trampoline(x_carregar_seed_se_vazio__mutmut_orig, x_carregar_seed_se_vazio__mutmut_mutants, args, kwargs)
    return result 

carregar_seed_se_vazio.__signature__ = _mutmut_signature(x_carregar_seed_se_vazio__mutmut_orig)
x_carregar_seed_se_vazio__mutmut_orig.__name__ = 'x_carregar_seed_se_vazio'

def x_limpar_banco_via_api__mutmut_orig() -> None:
    ddl = CriadorDeSchemasBiblioteca()
    try:
        ddl.abrir()
        ddl.limpar_banco()
    finally:
        ddl.fechar()

def x_limpar_banco_via_api__mutmut_1() -> None:
    ddl = None
    try:
        ddl.abrir()
        ddl.limpar_banco()
    finally:
        ddl.fechar()

x_limpar_banco_via_api__mutmut_mutants : ClassVar[MutantDict] = {
'x_limpar_banco_via_api__mutmut_1': x_limpar_banco_via_api__mutmut_1
}

def limpar_banco_via_api(*args, **kwargs):
    result = _mutmut_trampoline(x_limpar_banco_via_api__mutmut_orig, x_limpar_banco_via_api__mutmut_mutants, args, kwargs)
    return result 

limpar_banco_via_api.__signature__ = _mutmut_signature(x_limpar_banco_via_api__mutmut_orig)
x_limpar_banco_via_api__mutmut_orig.__name__ = 'x_limpar_banco_via_api'

def x_resetar_banco_via_api__mutmut_orig() -> None:
    ddl = CriadorDeSchemasBiblioteca()
    try:
        ddl.resetar_banco()  # método de instância
    finally:
        ddl.fechar()

def x_resetar_banco_via_api__mutmut_1() -> None:
    ddl = None
    try:
        ddl.resetar_banco()  # método de instância
    finally:
        ddl.fechar()

x_resetar_banco_via_api__mutmut_mutants : ClassVar[MutantDict] = {
'x_resetar_banco_via_api__mutmut_1': x_resetar_banco_via_api__mutmut_1
}

def resetar_banco_via_api(*args, **kwargs):
    result = _mutmut_trampoline(x_resetar_banco_via_api__mutmut_orig, x_resetar_banco_via_api__mutmut_mutants, args, kwargs)
    return result 

resetar_banco_via_api.__signature__ = _mutmut_signature(x_resetar_banco_via_api__mutmut_orig)
x_resetar_banco_via_api__mutmut_orig.__name__ = 'x_resetar_banco_via_api'



# ----------------------------------------------------------
# EXECUÇÃO DIRETA
# ----------------------------------------------------------
if __name__ == "__main__":
    ddl = CriadorDeSchemasBiblioteca()
    ddl.abrir()
    ddl.criar_tabelas()
    ddl.criar_indices()
    ddl.inserir_seed_se_vazio()
    ddl.mostrar_resumo()
    ddl.fechar()



# debug

# from pydantic import BaseModel, EmailStr, constr

# class UsuarioIn(BaseModel):
#     nome: constr(min_length=1)        # pelo menos 1 caractere
#     email: EmailStr                    # valida formato de e-mail



    
# from typing import Optional
# from pydantic import BaseModel, EmailStr, constr
# from datetime import date


# # ==========================================================
# # USUÁRIOS
# # ==========================================================
# class UsuarioIn(BaseModel):
#     nome: constr(min_length=1)
#     email: EmailStr


# class UsuarioOut(BaseModel):
#     id: int
#     nome: str
#     email: EmailStr

#     class Config:
#         orm_mode = True


# class UsuarioUpdate(BaseModel):
#     nome: Optional[str] = None
#     email: Optional[EmailStr] = None


# # ==========================================================
# # LIVROS
# # ==========================================================
# class LivroIn(BaseModel):
#     titulo: constr(min_length=1)
#     isbn: constr(min_length=5)


# class LivroOut(BaseModel):
#     id: int
#     titulo: str
#     isbn: str
#     disponivel: bool

#     class Config:
#         orm_mode = True


# # ==========================================================
# # EMPRÉSTIMOS
# # ==========================================================
# class EmprestimoIn(BaseModel):
#     livro_id: int
#     usuario_id: int
#     data_emprestimo: date
#     data_devolucao_prevista: date


# class EmprestimoOut(BaseModel):
#     id: int
#     livro_id: int
#     usuario_id: int
#     data_emprestimo: date
#     data_devolucao_prevista: date
#     data_devolucao_real: Optional[date] = None
#     dias_atraso: int
#     valor_multa: float

#     class Config:
#         orm_mode = True
