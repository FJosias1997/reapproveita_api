from sqlalchemy import Column, Integer, String, Float
from database import Base  # Importamos a Base do nosso arquivo database.py
from sqlalchemy.orm import relationship

# Modelo do SQLAlchemy (Representa a tabela 'produtos' no Python)
class CategoriaProdutos(Base):
    __tablename__ = "categoria_produtos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    categoria = Column(String(20), index=True)