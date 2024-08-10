from pydantic import BaseModel

class register(BaseModel):
    nick_name:str
    email: str
    password:str 
    confirm_password:str

class login(BaseModel):
    email: str
    password: str

class post(BaseModel):
    token: str
    newPostContent: str
    archive: str | None = None



class Datos(BaseModel):
    nick_name: str | None = None
    full_name: str | None = None
    email: str
    password: str
