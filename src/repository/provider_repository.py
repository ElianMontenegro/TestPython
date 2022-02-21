from sqlalchemy.orm import Session
from ..models import schemas
from ..models import provider_model


def create_provider(db: Session, provider: schemas.Provider):
    db_provider = provider_model.Provider(
        nom_proveedor=provider.nom_proveedor)
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider


def get_provider_by_id(db: Session, provider_id: int):
    return db.query(provider_model.Provider).filter(provider_model.Provider.id == provider_id).first()


def update_provider(db: Session, provider_id: int, provider: schemas.Provider):
    db_provider = db.query(provider_model.Provider).filter(provider_model.Provider.id == provider_id).update(
        {provider_model.Provider.nom_proveedor: provider.nom_proveedor})
    db.commit()
    return db_provider == 1


def delete_provider(db: Session, provider_id: int):
    db_provider = db.query(provider_model.Provider).filter(
        provider_model.Provider.id == provider_id).delete()
    db.commit()
    return db_provider == 1
