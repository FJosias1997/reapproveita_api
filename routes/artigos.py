from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Imports locais
from database.database_con import get_db
from models.all_models import ArtigosModel
from schemas.all_schemas import ArtigosSchema

router = APIRouter(
    prefix="/artigos",
    tags=["Artigos"]
)

@router.get("/", response_model=List[ArtigosSchema])
def listar_artigos(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os artigos cadastrados no banco de dados.
    """
    artigos = db.query(ArtigosModel).all()
    return artigos