import sqlite3

# Conectar a la base de datos (la creará si no existe)
conn = sqlite3.connect('project.db', isolation_level=None)
cursor = conn.cursor()


