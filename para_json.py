from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    pais: str

class UsuarioUpdate(BaseModel):
    nombre: str
    pais: str

class ListaCreate(BaseModel):
    nombre: str
class AgregarPelicula(BaseModel):
    pelicula_id: int