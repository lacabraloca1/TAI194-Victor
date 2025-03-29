from modelsPydantic import modelAuth
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from gentoken import create_token

routerauth = APIRouter()

# Endpoint para generar token
@routerauth.post("/auth", tags=["Autenticacion"])
def auth(credenciales: modelAuth):
    if credenciales.mail == "victor@gmail.com" and credenciales.passwd == " ":
        token: str = create_token(credenciales.model_dump())
        print(token)
        return JSONResponse(content={"token": token})
    else:
        return {"Aviso": "Usuario no cuenta con permiso"}

