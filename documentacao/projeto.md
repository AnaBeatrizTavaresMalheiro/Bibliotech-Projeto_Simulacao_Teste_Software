📚 Bibliotech — Documentação Inicial do Projeto

Sistema completo de gerenciamento de biblioteca com:

API REST em FastAPI

Interface Web com Jinja2 Templates

Banco SQLite com seed automático

Regras de negócio robustas (usuário, livro e empréstimos)

Estrutura modular seguindo boas práticas de arquitetura

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
