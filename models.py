from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Pruducto(Base):
    __tablename__="productos"

    id=Column(Integer, primary_key=True, index=True)
    nombre=Column(String, index=True)
    precio=Column(Float)
    stock=Column(Integer)

class Usuario(Base):
    __tablename__="suarios" 
    id=Column(Integer, primary_key=True, index=True)
    nombre=Column(String, index=True)
    precio=Column(Float)
    stock=Column(Integer)

class Pedido(Base):
    __tablaname__="pedidos"

    id=Column(Integer, primary_key=True, index=True)

    usuario_id=Column(String, ForeignKey("usuarios.id"))    
    total=Column(Float)

    usuario=relationship("Usuario")

























