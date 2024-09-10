import aiomysql
from database import connect_database

async def insert_item(user_id: int, item_name:str, item_price:float, item_lot:int) -> bool:
    conn: aiomysql.Connection = await connect_database()
    try:
        async with conn.cursor() as cursor:
            query: str = """INSERT INTO items
                            (user_id, item_name, item_price, item_lot) 
                            VALUES (%s, %s, %s, %s)"""
            await cursor.execute(query, (user_id, item_name, item_price, item_lot,))
            await conn.commit()
            
            if cursor.rowcount == 1:
                print("Item registrado..")
                return True
            else:
                print("Item no registrado..")
                return False
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False
    finally:
        conn.close() 


