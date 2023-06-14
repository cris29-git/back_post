from flask.ctx import AppContext
import mysql.connector
import pandas as pd
import inser_base_datos
from datetime import datetime
import os

class Conectar:
    @staticmethod
    def conectar():
        try:
            conexión = mysql.connector.connect(
                host="localhost",
                database="database_facturacionybonificacion-sicte",
                user="root",
                password="Admin.sicte1234",
                port="3306"
            )
            print("Conexión exitosa")
            return conexión
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)

    @staticmethod
    def insertar_datos(conn, ID_Table_Facture, CODIGO, Fecha, ALIADO, MOVIL, NOMBRE, CEDULA, ELITE, CUENTA, T_USER, IDORDEN_DE_TRABAJO, CODCIUDAD, CODNODO, AREA, CECO, CLASE, FACTURADO, CANTIDAD_ACTIVIDAD, COMUNIDAD, MODULO, CARPETA, TIPO_TRABAJO, SUBTIPO_TRABAJO, FECHA_CIERRE):
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO table_facture (ID_Table_Facture, CODIGO, Fecha, ALIADO, MOVIL, NOMBRE, CEDULA, ELITE, CUENTA, T_USER, IDORDEN_DE_TRABAJO, CODCIUDAD, CODNODO, AREA, CECO, CLASE, FACTURADO, CANTIDAD_ACTIVIDAD, COMUNIDAD, MODULO, CARPETA, TIPO_TRABAJO, SUBTIPO_TRABAJO, FECHA_CIERRE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (ID_Table_Facture, CODIGO, Fecha, ALIADO, MOVIL, NOMBRE, CEDULA, ELITE, CUENTA, T_USER, IDORDEN_DE_TRABAJO, CODCIUDAD, CODNODO, AREA, CECO, CLASE, FACTURADO, CANTIDAD_ACTIVIDAD, COMUNIDAD, MODULO, CARPETA, TIPO_TRABAJO, SUBTIPO_TRABAJO, FECHA_CIERRE,))
            conn.commit()
            print("Datos ingresados correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar los datos:", error)
        finally:
            if cursor:
                cursor.close()

    @staticmethod
    def cerrar_conexion(conn):
        if conn:
            conn.close()
            print("Conexión cerrada.")

def convertir_fecha_sql(fecha):
    fecha = datetime.strptime(fecha, '%d/%m/%Y')  # Suponiendo que la fecha de entrada esté en formato DD/MM/AAAA
    fecha_sql = fecha.strftime('%Y-%m-%d')  # Formato SQL: AAAA-MM-DD
    print("Fecha en formato SQL:", fecha_sql)
    return fecha_sql


def inicio():
    return "¡Inicio de sesión exitoso!"

# Leer el archivo Excel
try:
    df = pd.read_excel(r"C:\Users\Usuario\Desktop\back_post\SoporteFacturacion_2023_05_01 AL 2023_05_31.xlsx")
    print(df.columns)

    # Obtener los datos del archivo Excel
    # Aquí puedes procesar los datos del DataFrame df según tus necesidades
    # Por ejemplo, puedes recorrer las filas del DataFrame y llamar a la función insertar_datos para cada fila

    for fila in df.itertuples(index=False):
        ID_Table_Facture = fila.ID_Table_Facture
        CODIGO = fila.CODIGO
        Fecha = convertir_fecha_sql(fila.Fecha)
        ALIADO = fila.ALIADO
        MOVIL = fila.MOVIL
        NOMBRE = fila.NOMBRE
        CEDULA = fila.CEDULA
        ELITE = fila.ELITE
        CUENTA = fila.CUENTA
        T_USER = fila.T_USER
        IDORDEN_DE_TRABAJO = fila.IDORDEN_DE_TRABAJO
        CODCIUDAD = fila.CODCIUDAD
        CODNODO = fila.CODNODO
        AREA = fila.AREA
        CECO = fila.CECO
        CLASE = fila.CLASE
        FACTURADO = fila.FACTURADO
        CANTIDAD_ACTIVIDAD = fila.CANTIDAD_ACTIVIDAD
        COMUNIDAD = fila.COMUNIDAD
        MODULO = fila.MODULO
        CARPETA = fila.CARPETA
        TIPO_TRABAJO = fila.TIPO_TRABAJO
        SUBTIPO_TRABAJO = fila.SUBTIPO_TRABAJO
        FECHA_CIERRE = convertir_fecha_sql(fila.FECHA_CIERRE)

        # Establecer la conexión a la base de datos
        conn = Conectar.conectar()

        # Insertar los datos en la base de datos
        Conectar.insertar_datos(conn, ID_Table_Facture, CODIGO, Fecha, ALIADO, MOVIL, NOMBRE, CEDULA, ELITE, CUENTA, T_USER, IDORDEN_DE_TRABAJO, CODCIUDAD, CODNODO, AREA, CECO, CLASE, FACTURADO, CANTIDAD_ACTIVIDAD, COMUNIDAD, MODULO, CARPETA, TIPO_TRABAJO, SUBTIPO_TRABAJO, FECHA_CIERRE)

        # Cerrar la conexión
        Conectar.cerrar_conexion(conn)

except FileNotFoundError:
    print("No se encontró el archivo Excel.")

except Exception as error:
    print("Ocurrió un error:", error)

