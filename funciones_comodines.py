from comodines import *
from especificas import *
import os


def mostrar_comodines(estado_comodines: list):
    """_summary_

    Muestra los comodines que estan disponibles para usar, y si ya se uso anteriormente muestra un mensaje

    Args:
        estado_comodines (list): Lista sacada del diccionario de juego con el estado de los comodines controlada por booleanos
        - estado_comodines[1]: Comodín "Ubicar letra".

    """

    # if estado_comodines[0] == False:
    #     print("Ingrese [1] para usar Revelar Palabra")
    # else:
    #     print("El comodín Revelar Palabra ya fue usado.")

    if estado_comodines[1] == False:
        print("Ingrese [2] para usar Ubicar Letras\n")
    else:
        print("El comodín Ubicar Letras ya fue usado.\n")


def usar_comodines(estado_comodines: list, ingreso: str):
    """_summary_

    Marca un comodin como utilizado segun el ingreso del usuario 
    Controla que el usuario seleccione un comodin valido, y que no pueda usar un comodin que ya fue activado
    anteriormente

    Args:
        estado_comodines (list): Lista sacada del diccionario de juego con el estado de los comodines controlada por booleanos
        ingreso (str): Opcion ingresada por el usuario 
    """


    if ingreso == "1" and estado_comodines[0] == False:
        estado_comodines[0] = True

    elif ingreso == "2" and estado_comodines[1] == False:
        estado_comodines[1] = True

    else:
        print("Ese comodín ya fue usado.")


def usar_comodin_ubicar(estado_comodines: list, lista_palabras: list, palabras_ingresadas: list, lista_letras: list, lista_ubicar: list) -> list:
    """_summary_

    Activa el comodin Ubicar letra si no fue utilizado anteriormente y aplica su efecto

    El comodin ubica una letra sacada de la lista de letras, para mostrarla en todas las palabras que aun no fueron descubiertas
    Una vez aplicado el comodin, modifica la lista ubicar para que pueda usarse y seguir con el juego.

    Args:
        estado_comodines (list): Lista sacada del diccionario de juego con el estado de los comodines controlada por booleanos
        lista_palabras (list): Lista de palabras que aun no fueron adivinadas
        palabras_ingresadas (list): Lista de palabras ya adivinidadas
        lista_letras (list): Lista letras seleccionadas para jugar la ronda
        lista_ubicar (list): Lista donde se guarda el resultado del comodin

    Returns:
        list: Lista actualizada con el con efecto del comodin
    """

    if estado_comodines[1] == False:
        lista_ubicar = ubicar_letra(lista_palabras, palabras_ingresadas, lista_letras)
        estado_comodines[1] = True
        print("\nComodín 'Ubicar letras' aplicado!")
    else:
        print("El comodín Ubicar Letras ya fue usado.")

    os.system("pause")
    os.system("cls")
    
    return lista_ubicar


def actualizar_ocultas(lista_palabras: list, palabras_ingresadas: list, lista_ubicar: list, estado_comodines: list) -> list:
    """_summary_

    Modifica la lista de palabras ocultas, y aplica el efecto del comodin ubicar letra
    si es activado
    
    Funciona en dos etapas:
        1. Oculta normalmente las palabras no adivinadas.
        
        2. Si el comodín 'Ubicar letra' está activo, combina la ocultación
        con la letra ubicada usando `combinar_listas_ubicar`.

    Args:
        lista_palabras (list): Lista original de todas las palabras de la ronda.
        palabras_ingresadas (list): Lista de palabras ya adivinidadas
        lista_ubicar (list): Lista donde se guarda el resultado del comodin
        estado_comodines (list): Lista que indica si el comodín fue usado.

    Returns:
        list: la funcion retorna la lista combinada con el efecto del comodin. Si el comodin ya fue utilizado solo retorna una lista de palabras ocultas.
    """

    estado_comodin_ubicar = estado_comodines[1]

    lista_ocultas_base = ocultar_palabras(lista_palabras, palabras_ingresadas)
    combinada = lista_ocultas_base
    if estado_comodin_ubicar:
        combinada = combinar_listas_ubicar(lista_ubicar, lista_ocultas_base, lista_palabras)

    return combinada