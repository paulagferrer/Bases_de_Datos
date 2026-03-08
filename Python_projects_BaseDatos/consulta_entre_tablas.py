import pymysql
import pandas as pd

cnx = pymysql.connect(
    host="localhost",
    user="root",
    password="Milu2025&",
    database="airportdb"
)
cur = cnx.cursor()
# EJERCICIO 42: obtener Airbus A380
cur.execute("""
    SELECT type_id
    FROM airportdb.airplane_type
    WHERE identifier = 'Airbus A380';
""")

resultado = cur.fetchall()

if resultado:
    type_id_a380 = resultado[0][0]
    # obtener los aviones de ese tipo
    cur.execute(f"""
        SELECT airplane_id
        FROM airportdb.airplane
        WHERE type_id = {type_id_a380};
    """)

    aviones_a380 = cur.fetchall()
    df_aviones = pd.DataFrame(aviones_a380, columns=["airplane_id"])

    # obtener vols
    cur.execute("""
        SELECT flightno, `from`, `to`, airplane_id
        FROM airportdb.flight;
    """)

    vuelos = cur.fetchall()
    df_vuelos = pd.DataFrame(vuelos, columns=["flightno", "from", "to", "airplane_id"])

    conteo_aeropuertos = {} # contar aeropuertos

    for avion_id in df_aviones["airplane_id"]:
        vuelos_avion = df_vuelos[df_vuelos["airplane_id"] == avion_id]

        for _, vuelo in vuelos_avion.iterrows():

            origen = vuelo["from"]
            destino = vuelo["to"]
            conteo_aeropuertos[origen] = conteo_aeropuertos.get(origen, 0) + 1
            conteo_aeropuertos[destino] = conteo_aeropuertos.get(destino, 0) + 1

    # obtener país de cada aeropuerto
    cur.execute("""
        SELECT airport_id, country
        FROM airportdb.airport_geo;
    """)

    aeropuertos = cur.fetchall()
    df_aeropuertos = pd.DataFrame(aeropuertos, columns=["airport_id", "country"])

    mapa_aeropuerto_pais = dict(zip(df_aeropuertos["airport_id"], df_aeropuertos["country"]))

    conteo_paises = {}   # conteo por país

    for aeropuerto_id, num_vuelos in conteo_aeropuertos.items():
        if aeropuerto_id in mapa_aeropuerto_pais:

            pais = mapa_aeropuerto_pais[aeropuerto_id]
            conteo_paises[pais] = conteo_paises.get(pais, 0) + num_vuelos

    print("\nConteo de vuelos A380 por país:")
    print(conteo_paises)

    if conteo_paises:
        pais_max = max(conteo_paises, key=conteo_paises.get)
        print(f"\nPaís con más vuelos de Airbus A380: {pais_max} ({conteo_paises[pais_max]} vuelos)")

cur.close()
cnx.close()