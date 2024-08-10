import aiomysql
import asyncio
from database import connect_database

async def register_query(email: str, nick_name:str, password: str):
    conn: aiomysql.Connection = await connect_database()
    async with conn.cursor() as cursor:
        
        query: str = """INSERT INTO users 
                        (nick_name, email, password) 
                        VALUES (%s, %s, %s)"""
        await cursor.execute(query, (nick_name, email, password,))


async def login_query(email: str):
    conn: aiomysql.Connection = await connect_database()
    async with conn.cursor() as cursor:

        query: str = """SELECT password FROM users WHERE email = %s"""
        await cursor.execute(query, (email,))
        response = await cursor.fetchone()
        if not response:
            return False
        return response['password']
    