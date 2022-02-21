from pydantic import BaseModel


class Client(BaseModel):
    nom_cliente: str

    class Config:
        orm_mode = True


class Provider(BaseModel):
    nom_proveedor: str

    class Config:
        orm_mode = True
