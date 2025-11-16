📚 Bibliotech — Documentação Inicial do Projeto

Sistema completo de gerenciamento de biblioteca com:

API REST em FastAPI

Interface Web com Jinja2 Templates

Banco SQLite com seed automático

Regras de negócio robustas (usuário, livro e empréstimos)

Estrutura modular seguindo boas práticas de arquitetura

📁 1. Estrutura Geral do Projeto
aplicacao/
│
├── configuracoes/
│   ├── exceptions.py       # Exceções de regra de negócio e 404
│   ├── settings.py         # Configurações gerais
│   └── __init__.py
│
├── data/
│   ├── usuarios.json       # Seed inicial de usuários
│   ├── livros.json         # Seed inicial de livros
│   └── emprestimo.json     # Seed inicial de empréstimos
│
├── db/
│   ├── models.py           # Modelos SQLModel: Usuario, Livro, Emprestimo
│   ├── sessao.py           # Configuração da Session e Engine
│   └── database.py         # Inicialização do banco + carregamento de JSON
│
├── interface/
│   ├── router_web.py       # Rotas Web com templates Jinja2
│   │
│   ├── static/
│   │   └── style.css       # Estilos globais
│   │
│   └── templates/          # Html
│
├── regras_negocio/
│   ├── regras_usuario.py
│   ├── regras_livro.py
│   └── regras_emprestimo.py
│
├── routers/
│   ├── usuarios_router.py     # API REST Usuários
│   ├── livros_router.py       # API REST Livros
│   └── emprestimos_router.py  # API REST Empréstimos
│
├── services/
│   ├── usuario_service.py
│   ├── livro_service.py
│   └── emprestimo_service.py
│
└── server/
    └── main.py                # Aplicação FastAPI principal

🧠 3. Fluxo de Inicialização

O FastAPI inicia (startup)

database.inicializar_banco() é chamado

Banco é criado

Se estiver vazio → JSONs são carregados

Interface Web e API REST ficam disponíveis

🧩 4. Rotas da Aplicação

🌐 Web (HTML)
Recurso	Caminho
Home	/web
Usuários	/web/usuarios
Livros	/web/livros
Empréstimos	/web/emprestimos

🟦 API REST (JSON)
Recurso	Caminho
Usuários	/usuarios
Livros	/livros
Empréstimos	/emprestimos

🔐 5. Regras de Negócio
👤 Usuários

- Nome obrigatório

- Email único

- Máximo 3 empréstimos simultâneos

- Não pode ter multa pendente

- Não pode ser excluído se tiver empréstimo ativo

📘 Livros

- ISBN único

- Livro indisponível não pode ser emprestado

- Não exclui livro com empréstimo ativo

🔄 Empréstimos

- Devolução prevista = hoje + 7 dias

- Devolução duplicada não é permitida

- Atraso gera multa (1,50 por dia)

Devolver:

- marca livro como disponível

- decrementa contador do usuário

- define multa se necessário


🗄️ 7. Banco de Dados

SQLite local

Migrações automáticas

SQLModel (tipado e simples)

🚀 8. Como Executar
uvicorn aplicacao.server.main:app --reload


Acessar interface:

http://127.0.0.1:8000/web


Docs da API:

http://127.0.0.1:8000/docs