# Gerenciador de Gastos CLI

## Descrição do Projeto
Muitas pessoas têm dificuldade em controlar seus gastos diários, o que pode gerar desorganização financeira, dificuldade de planejamento e até endividamento.

Este projeto foi desenvolvido com o objetivo de oferecer uma solução simples e prática para registrar, visualizar e gerenciar despesas diretamente pelo terminal.

## Problema real
O controle de gastos pessoais é uma dor comum na sociedade, pois muitas pessoas não possuem ferramentas simples e acessíveis para acompanhar suas despesas no dia a dia.

## Proposta da solução
A aplicação permite que o usuário registre seus gastos com nome, valor e categoria, além de listar, editar, remover, filtrar e calcular totais, facilitando o controle financeiro pessoal.

## Público-alvo
Pessoas que desejam organizar suas finanças pessoais de forma simples, utilizando uma aplicação leve e acessível via terminal.

## Funcionalidades
- Adicionar gasto com nome, valor e categoria
- Listar todos os gastos cadastrados
- Mostrar total geral de gastos
- Mostrar total por categoria
- Filtrar gastos por categoria
- Editar gastos existentes
- Remover gastos
- Salvamento automático em arquivo JSON

## Tecnologias utilizadas
- Python
- JSON (armazenamento de dados)
- Pytest (testes automatizados)
- Flake8 (linting)
- GitHub Actions (CI)

## Instalação

Clone o repositório:

```bash
git clone https://github.com/FilipePortela03/gerenciador-gastos-cli.git
```

Acesse a pasta do projeto:

```bash
cd gerenciador-gastos-cli
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
python src/app.py
```

## Como rodar os testes

```bash
pytest tests
```

## Como rodar o lint

```bash
flake8 src tests
```

## Estrutura do projeto

## Estrutura do projeto

```text
gerenciador-gastos-cli/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── app.py
├── tests/
│   └── test_app.py
├── .flake8
├── .gitignore
├── gastos.json
├── README.md
├── requirements.txt
└── VERSION
```

## Versão atual
1.0.0

## Autor
Filipe Portela Silva

## Repositório público
https://github.com/FilipePortela03/gerenciador-gastos-cli