from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="API de Gestión de Tareas",
    description="V.O.O",
    version="1.2"
)

Tareas = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI",
        "vencimiento": "14-02-24",
        "estado": "completada"
    },
    {
        "id": 2,
        "titulo": "Hacer ejercicio",
        "descripcion": "Ir al gimnasio por la mañana",
        "vencimiento": "15-02-24",
        "estado": "pendiente"
    },
    {
        "id": 3,
        "titulo": "Comprar víveres",
        "descripcion": "Ir al supermercado",
        "vencimiento": "16-02-24",
        "estado": "pendiente"
    },
    {
        "id": 4,
        "titulo": "Leer un libro",
        "descripcion": "Leer 'El Quijote'",
        "vencimiento": "17-02-24",
        "estado": "en progreso"
    },
    {
        "id": 5,
        "titulo": "Llamar a mamá",
        "descripcion": "Llamar a mamá para saber cómo está",
        "vencimiento": "18-02-24",
        "estado": "completada"
    },
]

# Ruta o Endpoint principal
@app.get("/", tags=["Tareas"])
def Home():
    return {"Hello": "World"}

# Endpoint para obtener todas las tareas
@app.get("/tareas", tags=["Obtener todas las tareas"])
def obtener_todas_tareas():
    return {"Tareas Registradas": Tareas}

# Endpoint para obtener una tarea específica por su ID
@app.get("/tareas/{id}", tags=["Obtener una tarea específica por su ID"])
def obtener_tarea_id(id: int):
    for t in Tareas:
        if t["id"] == id:
            return t
    raise HTTPException(status_code=404, detail="La tarea no existe")

# Endpoint para crear una nueva tarea
@app.post("/tareas/", tags=["Crear una nueva tarea"])
def insertar_tarea(tarea: dict):
    for t in Tareas:
        if t["id"] == tarea.get("id"):
            raise HTTPException(status_code=400, detail="La tarea ya existe")
    
    Tareas.append(tarea)
    return tarea


