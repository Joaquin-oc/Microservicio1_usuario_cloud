from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum

class Rol(enum.Enum):
    admin = "admin"
    usuario = "usuario"

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(255))
    pais = Column(String(50))
    fecha_registro = Column(DateTime, default=datetime.now)
    rol = Column(Enum(Rol), default=Rol.usuario)

    peliculas_vistas = relationship("PeliculaVista", back_populates="usuario", cascade="all, delete")

class PeliculaVista(Base):
    __tablename__ = "peliculas_vistas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    pelicula_id = Column(Integer)
    fecha_vista = Column(DateTime, default=datetime.now)

    usuario = relationship("Usuario", back_populates="peliculas_vistas")

class Pelicula(Base):
    __tablename__ = "peliculas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200))
    descripcion = Column(String(500))
    año = Column(Integer)
    genero = Column(String(100))