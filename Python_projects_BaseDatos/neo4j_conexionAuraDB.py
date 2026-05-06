from neo4j import GraphDatabase
import pandas as pd
# Datos de conexión
URI = "neo4j+ssc://855d4c45.databases.neo4j.io"
USER = "855d4c45"
PASSWORD = "FjjBpyxYoUAfzT6xq5Yk9qbjGiugWYCHIdbcps1oQvk"
DATABASE ="855d4c45"

def conectar():
    try:
        with GraphDatabase.driver(URI, auth=(USER, PASSWORD)) as driver:
            driver.verify_connectivity()
            print("-----------------------------------------")
            print("¡CONEXIÓN EXITOSA!")
            print("El usuario ha sido validado correctamente.")
            print("-----------------------------------------")
    except Exception as e:
        print(f"Error definitivo: {e}")
        print("\nSi el error es 'Unauthorized', revisa que no haya espacios")
        print("extras en la contraseña dentro de tu código.")
# exercici 1
# conectar()

