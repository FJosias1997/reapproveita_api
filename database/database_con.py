from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. ATUALIZE AQUI com suas credenciais do MySQL
# Formato: "mysql+mysqlconnector://USER:PASSWORD@HOST/DATABASE_NAME"
DATABASE_URL = "mysql+mysqlconnector://root:rootmysql@localhost/reapproveita_db"

# 2. Criar a "engine" de conexão
engine = create_engine(DATABASE_URL)

# 3. Criar uma "fábrica" de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Criar uma classe Base para nossos modelos ORM
#    Nossos modelos (tabelas) em models.py vão herdar desta classe.
Base = declarative_base()


# 5. Dependência: Gerenciador da Sessão do Banco
#    Função que será injetada em nossos endpoints para
#    abrir e fechar a conexão com o banco a cada requisição.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()