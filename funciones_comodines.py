from comodines import *
import os

def mostrar_comodines(estado_comodines: list):
    """_summary_

    Muestra los comodines que estan disponibles para usar, y si ya se uso anteriormente muestra un mensaje

    Args:
        estado_comodines (list): Lista sacada del diccionario de juego con el estado de los comodines controlada por booleanos
        - estado_comodines[1]: Comodín "Ubicar letra".

    """

    if estado_comodines[0] == False and estado_comodines[1] == False:
        print("Ingrese [1] para usar Revelar Palabra\n")
        print("Ingrese [2] para usar Ubicar Letras\n")


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
    elif ingreso == "1" and estado_comodines[0] == False:
        print("Ese comodín Revelar [1] ya fue usado.")

    elif ingreso == "2" and estado_comodines[1] == False:
        estado_comodines[1] = True
    else:
        print("Ese comodín Ubicar Letra [2] ya fue usado.")


def usar_comodin_revelar(estado_comodines: list, lista_palabras: list, palabras_ingresadas: list, lista_revelar: list) -> list:
    """_summary_

    Args:
        estado_comodines (list): Lista de banderas recibida por parametro.
        lista_palabras (list): Lista de palabras recibida por parametro.
        palabras_ingresadas (list): Lista de palabras ingresadas por el usuario recibida por parametro.
        lista_revelar (list): Lista donde se aplicará el comodin.

    Returns:
        list: Si la bandera mantiene su estado original, el comodin se podra aplicar a la lista_revelar sin problema. 
              Caso contrario, le notificará al usuario que el comodin ya fue utilizado. 
    """

    if estado_comodines[0] == False:
        lista_revelar = revelar_mitad(palabras_ingresadas, lista_palabras)
        estado_comodines[0] = True
        print("\nComodín 'Revelar Palabra' aplicado!")
    else:
        print("El comodín Revelar Palabra ya fue usado.")

    os.system("pause")
    os.system("cls")
    
    return lista_revelar


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
