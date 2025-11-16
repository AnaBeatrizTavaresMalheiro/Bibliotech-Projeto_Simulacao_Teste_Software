📚 Regras de Negócio — Sistema de Gerenciamento de Empréstimos
🔹 1. Cadastro e gerenciamento de Livros
Regras

Cada livro possui:

titulo (texto)

isbn (único)

disponivel (True/False)

O ISBN é único.

Ao emprestar:

disponivel → False

Ao devolver:

disponivel → True

🔹 2. Cadastro e gerenciamento de Usuários
Regras

Todos os usuários possuem:

nome

email (validado, único)

qtd_emprestimo

possui_multa_aberta

O usuário não pode ter dois e-mails iguais.

O usuário pode ter no máximo 3 empréstimos ativos.

Se tiver multa aberta, não pode emprestar nenhum livro.

🔹 3. Empréstimos
Regras

Todo empréstimo vincula:

livro_id

usuario_id

data_emprestimo

data_devolucao_prevista

data_devolucao_real (preenchida na devolução)

Ao criar um empréstimo:

Verificar se o usuário:

Não tem multa.

Tem < 3 empréstimos ativos.

Verificar se o livro está disponível.

Atualizar:

Livro → disponivel = False

Usuário → qtd_emprestimo += 1

Ao devolver:

Registrar data_devolucao_real

Livro volta a disponivel = True

Usuário:

Se atrasou:

dias_atraso = diferença

valor_multa = dias_atraso * multa_por_dia

possui_multa_aberta = True

Se devolveu no prazo → nada acontece

🔹 4. Atualização e exclusão
Livros

Pode atualizar se não estiver emprestado.

Só pode deletar se não tiver empréstimos vinculados.

Usuários

Pode atualizar nome/e-mail (desde que e-mail seja único).

Pode deletar apenas se:

Não tiver empréstimos ativos.

Não tiver multa aberta.

Empréstimos

Não são deletados — apenas “finalizados” via devolução.

Não podem ser editados diretamente (apenas via regra de devolução).

🔹 5. Multas e atrasos

Cada dia de atraso gera:

multa = dias_atraso * config.multa_por_dia


Usuário com multa:

Não pode pegar novos livros.

Deve quitar multa manualmente (endpoint apropriado).

🔹 6. Regras de busca e listagem
Livros

Filtros:

titulo (like)

isbn (like)

disponivel (True/False)

Ordenação por:

id, titulo, isbn, disponivel

Usuários

Filtros:

nome

email

possui_multa_aberta

Empréstimos

Filtros:

Por usuário

Por livro

Por status (ativo/finalizado)

🔹 7. Tratamento de erros

ErroDeRegraNegocio

Tentativa de emprestar livro indisponível

Usuário com multa

Excedeu limite de empréstimos

ErroNaoEncontrado

Livro/usuário/emprestimo inexistente

Todos retornam códigos adequados (400, 404, 422)

⚙️ Guia de Execução do Projeto
1. Instalar dependências:
pip install -r requirements.txt

2. Criar tabelas + seed inicial:
python db/criar_schemas.py

3. Subir o servidor:
uvicorn server.main:app --reload

4. Acessar a documentação Swagger:

👉 http://127.0.0.1:8000/docs