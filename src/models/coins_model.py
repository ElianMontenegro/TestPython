from sqlalchemy import Column, ForeignKey, Integer, String, Float
from ..db.database import Base


class Coins(Base):
    __tablename__ = "monedas"

    id = Column(Integer, primary_key=True, index=True)
    tipo_moneda = Column(String, index=True)

    class Config:
        orm_mode = True


class Coins_Client(Base):
    __tablename__ = 'moneda_cliente'
    id_cliente = Column(ForeignKey('clientes.id'), primary_key=True)
    id_moneda = Column(ForeignKey('monedas.id'), primary_key=True)
    valor = Column(Float)

    class Config:
        orm_mode = True
