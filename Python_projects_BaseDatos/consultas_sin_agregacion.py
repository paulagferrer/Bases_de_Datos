import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="contraseña",
        database="airportdb"
    )
cur = cnx.cursor()
# exercicis semana 3_2
EJERCICIO_27 = False
EJERCICIO_34 = False
EJERCICIO_40 = True

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
    cur.execute("SELECT flightno, departure FROM flight;")
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    df_flights = pd.DataFrame(rows, columns=cols)

    print("Ejercicio 34:")
    print(df_flights.head())

    df_flights['departure'] = pd.to_datetime(df_flights['departure'])
    print("Ejercicio 36:")
    print(df_flights.dtypes)

    df_flights['year'] = df_flights['departure'].dt.year
    print("Ejercicio 37:")
    print(df_flights.head())

    df_flights = df_flights.sort_values('departure', ascending=False)
    print("Ejercicio 38:")
    print(df_flights.head())

if EJERCICIO_40:
    cur.execute("""
                SELECT *
                FROM flight
                WHERE departure > %s
                """, ("2015-01-07",))

    rows = cur.fetchall()
    columnas = [col[0] for col in cur.description]

    df_new = pd.DataFrame(rows, columns=columnas) #ecercici 41

