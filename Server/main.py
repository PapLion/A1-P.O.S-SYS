from fastapi import FastAPI
from Routers.auth_routers import auth_rts
from Routers.inventory_routers import inventory_rts
from dotenv import load_dotenv

load_dotenv('.env')
app = FastAPI()
app.include_router(auth_rts)
app.include_router(inventory_rts)