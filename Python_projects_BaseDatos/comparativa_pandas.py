import pandas as pd
import mysql.connector

EXERCICI_24 = True

if EXERCICI_24:
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

    except mysql.connector.Error as e:
        print("Error de conexión o consulta:", e)

    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()