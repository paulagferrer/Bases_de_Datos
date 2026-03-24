# intenta leer esos cambios
# EXERCICI 22
import mysql.connector
import time

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Milu2025&",
    database="airportdb"
)
cursor = conexion.cursor()
print("\n--- LECTURA 1: nivel por defecto (REPEATABLE READ) ---")
cursor.execute("""
    SELECT iata
    FROM airport
    WHERE airport_id = '329'
""")
print("Resultado:", cursor.fetchall())
time.sleep(5)
print("\n--- LECTURA 2: READ UNCOMMITTED ---")
# Cambiar nivel de aislamiento
conexion.start_transaction(isolation_level='READ UNCOMMITTED')
cursor.execute("""
    UPDATE airport
    SET iata = 'XXX'
    WHERE airport_id = '329'
""")
print("Resultado:", cursor.fetchall())
conexion.close()