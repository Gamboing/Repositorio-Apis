# Generar API (FastAPI + Pydantic). Incluir endpoints (GET, POST, PUT, DELETE).
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    nombre: str
    precio: float
    descripcion: str | None = None

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a mi primera API con FastAPI"}


