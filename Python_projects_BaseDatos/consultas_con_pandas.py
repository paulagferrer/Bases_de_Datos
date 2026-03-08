import pandas as pd
import mysql.connector

EJERCICIO_14 = False
EJERCICIO_21 = True

cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="contraseña",
        database="airportdb"
    )
cur = cnx.cursor()
if EJERCICIO_14:
    cur.execute("SELECT * FROM airport")
    rows = cur.fetchall()
    columnas = [col[0] for col in cur.description]

    df = pd.DataFrame(rows, columns=columnas) #ejercicio 15 y 17

    print("Exercici 18:",df.head())
    print("Exercici 19:")
    df.info()
    print("Exercici 20",df.shape)

if EJERCICIO_21:
    cur.execute("SELECT * FROM airport_geo")
    rows = cur.fetchall()
    columnas = [col[0] for col in cur.description]

    df2 = pd.DataFrame(rows, columns=columnas)

    # EJERCICIO 21: seleccionar columnas name y country
    print("Ejercicio 21:")
    print(df2[['name', 'country']].head())

    # EJERCICIO 22: filtrar aeropuertos cuyo país sea 'GERMANY'
    print("\nEjercicio 22:")
    df2_de = df2[df2['country'] == 'GERMANY']
    print(df2_de.head())

    # EJERCICIO 23: ordenar por name
    print("\nEjercicio 23:")
    df_sorted = df2.sort_values('name')
    print(df_sorted.head())

    # EJERCICIO 24: tipo de objeto
    print("\nEjercicio 24:")
    print(type(df2['country'] == 'SPAIN'))

    # EJERCICIO 25: detectar nulos
    print("\nEjercicio 25 - Conteo de nulos:")
    print(df2.isnull().sum())

