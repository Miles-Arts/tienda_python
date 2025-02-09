from sqlalchemy.orm import Session
import models,  schemas

# 🟢 Crear un producto
def create_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto=models.Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresch(db_producto)
    return db_producto

# 🔵 Obtener todos los productos
def get_productos(db:Session):
    return db.query(models.Pruducto).all()

# 🔵 Obtener un producto por ID
def get_producto(db: Session, producto_id: int ):
    return db.query(models.Pruducto).filter(models.Pruducto.id == producto_id).first()

# 🔴 Eliminar un producto por ID
def delete_producto(db: Session, producto_id: int):
    db_producto=get_producto(db, producto_id)
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto    

# 🟠 Actualizar un producto

def update_producto(db: Session, producto_id: int, producto_date: schemas.ProductoCreate):
    db_producto=get_producto(db, producto_id)
    if db_producto:
        for key, value in producto_date.model_dump().items():
            setattr(db_producto, key, value)
        db.commit()
        db.refresh(db_producto)
    return db_producto        




