from fastapi import APIRouter, status
from models import item
from fastapi import HTTPException
from queries.itemsDB import *

inventory_rts = APIRouter()

@inventory_rts.post("/inventory")
async def get_inventory(itm: item):
    response_db = await insert(user_id=itm.user_id,
                         item_name=itm.item_name,
                         item_price=itm.item_price,
                         item_lot=itm.item_lot)
    
    if not response_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= "Oops, algo salió mal.. :()"
        )
    
    raise HTTPException(
        status_code=status.HTTP_201_CREATED,
        detail="Se creó el item con éxito."
    )