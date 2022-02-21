from sqlalchemy import Column, ForeignKey, Integer, String, Float
from ..db.database import Base


class Client(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nom_cliente = Column(String, unique=True, index=True)


class Provider_Client(Base):
    __tablename__ = 'proveedor_cliente'
    id_cliente = Column(ForeignKey('clientes.id'), primary_key=True)
    id_proveedor = Column(ForeignKey('proveedores.id'), primary_key=True)
