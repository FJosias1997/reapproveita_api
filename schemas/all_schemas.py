from pydantic import BaseModel

# Modelo do Pydantic (Representa o JSON que vamos enviar/receber)
# Isso garante que a saída da API tenha este formato.


from . import categoria_produtos_schema
from . import produtos_schema
from . import supermercados_schema

ProdutosSchema = produtos_schema.ProdutosSchema
CategoriaProdutosSchema = categoria_produtos_schema.CategoriaProdutosSchema
SupermercadosSchema = supermercados_schema.SupermercadosSchema