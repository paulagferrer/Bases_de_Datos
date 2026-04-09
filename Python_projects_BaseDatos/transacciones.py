import mysql.connector
EJERCICIO_11 = False
EJERCICIO_12 = True
cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="contraseña",
        database="airportdb")
cur = cnx.cursor()

if EJERCICIO_11:
    cnx.autocommit = False
    try:
        cur.execute("""
            INSERT INTO airport (airport_code, airport_name, city, country)
            VALUES ('YYY', 'Aeropuerto Python', 'Madrid', 'España')
            """)
        cnx.commit()
        print("Insertado correctamente")
    except:
        cnx.rollback()
        print("Error, se deshace la operación")
    cnx.close()

if EJERCICIO_12:
    cnx.autocommit = False
    try:
        cur.execute("""
            INSERT INTO airport (airport_code, airport_name, city, country)
            VALUES ('YYY', 'Aeropuerto Python', 'Madrid', 'España')
        """)
        raise Exception("Forzar error")
    except:
        cnx.rollback()
        print("Rollback ejecutado")
    cnx.close()

