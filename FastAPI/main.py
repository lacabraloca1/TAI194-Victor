from fastapi import FastAPI   # type: ignore
from typing import Optional

app = FastAPI(
    title="Mi primer APi ",
    description="Victor O O",
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
#Endpoint promedio
@app.get("/promedio",tags=["MI Calificación TAI"])
def Promeido():
    return 10.5
#Endpoint con prametro obligatorio
@app.get("/usuario/{id}",tags=["Parametro Obligatorio"])
def Consulta_Usuario(id: int):
    #caso de busqueda ficticia en bd
    return {"Se encontro el usuario": id}

@app.get("/usuario/",tags=["Parametro Opcional"])
def Consulta_Usuario2(id: Optional[int]=None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"]==id:
                return {"mensaje":"Usuario encontrado","usuario es":usuario}
        return {"mensaje":f"No se Encontro el id: {id}"}
    return{"mensaje":"No se proporciono un usuario"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:    
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}