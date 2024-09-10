import asyncio
import aiomysql
from database import connect_database



async def user_data(user_name) -> tuple | bool:
    conn: aiomysql.connection = await connect_database()
    async with conn.cursor() as cursor:
        query: str = "SELECT * FROM users WHERE user_name = %s"
        await cursor.execute(query, (user_name,))
        response = await cursor.fetchone()
        if not response:
            return False
        return response





