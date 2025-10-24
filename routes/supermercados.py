from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# Imports locais
from database.database_con import get_db
from models.all_models import SupermercadosModel
from schemas.all_schemas import SupermercadosSchema

router = APIRouter(
    prefix="/supermercados",
    tags=["Supermercados"]
)

@router.get("/", response_model=List[SupermercadosSchema])
def listar_supermercados(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os supermercados cadastrados no banco de dados.
    """
    supermercados = db.query(SupermercadosModel).all()
    return supermercados