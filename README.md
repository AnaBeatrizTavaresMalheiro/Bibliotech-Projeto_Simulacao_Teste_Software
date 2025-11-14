# 📚 Sistema de Gerenciamento de Biblioteca — API (FastAPI)
Projeto desenvolvido para a disciplina **CC8550 - Simulação e Teste de Software**.  
Este sistema implementa uma API completa de gerenciamento de biblioteca, com operações CRUD, regras de negócio, validações, persistência em SQLite e testes automatizados.

---

## 📋 Descrição
A aplicação oferece endpoints REST para gerenciar:

- 📖 **Livros**
- 👥 **Usuários**
- 📋 **Empréstimos e Devoluções**

---

## 🚀 Instalação

### 1️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```
### 2️⃣ Inicializar o banco de dados
```bash
python src/db/inicializar.py
```
---
### 💻 Execução da API (FastAPI)

Inicie o servidor com recarregamento automático:
```bash
uvicorn src.server.main:app --reload
```

A API ficará disponível em:

🔗 http://127.0.0.1:8000

<img width="1184" height="70" alt="testes" src="https://github.com/user-attachments/assets/24d78df2-4fbe-48b5-8bac-4597df0c16e7" />


Documentação automática:

**http://127.0.0.1:8000/docs**

---

### 🧪 Testes

✔ Testes gerais:
```bash
pytest tests/ -v
```

✔ Testes com cobertura:
```bash
pytest --cov=src --cov-branch --cov-report=term-missing
```

---

### ✨ Funcionalidades do Sistema

✅ API REST completa

✅ CRUD de livros, usuários, autores e categorias

✅ Empréstimos com regras e validações

✅ Controle de devolução

✅ Exceções personalizadas

✅ Testes unitários e integrais

---

### 📝 Requisitos

* Python 3.10+

* SQLite (padrão no Python)

* FastAPI + Uvicorn

---

### 👥 Integrantes

Ana Beatriz de Souza - 24.122.018-5

Ana Beatriz Tavares Malheiro - 24.122.019-3

Luisa Graça Barbado - 24.122.058-1

---

### 📚 Disciplina

CC8550 – Simulação e Teste de Software

Centro Universitário FEI — 2º Semestre de 2025

