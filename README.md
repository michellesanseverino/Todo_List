# 📝 Gerenciador de Tarefas (Todo List)

Uma aplicação de linha de comando (CLI) simples, modular e testável desenvolvida em Python para o gerenciamento de tarefas pessoais.

---

## 📌 Sobre o Projeto

O **Gerenciador de Tarefas** é uma aplicação focada na prática de boas práticas de desenvolvimento de software em Python. O projeto conta com separação de responsabilidades (interface vs. regras de negócio), tratamento de exceções e uma suíte de testes unitários automatizados com `pytest`.

---

## 🚀 Funcionalidades

- **Adicionar Tarefa:** Cadastra novas tarefas com validação de entradas em branco.
- **Listar Tarefas:** Exibe todas as tarefas de forma numerada e com marcadores de status (`[ ]` para pendente e `[x]` para concluída).
- **Concluir Tarefa:** Altera o status de uma tarefa selecionada para concluída.
- **Remover Tarefa:** Exclui tarefas da lista informando o número correspondente.
- **Validação de Dados:** Prevenção contra erros como `ValueError` e `IndexError`.

---

## 📂 Estrutura do Projeto

```text
todo_list_python/
│
├── src/                    # Código-fonte da aplicação
│   ├── __init__.py         # Pacote Python
│   ├── main.py             # Menu interativo e interface CLI
│   └── todo.py             # Regras de negócio e lógica das tarefas
│
├── tests/                  # Testes unitários automatizados
│   ├── __init__.py
│   └── test_todo.py        # Testes das funções com Pytest
│
├── .gitignore              # Arquivos ignorados pelo Git
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências do projeto (pytest)