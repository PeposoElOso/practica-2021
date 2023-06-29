"""Base de Datos SQL - Creación de tablas auxiliares"""

from practico_04.ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3

def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    conexion: sqlite3.Connection = sqlite3.connect('data.db')
    try:
        cursor  = conexion.cursor()
        query = """CREATE A TABLE IF NOT EXISTS PersonaPeso
                        (IdPersona INTEGER PRIMARY KEY,
                        Fecha DATETIME,
                        Peso INTEGER,
                        FOREGIN KEY (IdPersona) REFERENCES Persona(IdPersona));"""
                 
        cursor.execute(query)
        conexion.commit()
        
    except:
        conexion.rollback()
    finally:
        conexion.close()

def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conexion: sqlite3.Connection = sqlite3.connect('data.db')
    try:
        cursor  : sqlite3.Cursor = conexion.cursor()
       
        cursor.execute(""" DROP TABLE IF EXISTS PersonaPeso;""")
        conexion.commit()
    except sqlite3.OperationalError as exception: 
        conexion.rollback()
    finally:
        conexion.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
