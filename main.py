import uvicorn
from fastapi import FastAPI
from sqlalchemy.sql import func
from sqlalchemy.exc import OperationalError
from database.database_con import engine, Base
from routes import produtos, supermercados, artigos

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Reapproveita API",
    description="API para o Hackathon de Saúde e Nutrição.",
    version="0.1.0"
)

if __name__ == "__main__":
    print("Iniciando servidor Uvicorn em http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

#Ao iniciar o servidor, este é o primeiro evento que deve ser executado.
#Ele vai verificar se o banco de dados está funcionando e está conectando.

@app.on_event("startup")
def check_db_connection():
    """
    Verifica a conexão com o banco de dados na inicialização do app.
    """
    try:
        with engine.connect() as conn:
            conn.execute(func.now()) 
        print("Conexão com o banco de dados bem-sucedida!")
    except OperationalError as e:
        print("ERRO: Falha ao conectar com o banco de dados.")
        print(f"Detalhes do erro: {e}")
    except Exception as e:
        print(f"ERRO inesperado ao conectar ao banco: {e}")


# --- Rotas(Endpoints)
app.include_router(produtos.router)
app.include_router(supermercados.router)
app.include_router(artigos.router)