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

    if estado_comodines[0] == False and estado_comodines[1] == False and estado_comodines[2] == False:
        print("Ingrese [1] para usar Revelar Palabra\n")
        print("Ingrese [2] para usar Ubicar Letras\n")
        print("Ingrese [3] para usar comodin Ta-Te-Ti\n")


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


def actualizar_ocultas(lista_palabras: list, palabras_ingresadas: list, lista_ubicar: list, lista_revelar: list, estado_comodines: list) -> list:
    """_summary_

    Modifica la lista de palabras ocultas, y aplica el efecto del comodin ubicar letra
    si es activado
    
    Funciona en dos etapas:
        1. Oculta normalmente las palabras no adivinadas.
        
        2. Si el comodín 'Ubicar letra' está activo, combina la ocultación
        con la letra ubicada usando `combinar_listas_ubicar`.

    Args:
        lista_palabras (list): Lista original de todas las palabras de la ronda.
        palabras_ingresadas (list): Lista de palabras ya adivinidadas.
        lista_ubicar (list): Lista donde se guarda el resultados del segundo comodin.
        lista_revelar (list): Lista donde se guarda el resultados del primer comodin.
        estado_comodines (list): Lista que indica si el comodín fue usado.

    Returns:
        list: la funcion retorna la lista combinada con el efecto del comodin. Si el comodin ya fue utilizado solo retorna una lista de palabras ocultas.
    """

    lista_ocultas_base = ocultar_palabras(lista_palabras, palabras_ingresadas)

    combinada = lista_ocultas_base

    if estado_comodines[0] and not estado_comodines[1]:
        combinada = combinar_listas_ubicar(lista_revelar, lista_ocultas_base, lista_palabras)

    if estado_comodines[1] and not estado_comodines[0]:
        combinada = combinar_listas_ubicar(lista_ubicar, lista_ocultas_base, lista_palabras)

    if estado_comodines[0] and estado_comodines[1]:

        mitad = combinar_listas_ubicar(lista_revelar, lista_ocultas_base, lista_palabras)
        ubicar = combinar_listas_ubicar(lista_ubicar, lista_ocultas_base, lista_palabras)
        combinada = combinar_listas(ubicar, mitad, lista_palabras)

    return combinada


def obtener_ingreso(estado_comodines: list) -> str:
    """_summary_

    Args:
        estado_comodines (list): Lista de banderas recibida por parametro.

    Returns:
        str: La funcion le pide un dato al usuario y dependiendo del estado de la bandera, le mostrará un mensaje avisandole que puede usar un comodin.
             Finalmente, retorna el dato ingresado por el usuario.
    """

    if estado_comodines[0] == False and estado_comodines[1] == False and estado_comodines[2] == False:
        ingreso = input("Ingrese una palabra. [1] o [2] o [3] para Comodines: ")
    
    elif estado_comodines[0] == False and estado_comodines[1] == False and estado_comodines[2] == True:
        ingreso = input("Ingrese una palabra, [1] o [2] para usar Revelar o Ubicar: ")
    
    elif estado_comodines[0] == False and estado_comodines[1] == True and  estado_comodines[2] == False:
        ingreso = input("Ingrese una palabra, [1] o [3] para usar Revelar o Ta-te-ti: ")
    
    elif estado_comodines[0] == True and estado_comodines[1] == False and  estado_comodines[2] == False:
        ingreso = input("Ingrese una palabra, [2] o [3] para usar Ubicar Letras o Ta-te-ti: ")
    
    elif estado_comodines[0] == False and estado_comodines[1] == True and  estado_comodines[2] == True:
        ingreso = input("Ingrese una palabra, [1] para usar Revelar Palabra: ")

    elif estado_comodines[0] == True and estado_comodines[1] == False and  estado_comodines[2] == True:
        ingreso = input("Ingrese una palabra o [2] para usar Ubicar Letras: ")

    elif estado_comodines[0] == True and estado_comodines[1] == True and  estado_comodines[2] == False:
        ingreso = input("Ingrese una palabra o [3] para usar Comodin Ta-te-ti: ")
    
    else:
        ingreso = input("Ingrese una palabra: ")

    return ingreso


