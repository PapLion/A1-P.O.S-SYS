import asyncio
import aiomysql
from database import connect_database


# Search a user with the nick name in the db
async def srch_nickN(user_name) -> tuple:
    # Connecto to database
    conn: aiomysql.connection = await connect_database()

    async with conn.cursor() as cursor:
        query: str = "SELECT * FROM users WHERE user_name = %s"
        await cursor.execute(query, (user_name,))
        response = await cursor.fetchone()
        if not response:
            return False
        return True

# Search a user with the name in the db
async def srch_name(user_name) -> tuple | bool:
    # Connecto to database
    conn: aiomysql.connection = await connect_database()

    async with conn.cursor() as cursor:
        query: str = "SELECT * FROM users WHERE full_name = %s"
        await cursor.execute(query, (user_name,))
        response = await cursor.fetchone()
        if not response:
            return False
        return response

# Search a user with the email in the db
async def srch_email(correo) -> tuple | bool:
    conn: aiomysql.connection = await connect_database()
    async with conn.cursor() as cursor:
        query: str = "SELECT * FROM users WHERE user_email = %s"
        await cursor.execute(query, (correo,))
        response = await cursor.fetchone()
        if not response:
            return False
        return True

# Get password with the email.
async def getPassword_with_Email(email: str) -> str | bool:
    conn: aiomysql.connection = await connect_database() # DB Connect


    async with conn.cursor() as cursor:
        query: str = "SELECT password FROM users WHERE email = %s"
        await cursor.execute(query, (email,)) # Ejecutamos la query de MySQL
        response = await cursor.fetchone()
        
        # Si response no está vacio agarramos la contraseña y la enviamos
        if response is not None:
            password = response['password']
            return password
        
        # Si response está vacio mandamos False
        else:
            return False
        
# Get full data with email and password.
async def email_password(email: str, password: str) -> str | bool:
    conn: aiomysql.connection = await connect_database()
    async with conn.cursor() as cursor:
        query: str = "SELECT password FROM users WHERE email = %s AND password = %s"
        await cursor.execute(query, (email, password,))
        response = await cursor.fetchone()
        if not response:
            return False
        return response

# Get nick with user_id
async def nick_id(user_id) -> str | bool:
    conn: aiomysql.connection = await connect_database()
    async with conn.cursor() as cursor:
        query: str = "SELECT user_name FROM users WHERE user_id = %s"
        await cursor.execute(query, (user_id))
        response = await cursor.fetchone()
        if not response:
            return False
        return response['user_name']


# Get full data with email and password.
async def get_contacts(user_id) -> list | bool:
    conn: aiomysql.connection = await connect_database() # DB connection
    async with conn.cursor() as cursor: # Cursor instance


        # SQL Query
        sql = """SELECT contact_id, 
        CASE WHEN user_id1 = %s THEN user_id2 
        ELSE user_id1 
        END AS user_id 
        FROM contacts 
        WHERE user_id1 = %s OR user_id2 = %s"""
        
        # Get contact list
        await cursor.execute(sql, (user_id, user_id, user_id))
        contacts_list = await cursor.fetchall()

        if not contacts_list:
            return False
        
        contact_list_nick: list = []

        # For Contact in contact_list
        for contact in contacts_list:
            # Get contact id
            id = contact['user_id']
             
            # Get nick name with user_id
            response = await nick_id(user_id = id)

            # Set nick name in contact_list_nick
            contact_list_nick.append(response)

        return contact_list_nick





