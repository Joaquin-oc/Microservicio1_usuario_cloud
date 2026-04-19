from pydantic import BaseModel
from enum import Enum

class Rol(str, Enum):
    admin = "admin"
    usuario = "usuario"

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    password: str
    pais: str

class UsuarioUpdate(BaseModel):
    nombre: str
    pais: str

class PeliculaCreate(BaseModel):
    titulo: str
    descripcion: str
    año: int
    genero: str