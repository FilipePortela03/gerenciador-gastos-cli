# Gerenciador de Gastos CLI

## Descrição do Projeto
Muitas pessoas têm dificuldade em controlar seus gastos diários, o que pode gerar desorganização financeira, dificuldade de planejamento e até endividamento.

Este projeto foi desenvolvido com o objetivo de oferecer uma solução simples e prática para registrar, visualizar e gerenciar despesas diretamente pelo terminal.

## Problema real
O controle de gastos pessoais é uma dor comum na sociedade, pois muitas pessoas não possuem ferramentas simples e acessíveis para acompanhar suas despesas no dia a dia.

## Proposta da solução
A aplicação permite que o usuário registre seus gastos com nome, valor e categoria, além de listar, editar, remover, filtrar e calcular totais, facilitando o controle financeiro pessoal.

Agora o sistema também permite registrar gastos internacionais em dólar (USD), realizando automaticamente a conversão para real (BRL) utilizando uma API pública de cotação.

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
- Adicionar gastos internacionais com conversão automática de USD para BRL
- Integração com API pública de cotação de moedas

## Tecnologias utilizadas
- Python
- JSON (armazenamento de dados)
- Requests (requisições HTTP)
- Pytest (testes automatizados)
- Flake8 (linting)
- GitHub Actions (CI)
- API AwesomeAPI (cotação de moedas)

## Instalação

Clone o repositório:

```bash
git clone https://github.com/FilipePortela03/gerenciador-gastos-cli.git
```

## Acesse a pasta do projeto:

```bash
cd gerenciador-gastos-cli
```

## Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
python src/app.py
```

## Integração com API

O projeto utiliza a AwesomeAPI para buscar a cotação atual do dólar em tempo real.

API utilizada:
https://economia.awesomeapi.com.br/json/last/USD-BRL

## Como rodar os testes

```bash
pytest tests
```

## Como rodar o lint

```bash
flake8 src tests
```

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
2.0.0

## Autor
Filipe Portela Silva

## Repositório público
https://github.com/FilipePortela03/gerenciador-gastos-cli