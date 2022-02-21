
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from ..repository import provider_repository

from ..models import schemas
from ..db.get_db import get_db
from fastapi import APIRouter

router = APIRouter()


@router.post("/provider/")
def create_provider(provider: schemas.Provider, db: Session = Depends(get_db)):
    db_provider = provider_repository.create_provider(db=db, provider=provider)
    if db_provider:
        return HTTPException(201)
    return HTTPException(400)


@router.put("/provider/{provider_id}")
def update_provider(provider_id: int, provider: schemas.Provider, db: Session = Depends(get_db)):
    db_provider = provider_repository.update_provider(
        db, provider_id=provider_id, provider=provider)
    if db_provider:
        return HTTPException(200)
    return HTTPException(404, detail="provider not found")


@router.delete("/provider/{provider_id}")
def delete_provider(provider_id: int, db: Session = Depends(get_db)):
    db_provider = provider_repository.delete_provider(
        db, provider_id=provider_id)
    if db_provider:
        return HTTPException(200)
    return HTTPException(404, detail="provider not found")
