from fastapi import FastAPI   # type: ignore

app = FastAPI()

#ruta o Endpoint
@app.get("/")
def home():
    return {"Hello": "World"}