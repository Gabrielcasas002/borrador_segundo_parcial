from especificas_comodines import *
from especificas import *


def combinar_palabra(ocultas_actual: str, palabra: str, palabra_ubicada: str) -> str:
    """_summary_

    Args:
        base_actual (str): String recibido por parametro.
        palabra (str): String recibido por parametro.
        palabra_ubicada (str): String recibido por parametro.

    Returns:
        str: la funcion construye un nuevo string combinando los strings recibidos.
    """

    combinada = ""
    
    for i in range(len(palabra)):
        if palabra_ubicada[i] != "_":
            combinada += palabra_ubicada[i]
        elif palabra_ubicada[i] == "_":
            combinada += ocultas_actual[i]
    
    return combinada


def combinar_listas_ubicar(lista_ubicar: list, lista_ocultas_base: list, lista_palabras: list) -> list:
    """_summary_

    Args:
        lista_ubicar (list): Lista recibida por parametro que representa a la lista generada por el comodin ubicar_letra .
        base (list): Lista de palabras descubiertas por el usuario recibida por parametro.
        lista_palabras (list): Lista de palabras obtenida por parametro.

    Returns:
        list: la funcion genera una nueva lista con las palabras actualizadas segun las revelaciones que fueron validas en el comodin.
    """

    nueva_lista = []

    if lista_ubicar == None:
        nueva_lista = copiar_lista(lista_ocultas_base)

    else:
        for i in range(len(lista_palabras)):
            palabra = lista_palabras[i]
            cadena_ocultas_actual = lista_ocultas_base[i]
            palabra_ubicada = lista_ubicar[i]
            bandera = ubicacion_valida(palabra_ubicada, palabra)

            if bandera == False:
                nueva_lista.append(cadena_ocultas_actual)
            elif bandera == True:
                combinada = combinar_palabra(cadena_ocultas_actual, palabra, palabra_ubicada)
                nueva_lista.append(combinada)

    return nueva_lista


def combinar_listas(lista_ubicar: list, lista_revelada: list, lista_palabras: list) -> list:
    
    lista = []

    for i in range(len(lista_palabras)):
        palabra_real = lista_palabras[i]
        palabra_ubicada = lista_ubicar[i]
        palabra_revelada = lista_revelada[i]

        palabra_final = ""

        for j in range(len(palabra_real)):
            letra_real = palabra_real[j]
            letra_ubicada = palabra_ubicada[j]
            letra_revelada = palabra_revelada[j]

            if letra_ubicada != "_" and letra_ubicada == letra_real:
                palabra_final += letra_ubicada

            elif letra_revelada != "_" and letra_revelada == letra_real:
                palabra_final += letra_revelada

            else:
                palabra_final += "_"

        lista.append(palabra_final)

    return lista