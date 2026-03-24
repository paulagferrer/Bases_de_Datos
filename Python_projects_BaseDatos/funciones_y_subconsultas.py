import mysql.connector

EJERCICIO_2 = True

cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="contraseña",
        database="airportdb"
    )
cur = cnx.cursor()

if EJERCICIO_2:

    cur.execute("SELECT * FROM airport LIMIT 3")
    for row in cur.fetchall():
        print(row)

    cur.close()
    cnx.close()