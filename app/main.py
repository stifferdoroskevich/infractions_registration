from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from pydantic import BaseModel
from typing import List
import sqlite3

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las orígenes. Cambia esto a una lista de dominios de confianza en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)


class Persona(BaseModel):
    id: int
    nombre: str
    correo_electronico: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:

        db.close()


def get_db_connection():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.post("/personas/", response_model=schemas.Persona)
def create_persona(persona: schemas.PersonaCreate, db: Session = Depends(get_db)):
    db_persona = crud.get_persona_by_email(db, email=persona.correo_electronico)
    if db_persona:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_persona(db=db, persona=persona)


@app.get("/personas/", response_model=List[Persona])
async def get_personas():
    conn = get_db_connection()
    personas = conn.execute("SELECT * FROM personas ORDER BY id").fetchall()
    conn.close()
    return [dict(persona) for persona in personas]
# Similar endpoints for Vehiculo and Oficial...
