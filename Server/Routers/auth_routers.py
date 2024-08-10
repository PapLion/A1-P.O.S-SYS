import asyncio
from functions_jwt import *
from fastapi import APIRouter, Header
from models import *
from fastapi import HTTPException
from search import *
from auth_db import *
from encryption import *

auth_rts = APIRouter()


@auth_rts.post("/login")
async def login_form(data: login) -> str:
    """
    Esta funcion obtiene los parametros ingresados en la
    clase data:
        data.email y data.password

    Primero obtiene la contraseña del email ingresado, para posteriormente
    comprobar la contraseña existente con la ingresada.

    Si no se puede obtener una contraseña la cuenta no existe y se manda error.
    Si la contraseña es incorrecta se manda error.

    Si todo es correcto, procede a generarse y enviarse el token al cliente.
    """

    get_password: str|bool = await login_query(data.email)

    verify_password: bool = check_data(get_password, data.password)
    
    if not get_password:
        raise HTTPException(status_code=400, detail="El correo electrónico es incorrecto...")
    
    if not verify_password:
       raise HTTPException(status_code=400, detail="La contraseña es incorrecta...")
    
    token_create = write_token(data.model_dump())
    
    raise HTTPException(status_code=200, detail=token_create)

@auth_rts.post("/register")
async def register_form(data: register) -> str:
    """
    Esta funcion recibe la clase "register" como parametro de la
    cual obtenemos los valores ingresados por el usuario:
    nick_name,
    email,
    password.

    Verificamos si el nick_name y el email ya están en uso, si es así
    se manda error.
    Si las contraseña ingresadas no coinciden se manda error.
    
    Si ninguno de los casos anteriores se dio, se procede a crear la cuenta.
    """

    get_nickn: tuple|bool = await srch_nickN(data.nick_name)

    get_email: tuple|bool = await srch_email(data.email)

    if get_email and get_nickn:
        raise HTTPException(status_code=409, detail="El nickname y email ya están en uso.")

    if get_nickn:
        raise HTTPException(status_code=409, detail="El nickname ya está en uso.")

    if get_email:
        raise HTTPException(status_code=409, detail="El email ya está en uso.")
    
    if data.password != data.confirm_password:
        raise HTTPException(status_code=409, detail="Las contraseñas ingresadas no son iguales.")
    
    await register_query(email=data.email, 
                         nick_name=data.nick_name,
                         password=encrypt_data(data.password))
    raise HTTPException(status_code=200, detail="Registro exitoso.")


@auth_rts.post("/verify/token")
async def token_verify(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token=token, output=True)

