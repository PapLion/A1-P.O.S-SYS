from fastapi import FastAPI
from Routers.auth_routers import auth_rts
from dotenv import load_dotenv

load_dotenv('.env')
app = FastAPI()
app.include_router(auth_rts)