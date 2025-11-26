from guardar_usuarios import *
from funciones_comodines import *
import random
import time


def jugar_descifrar_palabras(ingresar: str, palabras: list, lista_palabras_ingresadas: list) -> bool:
    """_summary_

    Args:
        ingresar (str): String recibido por parametro que representa un dato ingresado por el usuario.
        palabras (list): Lista de palabras recibida por parametro.
        lista_palabras_ingresadas (list): Lista de palabras ingresadas por el usuario recibida por paremtero

    Returns:
        bool: La funcion verifica si el string (ingresar) se encunetra en la lista de palabras, si la encuentra, la agrega a la lista de palabras ingresadas y la elimina de la lista de palabras.
              Ademas, la funcion retorna una bandera que cambia su estado a True si la palabra ingresada por el usuario fue encontrada.
    """

    bandera  = False

    for respuesta in range(len(palabras)):
        if palabras[respuesta] == ingresar:
           lista_palabras_ingresadas.append(ingresar)
           palabras.remove(palabras[respuesta])
           bandera = True
           break

    return bandera


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


def sumar_estadisticas(estadisticas: dict, puntuacion_ronda: int, cantidad_de_ingresos_incorrectos: int, tiempo_restante: int, contador: int, tiempo_ronda: float):
    """_summary_

    Args:
        estadisticas (dict): Diccionario recibido por parametro que representa las estadisticas del juego.
        puntuacion_ronda (int): Entero recibido por parametro que representa la puntuacion obtenida en la ronda.
        cantidad_de_ingresos_incorrectos (int): Entero recibido por parametro que representa la cantidad de ingresos incorrectos obtenidos en la ronda.
        tiempo_restante (int): Entero recibido por parametro que representa el tiempo restante en la ronda. 
        contador (int): Entero obtenido por parametro que representa al contador de la partida.
        tiempo_ronda (float): Flotante obtenido por parametro que representa el tiempo obtenido en la ronda.
    """
    contador += 1
    tiempo_entre_niveles = 0
    tiempo_entre_niveles += int(tiempo_ronda)

    estadisticas["Puntuacion Total"] += puntuacion_ronda
    estadisticas["Ingresos incorrectos"] += cantidad_de_ingresos_incorrectos
    estadisticas["Tiempo restante total en segundos"] += tiempo_restante
    estadisticas["Tiempo entre niveles"] += tiempo_entre_niveles
    
    promedio_entre_niveles = estadisticas["Tiempo entre niveles"]
    
    estadisticas["Tiempo promedio entre niveles"] = promedio_entre_niveles / contador


def mostrar_diccionario(diccionario: dict):
    """_summary_

    Args:
        diccionario (dict): Diccionario obtenido por parametro que se mostrará sus claves y el contenido de cada una de ellas. 
    """

    for clave in diccionario.keys():
       print(f"{clave} : {diccionario[clave]}")


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

# Referencia
def elegir_letras_juego(nivel: dict) -> list:
    """_summary_

    Args:
        nivel (dict): Diccionario recibido por parametro que representa a un nivel del juego que contiene 3 listas de letras.

    Returns:
        list: La funcion selecciona una de esas 3 listas al azar y la retorna en una nueva lista.
    """

    indice = random.randint(0, len(nivel["partidas"]) - 1)
    lista_letras = nivel["partidas"][indice]["letras"]

    return lista_letras

# Referencia
def elegir_palabras_juego(nivel: dict, letras: list) -> list:
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


def finalizar_partida(puntaje: int, incorrectas: int, tiempo_restante: int, estadisticas: dict, contador: int, tiempo_inicio: float):
    """_summary_

    Args:
        puntaje (int): Entero recibido por parametro que representa el puntaje obtenido en el juego.
        incorrectas (int): Entero recibido por parametro que representa la cantidad de ingresos incorrectos obtenidos en el juego.
        tiempo_restante (int): Entero recibido por parametro que representa el tiempo restante obtenido en el juego.
        estadisticas (dict): Diccionario recibido por parametro que contiene las estadisticas obtenidas en el juego y donde se guardarán todos los datos.
        contador (int): Entero recibido por parametro que representa el contador utilizado obtenido en el juego.
        tiempo_inicio (float): Flotante recibido por parametro que representa el tiempo de inicio del juego.
    """

    tiempo_total_ronda = time.time() - tiempo_inicio

    print("Ganaste La Partida !!!")
    print(f"Puntuación: {puntaje}")
    print(f"Tiempo restante: {tiempo_restante}")

    sumar_estadisticas(estadisticas, puntaje, incorrectas, tiempo_restante, contador, tiempo_total_ronda)

    

def procesar_ingreso(ingreso: str, lista_palabras: list, lista_ingresadas: list) -> int:
    """_summary_

    Args:
        ingreso (str): String recibido por parametro que representa a un dato ingresado por el usuario.
        lista_palabras (list): Lista de palabras recibida por parametro.
        lista_ingresadas (list): lista de palabras ingresadas por el usuario recibida por parametro.

    Returns:
        int: La funcion utiliza los datos obtenidos para generar una bandera. Si la bandera es True, la funcion calcula los puntos, lo muestra y lo retorna. 
    """

    print("")
    acierto = jugar_descifrar_palabras(ingreso, lista_palabras, lista_ingresadas)
    puntos = 0

    if acierto:
        puntos = len(ingreso) * 20
        print(f"Ganaste {puntos} puntos")        
    else:
        print("Palabra incorrecta.")

    return puntos


def calcular_tiempo(tiempo_inicio: float, tiempo_limite: int) -> float:
    """_summary_

    Args:
        tiempo_inicio (float): Flotante recibido por parametro que representa al tiempo de inicio de la partida.
        tiempo_limite (int): Entero recibido por parametro que representa al tiempo limite de la partida.

    Returns:
        float: La funcion retorna un flotante que representa al tiempo restante de la partida.
    """

    transcurrido = time.time() - tiempo_inicio
    tiempo_restante = tiempo_limite - transcurrido

    return tiempo_restante


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


def transformar_a_mayusculas(cadena: str) -> str:
    """_summary_

    Args:
        cadena (str): String recibido por parametro que sera recorrido elemento por elemento.

    Returns:
        str: devuelve la cadena transformada a mayusculas. su funcion es hacer lo mismo que el comando .upper()
    """

    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    cadena_mayuscula = ""

    for i in range(len(cadena)):
        letra = cadena[i]

        for j in range(len(minusculas)):

            if letra == minusculas[j]:
                cadena_mayuscula += mayusculas[j]

            elif letra == mayusculas[j]:
                cadena_mayuscula += letra

    return cadena_mayuscula


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


def obtener_ingreso(estado_comodines: list) -> str:
    """_summary_

    Args:
        estado_comodines (list): Lista de banderas recibida por parametro.

    Returns:
        str: La funcion le pide un dato al usuario y dependiendo del estado de la bandera, le mostrará un mensaje avisandole que puede usar un comodin.
             Finalmente, retorna el dato ingresado por el usuario.
    """

    estado_comodin_ubicar = estado_comodines[1]

    if estado_comodin_ubicar:
        ingreso = input("Ingrese una palabra: ")
    else:
        ingreso = input("Ingrese una palabra o [2] para usar Ubicar Letras: ")

    return ingreso


def verificar_ingreso(ingreso: str, palabras_disponibles: list, palabras_ingresadas: list) -> int:
    """_summary_

    Args:
        ingreso (str): String recibido por parametro que representa a un dato ingresado por el usuario.
        palabras_disponibles (list): Lista de palabras obtenida por parametro.
        palabras_ingresadas (list): Lista de palabras ingresadas por el usuario recibida por parametro.

    Returns:
        int: La funcion utiliza los datos recibidos, transforma el string en mayusculas y luego verifica el string para ver si se encuentra en la lista de palabras.
             Finalmente, retorna los puntos obtenidos si los hay.
    """

    ingreso_mayuscula = transformar_a_mayusculas(ingreso)
    puntos = procesar_ingreso(ingreso_mayuscula,palabras_disponibles,palabras_ingresadas)

    return puntos
