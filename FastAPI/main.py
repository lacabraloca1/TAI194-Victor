from fastapi import FastAPI , HTTPException 
from typing import Optional

app = FastAPI(
    title="Mi primer APi ",
    description="Victor O.O",
    version="1.o.1"
)

usuarios=[
    {"id":1,"nombre":"Victor","edad":20},
    {"id":2,"nombre":"Oscar","edad":22},
    {"id":3,"nombre":"Juan","edad":23},
    {"id":4,"nombre":"Pedro","edad":24},
    {"id":5,"nombre":"Maria","edad":25},
]

#ruta o Endpoint
@app.get("/",tags=["Inicio"])
def Home():
    return {"Hello": "World"}

#Enpoint GET
@app.get("/todoUsuarios",tags=["Operaciones CRUD"])
def leer():
    return {"Usuarios Registrados ": usuarios }

#Enpoint POST
@app.post("/Usuarios/",tags=["Operaciones CRUD"])
def insert(usuario:dict):
    for usr in usuarios:
        if usr["id"]== usuario.get("id"):
            raise HTTPException(status_code=400,detail="El usuario ya existe")
    
    usuarios.append(usuario)
    return usuario

#EndPoint PUT
@app.put("/Usuarios/{id}",tags=["Operaciones CRUD"])
def actualizar(id:int,usuarioactualiazdo:dict):
    for index,usr in enumerate(usuarios):
        if usr["id"]==id:
            usr[index].update(usuarioactualiazdo)
            return usuarios[index]
    raise HTTPException(status_code=404,detail="El usuario no existe")

#EndPoint DELETE
@app.delete("/Usuarios/{id}",tags=["Operaciones CRUD"])
def eliminar(id:int):
    for usr in usuarios:
        if usr["id"]==id:
            usuarios.remove(usr)
            return {"Usuario Eliminado":usr}
    raise HTTPException(status_code=404,detail="El usuario no existe")

