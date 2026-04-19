from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario, Rol
import hashlib

security = HTTPBasic()

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def get_usuario_actual(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == credentials.username).first()
    if not usuario or usuario.password != hash_password(credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña tan mal",
            headers={"WWW-Authenticate": "Basic"}
        )
    return usuario

def solo_admin(usuario: Usuario = Depends(get_usuario_actual)):
    if usuario.rol != Rol.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="tu no puedes hacer esto"
        )
    return usuario