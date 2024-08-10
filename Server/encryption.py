from werkzeug.security import generate_password_hash, check_password_hash

# Encripta información usando 'pbkdf2:sha256'
def encrypt_data(data: str) -> str: 
    data_encrypted: str = generate_password_hash(data, 'pbkdf2:sha256', 30)
    return data_encrypted


# Verifica si la información ingresada y la existente son iguales.
def check_data(hashed: str, password: str) -> bool:
    if not hashed:
        return False
    else:
        return check_password_hash(hashed, password)