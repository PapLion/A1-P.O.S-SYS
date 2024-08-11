from pydantic import BaseModel

class register(BaseModel):
    user_name:str
    user_email: str
    user_password:str 
    confirm_password:str

class login(BaseModel):
    user_email: str
    user_password: str

class post(BaseModel):
    token: str
    newPostContent: str
    archive: str | None = None

class item(BaseModel):
    user_id: str
    item_name: str
    item_price: int
    item_lot: int