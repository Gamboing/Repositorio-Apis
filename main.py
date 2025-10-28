# Generar API (FastAPI + Pydantic). Incluir endpoints (GET, POST, PUT, DELETE).
#Librerias utilizadas FastAPI y Pydantic
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

items_db = {}  # Diccionario para guardar los items

# Definicion del modelo de datos usando Pytdantic la estructura que utilizaran los datos de la Api que se vayan a ingresar
class Item(BaseModel):
    nombre: str
    precio: float
    descripcion: Optional[str] = None
#Creamos la instancia de FastAPI tecnicamente es el nombre de la aplicacion
app = FastAPI()

#Definimos el primer endpoint de tipo GET que devuelve un mensaje de bienvenida
@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a mi primera API con FastAPI"}

#Definimos un endpoint de tipo GET que recibe un ID de item y devuelve los detalles del item correspondiente
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items_db.get(item_id)
    if item:
        return {"item_id": item_id, "item": item}
    return {"error": "Item no encontrado"}

#Definimos un endpoint de tipo POST que recibe un item y lo devuelve con un mensaje de confirmacion aqui nos aseguramos que los Items 
# Cumplan con la estructura definida en el Modelo Item de Pydantic
@app.post("/items/{item_id}")
def crear_item(item_id: int, item: Item):
    items_db[item_id] = item
    return {"mensaje": "Item creado correctamente", "item": item}

# Definimos un endpoint de tipo PUT Que actualiza un item existente basado en su ID y devuelve el item actualizado
@app.put("/items/{item_id}")
def actualizar_item(item_id: int, item: Item):
    if item_id in items_db:
        items_db[item_id] = item
        return {"mensaje": f"Item {item_id} actualizado", "nuevo": item}
    return {"error": "Item no encontrado"}

# Definimos un endpoint de tipo DELETE que elimina un item basado en su ID y devuelve un mensaje de confirmacion
@app.delete("/items/{item_id}")
def eliminar_item(item_id: int):
    if item_id in items_db:
        del items_db[item_id]
        return {"mensaje": f"Item {item_id} eliminado correctamente"}
    return {"error": "Item no encontrado"}

