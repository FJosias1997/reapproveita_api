from pydantic import BaseModel,ConfigDict

from .supermercados_schema import SupermercadosSchema

# Modelo do Pydantic (Representa o JSON que vamos enviar/receber)
# Isso garante que a saída da API tenha este formato.

orm_config = ConfigDict(from_attributes=True)

class ProdutosSchema(BaseModel):
    id: int
    codigo: int
    supermercado_id: int
    categoria_id: int
    nome: str
    preco: float
    descricao_produto: str
    image_url: str
    supermercado: SupermercadosSchema

    model_config = orm_config # <-- Adicionar isto