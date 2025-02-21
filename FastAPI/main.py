from fastapi import FastAPI , HTTPException 
from typing import Optional , List
from pydantic import BaseModel

app = FastAPI(
    title="Mi primer APi ",
    description="Victor O.O",
    version="1.o.1"
)

class modelUsuario(BaseModel):
    id:int
    nombre:str
    edad:int
    correo:str

usuarios=[
    {"id":1,"nombre":"Victor","edad":20 ,"correo":"victor@gmail.com"},
    {"id":2,"nombre":"Oscar","edad":22 ,"correo":"oscar@gmail.com"},
    {"id":3,"nombre":"Juan","edad":23 ,"correo":"juan@gmail.com"},
    {"id":4,"nombre":"Pedro","edad":24,"correo":"pedro@gmail.com"},
    {"id":5,"nombre":"Maria","edad":25,"correo":"maria@gmail.com"},
]

#ruta o Endpoint
@app.get("/",tags=["Inicio"])
def Home():
    return {"Hello": "World"}

#Enpoint GET
@app.get("/todoUsuarios",response_model=List[modelUsuario],tags=["Operaciones CRUD"])
def leer():
    return usuarios 

#Enpoint POST
@app.post("/Usuarios/",response_model=modelUsuario,tags=["Operaciones CRUD"])
def insert(usuario:modelUsuario):
    for usr in usuarios:
        if usr["id"]== usuario.id:
            raise HTTPException(status_code=400,detail="El usuario ya existe")
    
    usuarios.append(usuario)
    return usuario

#EndPoint PUT
@app.put("/Usuarios/{id}",tags=["Operaciones CRUD"])
def actualizar(id:int ,usuarioactualiazdo:modelUsuario):
    for index , usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index]=usuarioactualiazdo.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=404,detail="El usuario no existe")

#EndPoint DELETE
@app.delete("/Usuarios/{id}",tags=["Operaciones CRUD"])
def eliminar(id:int):
    for usr in usuarios:
        if usr["id"]==id:
            usuarios.remove(usr)
            return {"Usuario Eliminado":usr}
    raise HTTPException(status_code=404,detail="Hijole no existe el usuario")

