import mysql.connector

EJERCICIO_2 = False
EJERCICIO_6 = False
EJERCICIO_7 = False
EJERCICIO_8 = True

cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Milu2025&",
        database="airportdb"
    )
cur = cnx.cursor()

if EJERCICIO_2:

    cur.execute("SELECT * FROM airport LIMIT 3")
    for row in cur.fetchall():
        print(row)

    cur.close()
    cnx.close()


if EJERCICIO_6:
    cur.execute("SELECT * FROM airport LIMIT 5")
    rows = cur.fetchall()
    print("Columnas:", [col[0] for col in cur.description])
    print("Filas:", cur.rowcount)

    cur.close()
    cnx.close()

if EJERCICIO_7:
    cur.execute("SELECT * FROM airport_geo WHERE country = 'SPAIN'")
    rows = cur.fetchall()
    for r in rows[:5]:
        print(r)

    cur.close()
    cnx.close()

if EJERCICIO_8:
    cur.execute("SELECT * FROM airport_geo WHERE country = 'SPAIN' ORDER BY city")
    rows = cur.fetchall()
    for r in rows[:5]:
        print(r)

    cur.close()
    cnx.close()