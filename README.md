
## 🧠 QA Test Vision — Quality Analytics Dashboard

Dashboard interativo para centralizar, mensurar e visualizar métricas de qualidade do Super App, com foco em bugs, regressões e eficiência de testes por sprint.


## 📋 Intuito do Projeto

O QA Test Vision foi criado para:

Consolidar dados de defeitos encontrados, corrigidos e despriorizados.

Oferecer insights visuais para Sprint Review.

Acompanhar tendências de qualidade ao longo das releases.

Melhorar a eficiência do processo regressivo e a confiabilidade das entregas.


## 🧩 Objetivos Específicos

Automatizar a coleta de dados sobre bugs por sprint.

Categorizar bugs por status: corrigido, pendente, despriorizado, transferido.

Gerar relatórios HTML interativos com gráficos dinâmicos.

Integrar com GitLab CI/CD para execução e publicação automática.


## 🐍 Stack Tecnológica

Linguagem: Python 3.x

Web/App: Plotly Dash

Visualização: Plotly Express

Dados: Pandas

Pipeline: GitLab CI/CD

Versionamento: Git + GitLab/GitHub


## 🏗️ Estrutura do Projeto
QA-TEST-VISION
└── bug_report/

    ├── data/
    │   ├── bugs_sprint.csv        # Dados brutos da sprint
    │   └── bugs_history.csv       # Histórico consolidado
    │
    ├── src/
    │   ├── __init__.py
    │   ├── data_processing.py     # Tratamento e análise dos dados
    │   ├── charts.py              # Funções de gráficos (Plotly)
    │   ├── dashboard.py           # Layout e callbacks do Dash
    │   └── utils.py               # Funções auxiliares
    │
    ├── tests/
    │   ├── test_data_processing.py
    │   └── test_dashboard.py
    │
    ├── .gitlab-ci.yml
    ├── requirements.txt
    ├── README.md
    └── app.py                     # Arquivo principal do dashboard


## ⚙️ Instalação e Execução Local
Pré-requisitos

Python 3.10+

Git

(Opcional) Ambiente virtual

## Passos para execução

# Clonar o repositório

git clone https://github.com/RafaelFossali/QA-Test-Vision---Quality-Analytics-Dashboard.git
cd QA-Test-Vision---Quality-Analytics-Dashboard

# Criar e ativar o ambiente virtual
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar o dashboard
python app.py


Acesse o dashboard em:
👉 http://localhost:8050/

## 📚 Dados de Entrada
data/bugs_sprint.csv

- Campos recomendados:

- id

- titulo

- status

- origem

- responsavel

- created_at

- closed_at

- sprint

- data/bugs_history.csv

- Mesmo schema do arquivo acima

- Consolidado de várias sprints


## Boas práticas

- Status padronizados: corrigido, pendente, despriorizado, transferido

- Datas no formato ISO-8601

- Evitar valores nulos em colunas-chave

## ▶️ Uso

Para executar localmente:

python app.py

Funcionalidades

Filtros por sprint, status e origem

Gráficos dinâmicos e responsivos

Tabela interativa com busca e ordenação

Exportação de relatório HTML estático


## 🧪 Testes

Executar os testes:

pytest --maxfail=1 --disable-warnings -q

Estratégia de testes

Testes unitários para funções de processamento

Smoke tests para componentes do Dash


##🔁 Integração com GitLab CI/CD

Exemplo de .gitlab-ci.yml:

stages:
  - test
  - report

variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip

test_job:
  stage: test
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - pytest --maxfail=1 --disable-warnings -q

generate_report:
  stage: report
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - python app.py
  artifacts:
    paths:
      - reports/
    expire_in: 1 week


## 📊 Visualizações Disponíveis

Barras: bugs por status

Pizza: proporção por origem

Linha: evolução por sprint

Tabela: com filtros e ordenação


## 🧰 Scripts úteis (Makefile opcional)
install:
	pip install -r requirements.txt

test:
	pytest --maxfail=1 --disable-warnings -q

run:
	python app.py


## 🗺️ Roadmap

Coleta automática de dados via API do GitLab

Persistência em banco local

Métricas de lead time e cycle time

Exportação do dashboard para PDF

## 👤 Autor

Rafael Fossali
QA Engineer • Automação & Analytics de Qualidade
