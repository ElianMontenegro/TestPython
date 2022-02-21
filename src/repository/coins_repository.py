from sqlalchemy.orm import Session
from ..models import coins_model, client_model


def get_coins(db: Session):
    return db.query(coins_model.Coins_Client, client_model.Client, coins_model.Coins).filter(
        coins_model.Coins_Client.id_cliente == client_model.Client.id,
        coins_model.Coins_Client.id_moneda == coins_model.Coins.id,
    ).all()
