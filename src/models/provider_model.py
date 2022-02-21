from sqlalchemy import Column, Integer, String
from ..db.database import Base


class Provider(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nom_proveedor = Column(String, index=True)

    class Config:
        orm_mode = True
