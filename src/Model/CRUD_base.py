import mysql.connector
from datetime import datetime
from typing import Literal, Tuple
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
    def insertar_datos(conn, datos):
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO table_facture (ID_Table_Facture, CODIGO, Fecha, ALIADO, MOVIL, NOMBRE, CEDULA, ELITE, CUENTA, T_USER, IDORDEN_DE_TRABAJO, CODCIUDAD, CODNODO, AREA, CECO, CLASE, FACTURADO, CANTIDAD_ACTIVIDAD, COMUNIDAD, MODULO, CARPETA, TIPO_TRABAJO, SUBTIPO_TRABAJO, FECHA_CIERRE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", datos)
            conn.commit()
            print("Datos ingresados correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar los datos:", error)
        finally:
            if cursor:
                cursor.close()

    @staticmethod
    def leer_datos(conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM table_facture")
            datos = cursor.fetchall()
            for fila in datos:
                print(fila)
        except mysql.connector.Error as error:
            print("Error al leer los datos:", error)
        finally:
            if cursor:
                cursor.close()

    @staticmethod
    def actualizar_datos(conn, ID_Table_Facture, nuevo_codigo, nueva_fecha):
        try:
            cursor = conn.cursor()
            consulta = "UPDATE table_facture SET CODIGO = %s, Fecha = %s WHERE ID_Table_Facture = %s"
            cursor.execute(consulta, (nuevo_codigo, nueva_fecha, ID_Table_Facture))
            conn.commit()
            print("Datos actualizados correctamente.")
        except mysql.connector.Error as error:
            print("Error al actualizar los datos:", error)
        finally:
            if cursor:
                cursor.close()

    @staticmethod
    def eliminar_datos(conn, ID_Table_Facture):
        try:
            cursor = conn.cursor()
            consulta = "DELETE FROM table_facture WHERE ID_Table_Facture = %s"
            cursor.execute(consulta, (ID_Table_Facture,))
            conn.commit()
            print("Datos eliminados correctamente.")
        except mysql.connector.Error as error:
            print("Error al eliminar los datos:", error)
        finally:
            if cursor:
                cursor.close()

    @staticmethod
    def consultar_datos(conn, consulta):
        try:
            cursor = conn.cursor()
            cursor.execute(consulta)
            datos = cursor.fetchall()
            for fila in datos:
                print(fila)
        except mysql.connector.Error as error:
            print("Error al realizar la consulta:", error)
        finally:
            if cursor:
                cursor.close()

    @staticmethod
    def validar_credenciales(conn, usuario, contraseña):
        try:
            cursor = conn.cursor()
            consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
            cursor.execute(consulta, (usuario, contraseña))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado is not None
        except mysql.connector.Error as error:
            print("Error al validar las credenciales:", error)
            return False

def convertir_fecha_sql(fecha):
    fecha = datetime.strptime(fecha, '%d/%m/%Y')  # Suponiendo que la fecha de entrada esté en formato DD/MM/AAAA
    fecha_sql = fecha.strftime('%Y-%m-%d')  # Formato SQL: AAAA-MM-DD
    print("Fecha en formato SQL:", fecha_sql)
    return fecha_sql

# Establecer la conexión a la base de datos
conn = Conectar.conectar()

# Leer los datos de la tabla
Conectar.leer_datos(conn)

# Insertar datos en la tabla
nuevos_datos = ("ID_Table_Facture", "CODIGO", "Fecha", "ALIADO", "MOVIL", "NOMBRE", "CEDULA", "ELITE", "CUENTA", "T_USER", "IDORDEN_DE_TRABAJO", "CODCIUDAD", "CODNODO", "AREA", "CECO", "CLASE", "FACTURADO", "CANTIDAD_ACTIVADAD", "COMUNIDAD", "MODULO", "CARPETA", "TIPO_TRABAJO", "SUBTIPO_TRABAJO", "FECHA_CIERRE")
Conectar.insertar_datos(conn, nuevos_datos)

# Actualizar los datos en la tabla
ID_Table_Facture_actualizar = 1  # Reemplaza 1 con el valor numérico correcto
nuevo_codigo = "Nuevo_Codigo"  # Reemplaza "Nuevo_Codigo" con el nuevo valor correcto
nueva_fecha = convertir_fecha_sql("01/06/2023")  # Reemplaza "01/06/2023" con la nueva fecha correcta
Conectar.actualizar_datos(conn, ID_Table_Facture_actualizar, nuevo_codigo, nueva_fecha)

# Eliminar datos de la tabla
ID_Table_Facture_eliminar = 1  # Reemplaza 1 con el valor numérico correcto
Conectar.eliminar_datos(conn, ID_Table_Facture_eliminar)

# Consultar datos en la tabla
consulta = "SELECT * FROM table_facture"
Conectar.consultar_datos(conn, consulta)

# Validar credenciales de usuario
usuario = input("Ingrese el nombre de usuario: ")
contraseña = input("Ingrese la contraseña: ")
if Conectar.validar_credenciales(conn, usuario, contraseña):
    print("Credenciales válidas. Inicio de sesión exitoso.")
else:
    print("Credenciales inválidas. Inicio de sesión fallido.")

# Cerrar la conexión
Conectar.cerrar_conexion(conn)
