"""Base de Datos SQL - Baja"""

import datetime

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona
import sqlite3


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    conexion: sqlite3.Connection = sqlite3.connect("db.db")
    try:
        cursor  = conexion.cursor()
        query = """ DELETE FROM Persona WHERE IdPersona = ?"""
        cursor.execute(query, id_persona)
        conexion.commit()
        return cursor.rowcount > 0
    #Rowcount devuelve la cantidad de filas afectadas por la ultima consulta
    except: 
        conexion.rollback()
    finally:
        conexion.close()

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
