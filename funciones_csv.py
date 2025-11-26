import random

def elegir_letras_csv(diccionario: dict) -> list:
    """_summary_

    Args:
        diccionario (dict): Recibe el diccionario_juego como paramatetro, para luego seleccionar una lista de letras aleatoriamente

    Returns:
        list: Lista de letras aleatoria del diccionario
    """

    indice = random.randint(0, len(diccionario) - 1)
    lista_letras = diccionario[indice]["letras"]

    return lista_letras


def elegir_palabras_csv(diccionario: dict, letras: list) -> list:
    """_summary_

    Args:
        diccionario (dict): Recibe el diccionario_juego como parametro
        letras (list): Recibe la lista de letras seleccionada anteriormente, para elegir la lista de palabras asociadas a la lista de letras
    Returns:
        list: Devuelve la lista de palabras seleccionadas
    """


    for i in range(len(diccionario)):

        if diccionario[i]["letras"] == letras:

            lista_palabras = diccionario[i]["palabras"]

    return lista_palabras


def eliminar_lista_csv(diccionario: list, lista_letras: list, lista_palabras: list):
    """_summary_

    Elimina del diccionario la sección que coincide exactamente con las letras y palabras dadas.

    Args:
        diccionario (list): Recibe el diccionario_juego
        lista_letras (list): Recibe la lista de letras seleccionada anteriormente
        lista_palabras (list): Recibe la lista de palabras dada anteriormente
    """

    for i in range(len(diccionario)):
        seccion = diccionario[i]
        if seccion["letras"] == lista_letras and seccion["palabras"] == lista_palabras:
            diccionario.remove(seccion)
            break


def recorrer_lista_letras(lista: list) -> str:
    """_summary_

    Convierte una lista de letras en un string sin separadores.

    Args:
        lista (list): Lista a recorrer

    Returns:
        str: Devuelve la lista letras como una cadena
    """

    cadena = ""

    for i in range(len(lista)):
        cadena += lista[i]

    return cadena


def recorrer_lista_palabras(lista: list) -> str:
    """_summary_

    Convierte una lista de palabras en un string separado por guiones.

    Args:
        lista (list): Lista de palabras

    Returns:
        str: Devuelve una cadena separando cada palabra con guiones
    """

    cadena = ""

    for i in range(len(lista)):
        cadena += lista[i]
        if i < len(lista) - 1:     
            cadena += "-"

    return cadena


def armar_palabras(palabra_actual: str, palabras_str: str) -> list:
    """_summary_

    Convierte un string de palabras unidas por guiones en una lista de palabras.

    Args:
        palabra_actual (str): Variable auxiliar para construir cada palabra
        palabras_str (str): Cadena formada anteriormente separada en guiones

    Returns:
        list: Lista de palabras separadas.
    """

    palabras_lista = []

    for i in range(len(palabras_str)):
        if palabras_str[i] != "-":
            palabra_actual += palabras_str[i]
        elif palabras_str[i] == "-":
            palabras_lista.append(palabra_actual)
            palabra_actual = ""

    if palabra_actual != "":
        palabras_lista.append(palabra_actual)

    return palabras_lista

