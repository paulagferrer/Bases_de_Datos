import mysql.connector
# EXERCICI 23
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Milu2025&",
    database="airportdb"
)
cursor = conexion.cursor()
# Cambiar nivel de aislamiento
cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED")

cursor.execute("""
    UPDATE airport
    SET iata = 'XXX'
    WHERE airport_id = '329'
""")
resultado = cursor.fetchall()
for fila in resultado:
    print(fila)
conexion.close()