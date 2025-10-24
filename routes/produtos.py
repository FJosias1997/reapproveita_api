import random
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import func

# Imports locais
from database.database_con import get_db
from models.all_models import ProdutosModel
from schemas.all_schemas import ProdutosSchema

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

@router.get("/", response_model=List[ProdutosSchema])
def buscar_produtos(
    query: Optional[str] = None, 
    db: Session = Depends(get_db)
):
    """
    Endpoint principal de busca de produtos.
    
    - Se 'query' for fornecido, filtra produtos por nome (ilike).
    - Se 'query' for omitido, retorna TODOS os produtos.
    
    Em ambos os casos, utiliza `joinedload` para carregar os dados do 
    supermercado associado e evitar N+1 queries.
    """
    consulta = db.query(ProdutosModel).options(
        joinedload(ProdutosModel.supermercado)
    )
    
    if query:
        consulta = consulta.filter(ProdutosModel.nome.ilike(f"%{query}%"))
    
    return consulta.all()

@router.get("/sugestoes", response_model=List[str])
def buscar_sugestoes_de_nome(
    query: str, 
    db: Session = Depends(get_db)
):
    """
    Endpoint para sugestões de auto-completar estilo Shopee.
    
    Busca produtos que contenham a query, extrai palavras-chave desses
    produtos e retorna uma lista aleatória de sugestões que 
    *começam* com a query.
    """
    
    nomes_tuplas = db.query(ProdutosModel.nome)\
                     .filter(ProdutosModel.nome.ilike(f"%{query}%"))\
                     .order_by(func.rand())\
                     .limit(50)\
                     .all()

    suggestion_set = set()
    query_lower = query.lower()

    for (nome,) in nomes_tuplas:
        nome_lower = nome.lower()
        
        if nome_lower.startswith(query_lower):
            suggestion_set.add(nome_lower)
            
        palavras = nome_lower.split()
        for palavra in palavras:
            if palavra.startswith(query_lower):
                suggestion_set.add(palavra)

    final_list = list(suggestion_set)
    random.shuffle(final_list)
    
    return final_list[:10]