from pydantic import BaseModel
from typing import List, Optional


class ProductoBase(BaseModel):
    nombre:str
    precio:float
    stock:int


# Esquema para Producto
class ProductoCreate(ProductoBase):
    pass

class ProductoResponde(ProductoBase):
    id: int


    class Config:
        from_attributes=True

# Esquema para Usuario
class UsuarioBase(BaseModel):
    nomre: str
    email:str

class UsuarioCreate(UsuarioBase):
    pass    

class UsuarioCreate(UsuarioBase):
    id: int

    class Config:
        from_attributes=True

# Esquema para Pedido
class PedidioBase(BaseModel):
    usuario_id: int
    total: float

class PedidoCreate(PedidioBase):
    pass

class PedidoREsponse(PedidioBase):
    id: int

    class Config:
        from_attribute=True



