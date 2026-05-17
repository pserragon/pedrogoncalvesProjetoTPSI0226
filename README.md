# ByteTech

## Login da Aplicação

```text
Username: admin
Password: ByteTech123
```

---

## Descrição

O ByteTech é um projeto desenvolvido em Python que simula um sistema de gestão de uma loja de componentes informáticos.

Este projeto foi criado com o objetivo de praticar conceitos de programação aprendidos ao longo do curso, incluindo CRUD, pesquisa, ordenação, persistência de dados, expressões regulares, modularização e tratamento de erros.

O sistema funciona em linha de comandos (CLI) e permite gerir produtos, stock e informações relacionadas com fornecedores.

---

## Funcionalidades

- Adicionar produtos
- Editar produtos
- Eliminar produtos
- Listar produtos
- Pesquisa linear
- Pesquisa binária
- Ordenação de produtos
- Estatísticas do sistema
- Alertas automáticos de stock
- Exportação de produtos para ficheiro TXT
- Login simples de utilizador
- Guardar dados em JSON
- Carregamento automático dos dados

---

## Algoritmos Utilizados

### Pesquisa
- Pesquisa Linear
- Pesquisa Binária

### Ordenação
- Bubble Sort
- Selection Sort

---

## Validações Regex

Foram utilizadas expressões regulares para validar:
- Email
- Telefone
- Nome da empresa
- Password de login

Também foram utilizados:
- `match()`
- `group()`
- `span()`

---

## Persistência de Dados

O projeto utiliza ficheiros JSON para guardar os dados dos produtos.

Os dados:
- são carregados automaticamente ao iniciar
- podem ser guardados durante a utilização
- ficam persistentes após fechar o programa

---

## Estrutura do Projeto

```bash
ByteTech/
│
├── main.py
│
├── models/
│   └── produto.py
│
├── services/
│   ├── crud.py
│   ├── pesquisa.py
│   ├── ordenacao.py
│   ├── estatisticas.py
│   ├── json_manager.py
│   └── produtos_exemplo.py
│
├── data/
│   └── produtos.json
│
└── exports/
    └── produtos_exportados.txt
```

---

## Tecnologias Utilizadas

- Python 3
- JSON
- Regex
- Programação Modular
- Programação Orientada a Objetos (OOP)

---

## Como Executar

1. Abrir o projeto no Visual Studio Code
2. Executar o ficheiro:

```bash
python main.py
```

---

## Funcionalidades Extra

- Sistema de login
- Alertas automáticos de stock baixo
- Geração automática de emails para fornecedores
- Exportação de dados para TXT
- Produtos exemplo automático

---

## Objetivo do Projeto

O principal objetivo deste projeto foi aplicar conhecimentos de Python num sistema completo e funcional, praticando lógica de programação, organização de código e manipulação de dados.

---

## Autor

Pedro Gonçalves  
TPSI0226  
Projeto Final Python