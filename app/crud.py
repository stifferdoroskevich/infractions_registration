from sqlalchemy.orm import Session
from . import models, schemas

def get_persona(db: Session, persona_id: int):
    return db.query(models.Persona).filter(models.Persona.id == persona_id).first()

def get_persona_by_email(db: Session, email: str):
    return db.query(models.Persona).filter(models.Persona.correo_electronico == email).first()

def get_personas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Persona).offset(skip).limit(limit).all()

def create_persona(db: Session, persona: schemas.PersonaCreate):
    db_persona = models.Persona(nombre=persona.nombre, correo_electronico=persona.correo_electronico)
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    return db_persona

# Similar functions for Vehiculo and Oficial...
