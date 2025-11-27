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
