from modelsPydantic import modelUsuario
from DB.conexion import Session
from models.modelsDB import User
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException , APIRouter

routerUsuario = APIRouter()

# Endpoint GET - Obtener todos los usuarios
@routerUsuario.get("/todoUsuarios", tags=["Operaciones CRUD"])
def leer():
    db = Session()
    try:
        consulta=db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "No fue Posible la Consulta ", "error": str(e)})
    finally:
        db.close()

#Encontrar usuario por id
@routerUsuario.get("/Usuarios/{id}", tags=["Operaciones CRUD"], responses={
    404: {"description": "Usuario no encontrado"}
})
def leeruno(id: int):
    db = Session()
    try:
        consulta1 = db.query(User).filter(User.id == id).first()
        if not consulta1:
            return JSONResponse(status_code=404, content={"mensaje": "usuario no encontrado"})

        return JSONResponse(content=jsonable_encoder(consulta1))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar usuario: {str(e)}")
    finally:
        db.close()

# Endpoint POST - Insertar usuario
@routerUsuario.post("/Usuarios/", response_model=modelUsuario, tags=["Operaciones CRUD"], responses={
    400: {"description": "El usuario ya existe"}
})
def guardar(usuario: modelUsuario):
    db = Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201, content={"message": "Usuario creado", "usuario": usuario.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al crear usuario", "error": str(e)})
    finally:
        db.close()  

# Endpoint PUT - Actualizar usuario
@routerUsuario.put("/Usuarios/{id}", tags=["Operaciones CRUD"], responses={
    404: {"description": "Usuario no encontrado"},
    500: {"description": "Error al actualizar usuario"}
})
def actualizar(id: int, usuario_actualizado: modelUsuario):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).update(usuario_actualizado.model_dump())
        if consulta == 0:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        db.commit()
        return JSONResponse(content={"message": "Usuario actualizado", "usuario": usuario_actualizado.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al actualizar usuario", "error": str(e)})
    finally:
        db.close()

# Endpoint DELETE - Eliminar usuario
@routerUsuario.delete("/Usuarios/{id}", tags=["Operaciones CRUD"], responses={
    404: {"description": "Usuario no encontrado"}
})
def eliminar(id: int):
    db = Session()
    try:
        consulta = db.query(User).filter(User.id == id).first()
        if not consulta:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        db.delete(consulta)
        db.commit()
        return JSONResponse(content={"message": "Usuario eliminado"})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "Error al eliminar usuario", "error": str(e)})
    finally:
        db.close()
