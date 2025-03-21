from pydantic import BaseModel, EmailStr, Field

class modelUsuario(BaseModel):  
    name: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios, min 1 max 85")
    age: int = Field(..., ge=1, le=99, description="Edad mínima 1, máxima 99")  
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.com$", description="Correo válido", example="usuario@example.com")  

class modelAuth(BaseModel):
    mail: EmailStr 
    passwd: str = Field(..., min_length=8, strip_whitespace=True, description="La contraseña es de mínimo 8 caracteres sin letras y espacios")