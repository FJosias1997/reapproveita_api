## Reapproveita API 🥦

Este é o repositório do backend (API) para o aplicativo Reapproveita. A plataforma conecta supermercados a consumidores, ofertando produtos próximos da data de validade com 50% de desconto, com o objetivo de combater o desperdício de alimentos.

Este projeto fornece os endpoints RESTful que o aplicativo mobile em Flutter (<-- Sugiro linkar seu app aqui) consome para buscar e exibir produtos, supermercados, etc.

## 🎯 Contexto do Projeto

Esta API foi desenvolvida como parte de um Hackathon de Saúde e Nutrição, servindo como a prova de conceito do backend necessário para suportar as funcionalidades do aplicativo.

⚠️ Aviso: Este é um projeto de protótipo e continua em desenvolvimento.

## 🛠️ Tecnologias Principais

    Python 3.10+: Linguagem de programação base.

    FastAPI: Framework web moderno e de alta performance para construir as APIs.

    SQLAlchemy: ORM (Object-Relational Mapper) para interagir com o banco de dados usando Python.

    Pydantic: Usado pelo FastAPI para validação de dados e definição de Schemas.

    MySQL: Banco de dados relacional para armazenar os dados.

    Uvicorn: Servidor ASGI (Asynchronous Server Gateway Interface) para executar o FastAPI.

## 🗂️ Estrutura do Projeto

O código-fonte da API está organizado de forma a separar responsabilidades, seguindo as convenções do FastAPI:

```
/
├── models/             # Define as tabelas do banco (Models SQLAlchemy)
│   ├── all_models.py
│   ├── categoria_produtos_model.py
│   └── ...
│
├── schemas/            # Define os formatos de dados de entrada/saída (Schemas Pydantic)
│   ├── all_schemas.py
│   ├── categoria_produtos_schema.py
│   └── ...
│
├── database.py         # Configuração da conexão com o banco (SQLAlchemy Engine, Session, Base)
├── db.sql              # Script SQL com dados de teste para popular o banco
├── main.py             # Ponto de entrada da aplicação FastAPI, onde os endpoints são definidos
├── requirements.txt    # Lista de dependências Python (Crie este arquivo!)
└── LICENSE             # Licença do projeto
```

## 🚀 Guia de Instalação e Execução

Siga estes passos para configurar e executar a API localmente.

### Pré-requisitos

    Python 3.10 ou superior

    Um servidor MySQL (Ex: XAMPP, WAMP, MAMP ou a instalação oficial do MySQL Community Server)

#### 1. Clone o Repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

#### 2. Crie e Ative um Ambiente Virtual

É uma boa prática isolar as dependências do seu projeto.

```bash
# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
.\venv\Scripts\activate
```

#### 3. Instale as Dependências
requirements.txt
```
fastapi
uvicorn[standard]
sqlalchemy
pydantic
mysqlclient
```

Comando para instalar:
```pip3 install -r requirements.txt```

#### 4. Configure o Banco de Dados (MySQL)

Passo 4.1: Crie o Banco de Dados Acesse o seu cliente MySQL (linha de comando, DBeaver, etc.) e crie o banco de dados:

```
CREATE DATABASE reapproveita_db;
```
Passo 4.2: Configure a Conexão Abra o arquivo database.py. Você precisará editar a variável DATABASE_URL para apontar para o seu banco de dados MySQL.

Exemplo de string de conexão no database.py:

```
# (Exemplo - ajuste com seu usuário e senha)
USUARIO_DB = "root"
SENHA_DB = "sua_senha_do_mysql"
HOST_DB = "localhost"
NOME_DB = "reapproveita_db"

DATABASE_URL = f"mysql+mysqlclient://{USUARIO_DB}:{SENHA_DB}@{HOST_DB}/{NOME_DB}"
```

Passo 4.3: Importe os Dados de Teste Execute o script db.sql fornecido para popular seu banco com os dados iniciais.

```
# Execute este comando no seu terminal
mysql -u SEU_USUARIO_MYSQL -p reapproveita_db < db.sql
```

### 5. Execute a API

Com o banco configurado e as dependências instaladas, inicie o servidor FastAPI:
```
python3 main.py
```

OU (forma mais comum):

```
uvicorn main:app --reload
```

A API estará disponível em http://127.0.0.1:8000.

🔌 Endpoints da API

Você pode acessar a documentação interativa (Swagger UI) gerada automaticamente pelo FastAPI em:

```
http://127.0.0.1:8000/docs
```

### Principais Endpoints Disponíveis:

    GET /produtos

        Retorna uma lista de todos os produtos, com os dados do supermercado associado.

        Suporta filtragem por nome: GET /produtos?query=banana

    GET /produtos/sugestoes

        Retorna uma lista de até 10 sugestões de texto para auto-completar a busca.

        Exige uma query: GET /produtos/sugestoes?query=a

    GET /supermercados

        Retorna uma lista de todos os supermercados cadastrados.

## 📄 Licença

Este projeto está licenciado sob os termos do arquivo LICENSE.

