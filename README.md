# Controle de Ponto

Aplicação simples de controle de ponto feita em Python com [Flet](https://flet.dev/). A interface exibe um relógio em tempo real e permite registrar o horário atual ao clicar no botão **Marcar Ponto**.

## Captura de Tela

![Tela do projeto Controle de Ponto desktop](./screenshotDesktop.png)
![Tela do projeto Controle de Ponto smartPhone](./screenshotSmartPhone.jpeg)

## Funcionalidades

- Exibe a hora atual atualizada a cada segundo.
- Registra data e hora do ponto marcado.
- Interface gráfica simples e centralizada.

## Tecnologias

- Python 3.14 ou superior
- Flet
- uv, opcional, para gerenciar dependências e executar o projeto

## Como Executar

### Usando uv

Instale as dependências:

```bash
uv sync
```

Execute a aplicação:

```bash
uv run python main.py
```

### Usando pip

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows, ative com:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install flet
```

Execute a aplicação:

```bash
python main.py
```

## Estrutura do Projeto

```text
.
├── main.py          # Código principal da aplicação
├── pyproject.toml   # Configuração do projeto e dependências
├── uv.lock          # Arquivo de lock das dependências
└── README.md        # Documentação do projeto
```

## Como Funciona

O arquivo `main.py` cria uma página Flet com:

- título da aplicação;
- texto com a hora atual;
- botão para marcar o ponto;
- mensagem de status com o horário registrado.

O relógio é atualizado por uma tarefa assíncrona que roda a cada segundo. Ao clicar em **Marcar Ponto**, a aplicação captura a data e hora atual e mostra o registro na tela.
