from sqlalchemy import Column, ForeignKey, Integer, String, Float
from database.database_con import Base  # Importamos a Base do nosso arquivo database.py
from sqlalchemy.orm import relationship

# Modelo do SQLAlchemy (Representa a tabela 'produtos' no Python)
class Produtos(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo = Column(Integer)
    supermercado_id = Column(Integer, ForeignKey("supermercados.id"))
    categoria_id = Column(Integer,ForeignKey("categoria_produtos.id"), index=True)
    preco = Column(Float)
    nome = Column(String(100), index=True)
    descricao_produto = Column(String(10000))
    image_url = Column(String)

# Este é o 'link' mágico do ORM. 
    # 'back_populates' deve corresponder ao nome do relationship em Supermercados
    supermercado = relationship("Supermercados", back_populates="produtos")
