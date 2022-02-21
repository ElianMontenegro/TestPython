from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from ..repository import client_repository, provider_repository

from ..models import schemas
from ..db.get_db import get_db
from fastapi import APIRouter

router = APIRouter()


@router.post("/client/")
def create_client(client: schemas.Client, db: Session = Depends(get_db)):
    db_client = client_repository.create_client(db=db, client=client)
    if db_client:
        return HTTPException(201)
    return HTTPException(400)


@router.put("/client/{client_id}")
def update_client(client_id: int, client: schemas.Client, db: Session = Depends(get_db)):
    db_client = client_repository.update_user(
        db, client_id=client_id, client=client)
    if db_client:
        return HTTPException(200)
    return HTTPException(404, detail="client not found")


@router.delete("/client/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    db_client = client_repository.delete_user(db, client_id=client_id)
    if db_client:
        return HTTPException(200)
    return HTTPException(404, detail="client not found")


@router.post("/client/{client_id}/{provider_id}")
def asing_provider_to_client(
    provider_id: int,
    client_id: int,
    db: Session = Depends(get_db)
):
    db_client = client_repository.get_client_by_id(db, client_id=client_id)
    if not db_client:
        raise HTTPException(404, detail="client not found")

    db_provider = provider_repository.get_provider_by_id(
        db, provider_id=provider_id)
    if not db_provider:
        raise HTTPException(404, detail="provider not found")

    db_provider_client = client_repository.asing_provider_to_client(
        db, client_id, provider_id)
    if db_provider_client:
        return HTTPException(201)
    return HTTPException(400)
