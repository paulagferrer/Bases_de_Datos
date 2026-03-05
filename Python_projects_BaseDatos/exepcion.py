import mysql.connector
from mysql.connector import Error

try:
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mal_password",
        database="airportdb"
    )
except Error as e:
    print("Se ha producido una excepción:")
    print(type(e).__name__)
    print(e)