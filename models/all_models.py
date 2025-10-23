# /models/all_models.py

# Apenas importe os módulos.
# Quando o Python ler isto, ele vai executar cada arquivo.
# Ao executar cada arquivo, as classes (ProdutoDB, CategoriaProdutosDB, etc.)
# irão se registrar automaticamente na 'Base' que elas importaram do 'database.py'.

from . import produtos_model
from . import categoria_produtos_model
from . import supermercados_model
from . import artigos_model

Produtos = produtos_model.Produtos
CategoriaProdutos = categoria_produtos_model.CategoriaProdutos
Supermercados = supermercados_model.Supermercados
Artigos = artigos_model.Artigos