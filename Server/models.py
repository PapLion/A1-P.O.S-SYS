from pydantic import BaseModel

class register(BaseModel):
    user_name:str
    user_email: str
    user_password:str 
    confirm_password:str

class login(BaseModel):
    user_email: str
    user_password: str


class item(BaseModel):
    user_id: int
    item_name: str
    item_price: float
    item_lot: int