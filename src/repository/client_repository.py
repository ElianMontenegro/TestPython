from sqlalchemy.orm import Session
from ..models import schemas
from ..models import client_model


def create_client(db: Session, client: schemas.Client):
    db_client = client_model.Client(
        nom_cliente=client.nom_cliente)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def get_client_by_id(db: Session, client_id: int):
    return db.query(client_model.Client).filter(client_model.Client.id == client_id).first()


def update_user(db: Session, client_id: int, client: schemas.Client):
    db_client = db.query(client_model.Client).filter(client_model.Client.id == client_id).update(
        {client_model.Client.nom_cliente: client.nom_cliente})
    db.commit()
    return db_client == 1


def delete_user(db: Session, client_id: int):
    db_client = db.query(client_model.Client).filter(
        client_model.Client.id == client_id).delete()
    db.commit()
    return db_client == 1


def asing_provider_to_client(db: Session, client_id: int, provider_id: int):
    db_provider_client = client_model.Provider_Client(
        id_cliente=client_id,
        id_proveedor=provider_id
    )
    db.add(db_provider_client)
    db.commit()
    db.refresh(db_provider_client)
    return db_provider_client
