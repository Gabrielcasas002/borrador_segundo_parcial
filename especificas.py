# from guardar_usuarios import *
from funciones_comodines import *
from funciones_mostrar import *
from funciones_ronda import *
import random

def listar_palabras(palabras_asociadas: list, palabras_descubiertas: list) -> list:
    """_summary_

    Args:
        palabras_asociadas (list): Lista de palabras recibida por parametro.
        palabras_descubiertas (list): Lista de palabras descubiertas por el usuario recibida por parametro.

    Returns:
        list: 
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


def limpiar_lista(diccionario_juego: list, nivel: int, lista_letras: list, lista_palabras: list) -> dict:
    """_summary_

    Args:
        diccionario_juego (list): Diccionario obtenido por parametro que representa al diccionario del juego.
        nivel (int): Entero recibido por parametro que representa a el nivel actual.
        lista_letras (list): Lista de letras recibida por parametro.
        lista_palabras (list): Lista de palabaras recibida por parametro.

    Returns:
        dict: La funcion elimina las listas recibidas del diccionario del juego y retorna un nuevo diccionario modificado.
    """

    partidas = diccionario_juego[nivel - 1]["partidas"]
    indice_a_borrar = -1

    for i in range(len(partidas)):
        partida = partidas[i]

        if partida["letras"] == lista_letras and partida["palabras"] == lista_palabras:
            indice_a_borrar = i
            break

    if indice_a_borrar != -1:
        partidas.pop(indice_a_borrar)

    return diccionario_juego


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

        if encontrada:
            ocultas.append(palabras_total[i])
        else:
            ocultas.append("_" * len(palabras_total[i]))

    return ocultas


def elegir_letras_nivel(nivel: dict) -> list:
    """_summary_

    Args:
        nivel (dict): Diccionario recibido por parametro que representa a un nivel del juego que contiene 3 listas de letras.

    Returns:
        list: La funcion selecciona una de esas 3 listas al azar y la retorna en una nueva lista.
    """

    indice = random.randint(0, len(nivel["partidas"]) - 1)
    lista_letras = nivel["partidas"][indice]["letras"]

    return lista_letras


def elegir_nivel(diccionario_niveles: list, numero: int) -> dict:
    """_summary_

    Devuelve el diccionario correspondiente al nivel solicitado.

    Args:
        diccionario_niveles (list): Lista de niveles cargados.
        numero (int): Nivel a seleccionar.

    Returns:
        dict: Retorna el Nivel encontrado
    """

    for i in range(len(diccionario_niveles)):
        if diccionario_niveles[i]["nivel"] == numero:
            return diccionario_niveles[i]


# Cambiar el nombre
def elegir_palabras_nivel(nivel: dict, letras: list) -> list:
    """_summary_

    Args:
        nivel (dict): Diccionario recibido por parametro que representa a un nivel del juego que contiene 3 listas de letras y 3 listas de palabras.
        letras (list): Lista de letras recibida por parametro que representa a una de las listas ubicadas en el diccionario.

    Returns:
        list: La funcion utiliza la lista de letras para buscar su lista de palabras, una vez encontrada, la guarda en una nueva lista y la retorna.
    """

    palabras = []
    partidas = nivel["partidas"]

    for i in range(len(partidas)):
        if partidas[i]["letras"] == letras:
            palabras = partidas[i]["palabras"]
    
    return palabras


def copiar_lista(lista_original: list) -> list:
    """_summary_

    Args:
        lista_original (list): Lista recibida por parametro.

    Returns:
        list: La funcion copia cada elemento de la lista recibida por parametro. su funcion es hacer lo mismo que el comando .copy()
    """

    nueva_lista = list()

    for i in range(len(lista_original)):
        nueva_lista.append(lista_original[i])

    return nueva_lista

