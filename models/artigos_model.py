from sqlalchemy import Column, Integer, String, Date
from database.database_con import Base  # Importamos a Base do nosso arquivo database.py
from sqlalchemy.orm import relationship

# Modelo do SQLAlchemy (Representa a tabela 'produtos' no Python)
class Artigos(Base):
    __tablename__ = "artigos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(100))
    descricao = Column(String(100))
    data_criacao = Column(Date)
    autor = Column(String(50))
    image_url = Column(String(500))
    conteudo = Column(String())

#     id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
# titulo varchar(100),
# descricao varchar(100),
# data_criacao date,
# autor varchar(50),
# image_url varchar(500),
# conteudo text

 