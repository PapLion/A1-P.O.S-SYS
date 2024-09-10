import aiomysql
import asyncio
from database import connect_database

async def register_query(user_email: str, user_name:str, user_password: str):
    conn: aiomysql.Connection = await connect_database()
    async with conn.cursor() as cursor:
        
        query: str = """INSERT INTO users 
                        (user_name, user_email, user_password) 
                        VALUES (%s, %s, %s)"""
        await cursor.execute(query, (user_name, user_email, user_password,))


async def login_query(user_email: str):
    conn: aiomysql.Connection = await connect_database()
    async with conn.cursor() as cursor:

        query: str = """SELECT user_password FROM users WHERE user_email = %s"""
        await cursor.execute(query, (user_email,))
        response = await cursor.fetchone()
        if not response:
            return False
        return response['user_password']
    