# --- 1. Imports da Biblioteca Padrão ---
import random
from typing import List, Optional

# --- 2. Imports de Terceiros (Libs) ---
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.sql import func
from sqlalchemy.exc import OperationalError

# --- 3. Imports Locais do Projeto ---
from database import engine, Base, get_db
import models.all_models as models
import schemas.all_schemas as schemas

# --- 4. Inicialização do App e Banco de Dados ---
# Cria as tabelas (se não existirem)
Base.metadata.create_all(bind=engine)

# Cria a instância principal do FastAPI
app = FastAPI(
    title="Reapproveita API",
    description="API para o Hackathon de Saúde e Nutrição.",
    version="0.1.0"
)

# --- 5. Eventos de Inicialização (Startup) ---

@app.on_event("startup")
def check_db_connection():
    """
    Verifica a conexão com o banco de dados na inicialização do app.
    """
    print("Tentando conectar ao banco de dados...")
    try:
        # Tenta estabelecer uma conexão simples
        with engine.connect() as conn:
            conn.execute(func.now()) # Executa uma query simples
        print("Conexão com o banco de dados bem-sucedida!")
    except OperationalError as e:
        print("ERRO: Falha ao conectar com o banco de dados.")
        print(f"Detalhes do erro: {e}")
    except Exception as e:
        print(f"ERRO inesperado ao conectar ao banco: {e}")

# --- 6. Endpoints da API ---

# --- Recursos: Produtos ---

@app.get("/produtos", response_model=List[schemas.ProdutosSchema], tags=["Produtos"])
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
    # Inicia a consulta já otimizada com joinedload
    consulta = db.query(models.Produtos).options(
        joinedload(models.Produtos.supermercado)
    )
    
    # Aplica o filtro APENAS se a query foi fornecida
    if query:
        consulta = consulta.filter(models.Produtos.nome.ilike(f"%{query}%"))
    
    # Executa a consulta (com ou sem filtro) e retorna os resultados
    return consulta.all()


@app.get("/produtos/sugestoes", response_model=List[str], tags=["Produtos"])
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
    
    # 1. Busca um "pool" aleatório de produtos no DB que contenham a query.
    #    (Usamos func.rand() para MySQL; seria func.random() para PostgreSQL)
    nomes_tuplas = db.query(models.Produtos.nome)\
                     .filter(models.Produtos.nome.ilike(f"%{query}%"))\
                     .order_by(func.rand())\
                     .limit(50)\
                     .all()

    # 2. Processa os nomes em Python para extrair as sugestões
    suggestion_set = set() # Usamos um "set" para evitar duplicatas
    query_lower = query.lower()

    for (nome,) in nomes_tuplas:
        nome_lower = nome.lower()
        
        # 3. Adiciona o nome completo (ex: "banana prata")
        #    Verifica se ele realmente começa com a query
        if nome_lower.startswith(query_lower):
            suggestion_set.add(nome_lower)
            
        # 4. Adiciona as palavras individuais (ex: "banana", "prata")
        palavras = nome_lower.split()
        for palavra in palavras:
            if palavra.startswith(query_lower):
                suggestion_set.add(palavra)

    # 5. Converte o set de volta para uma lista
    final_list = list(suggestion_set)
    
    # 6. Embaralha a lista final de sugestões
    random.shuffle(final_list)
    
    # 7. Retorna as 10 primeiras
    return final_list[:10]


# --- Recursos: Supermercados ---

@app.get("/supermercados", response_model=List[schemas.SupermercadosSchema], tags=["Supermercados"])
def listar_supermercados(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os supermercados cadastrados no banco de dados.
    """
    supermercados = db.query(models.Supermercados).all()
    return supermercados

# --- 7. Ponto de Entrada (Main) ---
# (Deve ficar no final do arquivo)

if __name__ == "__main__":
    print("Iniciando servidor Uvicorn em http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)