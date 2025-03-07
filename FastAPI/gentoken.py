import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException
from datetime import datetime, timedelta

# En un entorno de producción se recomienda obtener la clave desde variables de entorno o un gestor seguro.
SECRET_KEY = "secretkey"

def create_token(data: dict):
    # Se establece la expiración del token (por ejemplo, 1 hora a partir de ahora)
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload = data.copy()
    payload["exp"] = expiration
    token: str = jwt.encode(payload=payload, key=SECRET_KEY, algorithm="HS256")
    return token

def validateToken(token: str):
    try:
        data: dict = jwt.decode(token, key=SECRET_KEY, algorithms=["HS256"])
        return data  # Se retorna el diccionario decodificado
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token Expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token no Autorizado")
