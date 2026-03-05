import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Milu2025&",
        database="airportdb"
    )
cur = cnx.cursor()

EJERCICIO_27 = False
EJERCICIO_34 = True

if EJERCICIO_27:
    cur.execute("SELECT * FROM airport_geo")
    rows = cur.fetchall()
    columnas = [col[0] for col in cur.description]

    df = pd.DataFrame(rows, columns=columnas)
    #ejericio 27 obtener aeropuestos
    df = df.sort_values('country')

    # ejercicios 28 recorrer y contar
    counts = {}
    for _, row in df.iterrows():
        country = row['country']
        counts[country] = counts.get(country, 0) + 1

    # encontrar país con mas aeropuertos
    max_country = max(counts.items(), key=lambda kv: kv[1])
    print("Ejerici 30:")
    print("País con más aeropuertos:", max_country)

if EJERCICIO_34:
    # ejerdicio 34
    cur.execute("SELECT flightno, departure FROM flight;")
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    df_flights = pd.DataFrame(rows, columns=cols)

    # ejercicio 36
    df_flights['departure'] = pd.to_datetime(df_flights['departure'])

    # ejericio 37 extraer año
    df_flights['year'] = df_flights['departure'].dt.year

    #ejericio 38 ordenar por fecha de salida descendente
    df_flights = df_flights.sort_values('departure', ascending=False)
