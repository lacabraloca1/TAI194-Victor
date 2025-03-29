from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerauth

app = FastAPI(
    title="Api Voo",
    description="Victor",
    version="2.0"
)
Base.metadata.create_all(bind=engine)

# Ruta de inicio
@app.get("/", tags=["Inicio"])
def Home():
    return {"message": "Bienvenido a mi API"}

app.include_router(routerUsuario)
app.include_router(routerauth)