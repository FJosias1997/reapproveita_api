from sqlalchemy import Column, Integer, String, Float
from database import Base  # Importamos a Base do nosso arquivo database.py
from sqlalchemy.orm import relationship

# Modelo do SQLAlchemy (Representa a tabela 'produtos' no Python)
class Supermercados(Base):
    __tablename__ = "supermercados"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(20), index=True)
    image_url = Column(String)

    # Este relationship informa ao SQLAlchemy que 'produtos' estão ligados a esta classe
    produtos = relationship("Produtos", back_populates="supermercado")