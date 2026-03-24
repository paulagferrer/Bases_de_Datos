# hace cambios sin commit
# EXERCICI 21
import mysql.connector
import time

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Milu2025&",
    database="airportdb"
)
cursor = conexion.cursor()
# Desactivar autocommit
conexion.autocommit = False
print("CONEXION 1: iniciando transacción")
# Iniciar transacción con nivel por defecto (REPEATABLE READ)
conexion.start_transaction()
# Modificar un dato
cursor.execute("""
    UPDATE airport
    SET iata = 'XXX'
    WHERE airport_id = '329'
""")
print("CONEXION 1: dato modificado pero NO confirmado")
print("Esperando 30 segundos antes de terminar...")
time.sleep(30)
# No hacemos commit
print("CONEXION 1: cerrando sin commit (los cambios NO se guardan)")
conexion.close()