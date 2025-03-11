from typing import List
from fastapi import FastAPI , HTTPException # type: ignore
from models import modelCarro

app = FastAPI()
Carros=[
    {"modelo":"Chevrolet","placa":"HGDUS5","año":2020},
    {"modelo":"Ford","placa":"ZCOPJI","año":2012},
]


@app.get("/todoCarros", response_model=List[modelCarro], tags=["Operaciones CRUD"])
def leer():
    return [modelCarro(**usr) for usr in Carros]


@app.post("/AgregarCarro/", response_model = modelCarro, tags=["Post carro"], responses={
    400: {"description": "El vehiculo ya existe"}
})
def insertar_carro(carro: modelCarro):
    for car in Carros:
        if car["placa"] == carro.placa:
            raise HTTPException(status_code=400, detail="El carro ya existe")
    
    Carros.append(carro.model_dump())  
    return carro


@app.delete("/Carro/{placa}", tags=["Eliminar un carro"], responses={
    404: {"description": "Vehiculo no encontrado"}
})
def eliminar_carro(placa: str):
    for t in Carros:
        if t["placa"] == placa:
            Carros.remove(t)
            return {"Vehiculo Eliminado": t}
    raise HTTPException(status_code=404, detail="El vehiculo no existe")