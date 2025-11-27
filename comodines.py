from especificas_comodines import *
from diccionario_juego import *
from especificas import *
import random


def listar_palabras(palabras_asociadas: list, palabras_descubiertas: list) -> list:
    """_summary_

    Args:
        palabras_asociadas (list): Lista de palabras recibida por parametro.
        palabras_descubiertas (list): Lista de palabras descubiertas por el usuario recibida por parametro.

    Returns:
        list: La funcion crea una nueva lista sin elementos repetidos.
    """

    palabras_total = []

    for i in range(len(palabras_asociadas)):
        palabras_total.append(palabras_asociadas[i])

    for i in range(len(palabras_descubiertas)):
        repetido = False

        for j in range(len(palabras_total)):
            if palabras_descubiertas[i] == palabras_total[j]:
                repetido = True
                break

        if repetido == False:
            palabras_total.append(palabras_descubiertas[i])

    return palabras_total


def ocultar_palabras(palabras_asociadas: list, palabras_descubiertas: list) -> list:
    """_summary_

    Args:
        palabras_asociadas (list): Lista de palabras recibida por parametro.
        palabras_descubiertas (list): Lista de palabras decubiertas por el usuario recibida por parametro.

    Returns:
        list: La funcion retorna una nueva lista modificada utilizando ambas lista. Modifica cada elemento de las listas para agregar "_" a cada indice de los elementos.
    """

    palabras_total = listar_palabras(palabras_asociadas, palabras_descubiertas)

    ocultas = []

    for i in range(len(palabras_total)):
        encontrada = False

        for j in range(len(palabras_descubiertas)):
            if palabras_total[i] == palabras_descubiertas[j]:
                encontrada = True
                break

        if encontrada == True:
            ocultas.append(palabras_total[i])
        elif encontrada == False:
            ocultas.append("_" * len(palabras_total[i]))

    return ocultas



def revelar_mitad(palabras_ingresadas: list, palabras_asociadas: list) -> list:
    """_summary_

    Args:
        palabras_ingresadas (list): Lista de palabras ingresadas por el usuario obtenida por parametro.
        palabras_asociadas (list): lista de palabras obtenida por parametro.

    Returns:
        list: La funcion retorna una nueva lista donde uno de sus elementos cuenta con una palabra revelada parcialmente. 
    """
    
    ocultas = ocultar_palabras(palabras_asociadas, palabras_ingresadas)

    indices_ocultas = []
    for i in range(len(ocultas)):

        if ocultas[i] != palabras_asociadas[i]: 

            indices_ocultas.append(i)

    indice_aleatorio = indices_ocultas[random.randint(0, len(indices_ocultas) - 1)]
    palabra = palabras_asociadas[indice_aleatorio]


    if len(palabra) == 3:
        mitad = 2
    else:
        mitad = len(palabra) // 2

    primera_mitad = rebanar(palabra, 0, mitad)
    segunda_mitad = "_" * (len(palabra) - mitad)

    palabra_comodin = primera_mitad + segunda_mitad

    ocultas[indice_aleatorio] = palabra_comodin

    return ocultas


def ubicar_letra(lista_palabras: list, lista_descubiertas: list, lista_letras: list) -> list:
    """_summary_

    Args:
        lista_palabras (list): lista de palabras obtenida por parametro.
        lista_descubiertas (list): lista de palabras ingresadas por el usuario obtenida por parametro. 
        lista_letras (list): lista de letras recibida por parametro.

    Returns:
        list: La funcion busca un caracter aleatorio en la lista de letras, y retorna una nueva lista revelando la letra en las palabras que la contengan.
    """

    palabras_ocultas = ocultar_palabras(lista_palabras, lista_descubiertas)

    letra = seleccionar_string_aleatoria(lista_letras)

    lista_ubicar = []

    for i in range(len(lista_palabras)):
        palabra = lista_palabras[i]
        palabra_oculta = palabras_ocultas[i]

        nueva = ""
        
        j = 0
        while j < len(palabra):

            if palabra[j] == letra:
                nueva += letra
            elif palabra[j] != letra:
                nueva += palabra_oculta[j]

            j += 1

        lista_ubicar.append(nueva)

    return lista_ubicar
