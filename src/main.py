from fastapi import FastAPI
from .router import client_router, provider_router, coins_router
app = FastAPI()

app.include_router(client_router.router)
app.include_router(provider_router.router)
app.include_router(coins_router.router)
