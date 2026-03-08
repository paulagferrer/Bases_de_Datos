import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="contraseña",
    database="airportdb"
)
cur = cnx.cursor()
EJERCICIOS_22_23_24 = True

if EJERCICIOS_22_23_24:

    # 1️⃣ Cargar datos desde airport_geo
    cur.execute("SELECT * FROM airport_geo")
    rows = cur.fetchall()
    columnas = [col[0] for col in cur.description]

    df = pd.DataFrame(rows, columns=columnas)

    print("Total filas cargadas:", len(df))
    print()

    # EJERCICIO 22
    conteo_pais = df.groupby('country').size().reset_index(name='total_airports')
    conteo_pais = conteo_pais.sort_values('total_airports', ascending=False)

    print("Ejercicio 22 - Aeropuertos por país:")
    print(conteo_pais.head())
    print()

    # EJERCICIO 23
    conteo_country_city = (
        df.groupby(['country', 'city'])
          .size()
          .reset_index(name='total_airports')
          .sort_values(['country', 'total_airports'], ascending=[True, False])
    )

    print("Ejercicio 23 - Aeropuertos por (country, city):")
    print(conteo_country_city.head())
    print()

    grupo_obj = df.groupby('country')

    print("Ejercicio 24 - Tipo devuelto por groupby:")
    print(type(grupo_obj))

cur.close()
cnx.close()