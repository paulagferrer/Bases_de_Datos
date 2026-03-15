import pandas as pd
import mysql.connector
# semana 4.1
EJERCICIO_24 = True
# El problema al cargar completamente booking en pandas es el consumo de memoria y
# el coste de transferencia de datos.
# Para tablas grandes, es preferible agregar primero en MySQL.
if EJERCICIO_24:
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="contraseña",
            database="airportdb"
        )
        query = "SELECT * FROM booking"
        df = pd.read_sql(query, cnx)

        print("Número total de filas:", len(df))
        print(df.head())
# no acaba nunca el programa
    except mysql.connector.Error as e:
        print("Error de conexión o consulta:", e)

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()