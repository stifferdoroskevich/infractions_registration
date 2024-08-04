from pydantic import BaseModel
from typing import List, Optional

class VehiculoBase(BaseModel):
    placa_patente: str
    marca: str
    color: str

class VehiculoCreate(VehiculoBase):
    owner_id: int

class Vehiculo(VehiculoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class PersonaBase(BaseModel):
    nombre: str
    correo_electronico: str

class PersonaCreate(PersonaBase):
    pass

class Persona(PersonaBase):
    id: int
    vehiculos: List[Vehiculo] = []

    class Config:
        orm_mode = True

class OficialBase(BaseModel):
    nombre: str
    numero_identificatorio: str

class OficialCreate(OficialBase):
    pass

class Oficial(OficialBase):
    id: int

    class Config:
        orm_mode = True
