from pydantic import BaseModel, Field

class modelCarro(BaseModel): 
    modelo: str = Field(..., min_length=3 ,max_length=25, description="El modelo debe de ser de 3 a 25 caracteres")
    placa: str = Field(..., max_length=10, description="La placa debe de ser de 10 digitos maximo")
    año: int = Field(..., min=4, min_length=4, max_length=4, description="El año debe ser de 4 digitos")  
