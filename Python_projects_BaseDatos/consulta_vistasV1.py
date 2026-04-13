import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="contraseña",
    database="airportdb")

cur = conn.cursor()
# EXERCICI 31
cur.execute("SELECT * FROM `num_vuelos_por_aeropuerto`")
rows = cur.fetchall()
columns = [desc[0] for desc in cur.description]

df = pd.DataFrame(rows, columns=columns)

print(df)

cur.close()
conn.close()