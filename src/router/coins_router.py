from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from ..repository import coins_repository

from ..db.get_db import get_db
from fastapi import APIRouter

router = APIRouter()


@router.get("/coins")
def get_coins(db: Session = Depends(get_db)):
    db_coins = coins_repository.get_coins(db)
    if db_coins:
        return db_coins
    return HTTPException(404)
