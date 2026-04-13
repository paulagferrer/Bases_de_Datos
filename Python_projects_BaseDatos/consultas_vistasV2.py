import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="contraseña",
    database="airportdb"
)
# EXERCICI 32
cur = conn.cursor()
cur.execute("SELECT * FROM `num_vuelos_por_aeropuerto` LIMIT 10")
rows = cur.fetchall()
columns = [desc[0] for desc in cur.description]

df = pd.DataFrame(rows, columns=columns)

print(df)

cur.close()
conn.close()

############################################################################################

import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="contraseña",
    database="airportdb")

# EXERCICI 34
df = pd.read_sql_query("SELECT * FROM `num_vuelos_por_aeropuerto`", conn)

print(df.head()) # EXERCICI 35

# EXERCICI 36
df_ordenado = df.sort_values(by="num_vuelos", ascending=False)
print(df_ordenado)

# EXERCICI 37
df_mas_100 = df[df["num_vuelos"] > 100]
print(df_mas_100)

conn.close()