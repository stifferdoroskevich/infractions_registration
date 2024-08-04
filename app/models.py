from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Persona(Base):
    __tablename__ = "personas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    correo_electronico = Column(String, unique=True, index=True)
    vehiculos = relationship("Vehiculo", back_populates="owner")

class Vehiculo(Base):
    __tablename__ = "vehiculos"
    id = Column(Integer, primary_key=True, index=True)
    placa_patente = Column(String, unique=True, index=True)
    marca = Column(String)
    color = Column(String)
    owner_id = Column(Integer, ForeignKey('personas.id'))
    owner = relationship("Persona", back_populates="vehiculos")

class Oficial(Base):
    __tablename__ = "oficiales"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    numero_identificatorio = Column(String, unique=True, index=True)
