from especificas import *
from diccionario_juego import *
import random


def rebanar(cadena: str, inicio: int, finalizacion: int) -> str:
    """_summary_

    Args:
        cadena (str): String recibido por parametro.
        inicio (int): Entero que recibido por parametro que marca el inicio.
        finalizacion (int): Entero recibido por parametro que marca la finalizacion

    Returns:
        str: La funcion retorna un nuevo string, recortando el anterior desde el inicio hasta la finalizacion. 
    """
    cadena_auxiliar = ""
    for caracter in range(inicio, finalizacion):
        cadena_auxiliar += cadena[caracter]

    return cadena_auxiliar


def listar_palabras(palabras_asociadas: list, palabras_descubiertas: list) -> list:
    """_summary_

    Args:
        palabras_asociadas (list): Lista de palabras recibida por parametro.
        palabras_descubiertas (list): Lista de palabras descubiertas por el usuario recibida por parametro.

    Returns:
        list: Returna una lista sin elementos repetidos
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


def ocultar_palabras(palabras_asociadas: list, palabras_descubiertas: list):
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


def seleccionar_string_aleatoria(lista: list) -> str:
    """_summary_

    Args:
        lista (list): Lista recibida por parametro. 

    Returns:
        str: La funcion toma un elemento aleatorio de la lista, lo guarda en una variable y lo retorna.
    """

    indice = random.randint(0, len(lista) - 1)

    indice_string = lista[indice]

    return indice_string


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


def ubicacion_valida(palabra_ubicada: str, palabra: str) -> bool:
    """_summary_

    Recibe dos cadenas, y verifica si palabra_ubicada tiene contenido, si no tiene retorna un false.
    Y si tiene contenido pero no tienen el mismo largo, tambien retorna un false.

    Args:
        palabra_ubicada (str): String recibido por parametro.
        palabra_real (str): String recibido por parametro.

    Returns:
        bool: Si la palabra ubicada es None o es distina de la palabra real, la bandera cambia de estado y la retorna como False. Caso contrario, retorna True.
    """

    bandera = True
    
    if palabra_ubicada == None:
        bandera = False

    elif len(palabra_ubicada) != len(palabra):
        bandera = False
    
    return bandera


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