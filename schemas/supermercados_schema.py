from pydantic import BaseModel,ConfigDict


orm_config = ConfigDict(from_attributes=True)
class SupermercadosSchema(BaseModel):
    id: int
    nome: str
    image_url: str

    model_config = orm_config
