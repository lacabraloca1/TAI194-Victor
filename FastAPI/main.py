from fastapi import FastAPI, HTTPException
from typing import List
from models import modelUsuario

app = FastAPI(
    title="Mi primer API",
    description="Victor O.O",
    version="1.0.1"
)

# Lista de usuarios simulando una BD
usuarios = [
    {"id": 1, "nombre": "Victor", "edad": 20, "correo": "victor@gmail.com"},
    {"id": 2, "nombre": "Oscar", "edad": 22, "correo": "oscar@gmail.com"},
    {"id": 3, "nombre": "Juan", "edad": 23, "correo": "juan@gmail.com"},
    {"id": 4, "nombre": "Pedro", "edad": 24, "correo": "pedro@gmail.com"},
    {"id": 5, "nombre": "Maria", "edad": 25, "correo": "maria@gmail.com"},
]

# Ruta de inicio
@app.get("/", tags=["Inicio"])
def Home():
    return {"message": "Bienvenido a mi API"}

# Endpoint GET - Obtener todos los usuarios
@app.get("/todoUsuarios", response_model=List[modelUsuario], tags=["Operaciones CRUD"])
def leer():
    return [modelUsuario(**usr) for usr in usuarios]  # Convertir a modelo Pydantic

# Endpoint POST - Insertar usuario
@app.post("/Usuarios/", response_model=modelUsuario, tags=["Operaciones CRUD"], responses={
    400: {"description": "El usuario ya existe"}
})
def insert(usuario: modelUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    usuarios.append(usuario.model_dump())  # Convertir a diccionario antes de agregar
    return usuario

# Endpoint PUT - Actualizar usuario
@app.put("/Usuarios/{id}", tags=["Operaciones CRUD"], responses={
    404: {"description": "Usuario no encontrado"}
})
def actualizar(id: int, usuario_actualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuario_actualizado.model_dump()  # Convertir a dict
            return usuario_actualizado
    raise HTTPException(status_code=404, detail="El usuario no existe")

# Endpoint DELETE - Eliminar usuario
@app.delete("/Usuarios/{id}", tags=["Operaciones CRUD"], responses={
    404: {"description": "Usuario no encontrado"}
})
def eliminar(id: int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"message": "Usuario eliminado", "usuario": usr}
    raise HTTPException(status_code=404, detail="El usuario no existe")
