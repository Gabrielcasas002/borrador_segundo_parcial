
def mostrar_estado_ronda(lista_palabras: list, incorrectas: int, puntuacion_total: int):
    """_summary_

    Args:
        lista_palabras (list):  Lista de palabras recibida por parametro.
        incorrectas (int): Entero recibido por parametro que representa la cantidad de ingresos incorrectos.
        puntuacion_total (int): Entero recibido por parametro que representa la cantidad de puntos totales. 
    """

    mostrar_lista(lista_palabras)

    print(f"Palabras Incorrectas: {incorrectas}")

    print("Total de puntos:", puntuacion_total)


def mostrar_lista(matriz: list):
    """_summary_

    Args:
        matriz (list): Lista recibida por parametro que se mostrará elemento por elemento.
    """

    for i in range(len(matriz)):
        print(matriz[i], end= " ")
    print()


def mostrar_diccionario(diccionario: dict):
    """_summary_

    Args:
        diccionario (dict): Diccionario obtenido por parametro que se mostrará sus claves y el contenido de cada una de ellas. 
    """

    for clave in diccionario.keys():
       print(f"{clave} : {diccionario[clave]}")


def mostrar_estado_partida(lista_letras: list, lista_ocultas: list, incorrectas: int, puntaje: int):
    """_summary_

    Args:
        lista_letras (list): Lista de letra obtenida por parametro.
        lista_ocultas (list): Lista de palabras ocultas obtenida por parametro.
        incorrectas (int): Entero obtenido por parametro que representa a la cantidad de ingresos incorrectos.
        puntaje (int): Entero obtenido por parametro que representa al puntaje obtenido en la ronda.
    """

    print("Letras seleccionadas:")
    mostrar_lista(lista_letras)

    print("Palabras ocultas:")
    mostrar_lista(lista_ocultas)

    if incorrectas > 0:
        print(f"Ingresos incorrectos: {incorrectas}")

    print(f"Puntuación total: {puntaje}")


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