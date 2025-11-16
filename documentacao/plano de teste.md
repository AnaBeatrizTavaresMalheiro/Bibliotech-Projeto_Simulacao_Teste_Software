📋 Plano de Teste — Projeto Bibliotech

🧩 1. Objetivo

Garantir a qualidade, corretude e robustez das funcionalidades do sistema Bibliotech, validando desde regras de negócio até endpoints REST e integração com banco de dados.

Este plano define o escopo, estratégias, técnicas, métricas e resultados obtidos durante a execução dos testes.

🎯 2. Escopo dos Testes

O projeto possui três camadas testadas:

Camada de Controle (API REST / FastAPI)
/usuarios, /livros, /emprestimos

Regras de Negócio
Validações de usuários, livros e empréstimos

Banco de Dados
Persistência via SQLite

🛠️ 3. Tipos de Teste Aplicados
3.1 Testes Unitários

Validam funcionalidades isoladas:

Regras de negócio dos módulos usuarios, livros e emprestimos

Tratamento de exceções (ErroDeRegraNegocio, ErroNaoEncontrado)

Comportamentos individuais (limites, condições inválidas etc.)

Total: 40 testes

3.2 Testes de Integração

Verificam vários módulos trabalhando juntos:

API REST + Banco de Dados

Sessões do SQLModel

Criação de usuários, livros e empréstimos reais

Total: 17 testes
Cobertura de integração: 88%

3.3 Testes Funcionais — Caixa Branca

Visam validar o fluxo interno da aplicação, com foco direto no código.

Total: 71 testes

3.4 Testes Funcionais — Caixa Preta

Validam o comportamento externo do sistema:

Respostas HTTP

Status codes

JSON retornado

Cenários de uso realista

Total: 10 testes

🧪 4. Técnicas Utilizadas

Rollback automático para isolamento entre testes
(reset do banco entre cada execução)

Testes de API via TestClient (FastAPI)

Mock / MagicMock para simulação de dependências

Análise estrutural (Caixa Branca)

Análise comportamental (Caixa Preta)

Mutation Testing para medir qualidade real dos testes

☠️ 5. Mutation Testing (MutMut)

Avalia se os testes realmente capturam falhas introduzidas artificialmente.

268 mutantes mortos

20 mutantes sobreviventes

Efetividade real: 93,1%

Fórmula usada:

Score = mortos / (mortos + vivos)
       = 268 / (268 + 20)
       = 93,1%


Esse índice indica uma suíte de testes madura, cobrindo bem a lógica interna.

📊 6. Métricas de Cobertura
Métrica	Valor
Cobertura geral do projeto	88%
Total de testes	138
Unitários	40
Integração	17
Caixa Branca	71
Caixa Preta	10
Mutação (Kill rate)	93,1%
📌 7. Conclusão

O processo de testes do Bibliotech obteve resultados robustos, mostrando:

Excelente cobertura estrutural (88%)

Forte detecção de falhas via mutation testing (93,1%)

Boa distribuição entre testes unitários, integração e funcionais

Validação completa dos principais fluxos da aplicação

A suíte de testes garante confiabilidade ao sistema, permitindo futuras evoluções com segurança e reduzindo riscos de regressões.

📌Execução dos testes:


## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Rossi-Luciano/teste_de_software.git
   cd teste_de_software/mutation-testing-demo
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   
   # Linux/Mac
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

### 4. Executar Geral

```bash
python -m pytest tests/ -v
```

### 5. Executar Testes de Mutação

```bash
# Remover cache anterior (se existir)
rm -rf .mutmut-cache/

# Executar mutmut
mutmut run
```

### 6. Executar Testes Unitário

```bash
tests/unit --cov=aplicacao --cov-report=term-missing -v
```
### 7. Executar Testes Integração
```bash
tests/integration --cov=aplicacao --cov-report=term-missing -v
```
### 8. Executar Testes Funcional
```bash
pytest tests/functional --cov=aplicacao --cov-report=term-missing -v
```

