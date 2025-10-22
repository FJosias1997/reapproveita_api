from pydantic import BaseModel

class CategoriaProdutosSchema(BaseModel):
    id: int
    categoria: str

    class Config:
        from_attributes = True