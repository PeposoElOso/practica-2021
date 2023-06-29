"""Bloque IF, operadores lógicos, función max y operador ternario."""


def maximo_basico(a: float, b: float) -> float:
    "Toma dos números y devuelve el mayor."
    if a > b :
        return a
    elif a==b:
        print("Son iguales")
        return a
    else:
        return b

    "Restricción: No utilizar la función max"
    

print(maximo_basico(90,5))

# NO MODIFICAR - INICIO
assert maximo_basico(10, 5) == 10
assert maximo_basico(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_libreria(a: float, b: float) -> float:
    """#Re-escribir utilizando el built-in max.
    #Referencia: https://docs.python.org/3/library/functions.html#max
    """
    return max(a, b)
    
    
print(maximo_libreria(90,5))


# NO MODIFICAR - INICIO
assert maximo_libreria(9, 18) == 18
# NO MODIFICAR - FIN


###############################################################################


def maximo_ternario(a: float, b: float) -> float:
    """#Re-escribir utilizando el operador ternario.
    #Referencia: https://docs.python.org/3/reference/expressions.html#conditional-expressions
"""
    return b if b>a else a
    pass # Completar

print (maximo_ternario(90, 8))
# NO MODIFICAR - INICIO
#assert maximo_ternario(10, 5) == 10
#assert maximo_ternario(9, 18) == 18
# NO MODIFICAR - FIN
