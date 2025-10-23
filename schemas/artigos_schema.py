from pydantic import BaseModel,ConfigDict
from datetime import date


orm_config = ConfigDict(from_attributes=True)
class ArtigosSchema(BaseModel):
    id: int
    titulo: str
    descricao: str
    data_criacao: date
    autor: str
    image_url: str
    conteudo: str

    model_config = orm_config
