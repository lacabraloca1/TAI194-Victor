import jwt

def create_token(data:dict):
    token: str=jwt.encode(payload=data,key="secretkey",algorithm="hs256")
    return token
