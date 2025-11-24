from guardar_usuarios import *
from funciones_comodines import *
import random
import time


def jugar_descifrar_palabras(ingresar: str, palabras: list, lista_palabras_ingresadas: list) -> bool:
    """_summary_

    Args:
        ingresar (str): _description_
        palabras (list): _description_
        lista_palabras_ingresadas (list): _description_

    Returns:
        bool: _description_
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
        lista_palabras (list): _description_
        incorrectas (int): _description_
        puntuacion_total (int): _description_
    """

    mostrar_lista(lista_palabras)

    print(f"Palabras Incorrectas: {incorrectas}")

    print("Total de puntos:", puntuacion_total)


def mostrar_lista(matriz: list) -> list:
    """_summary_

    Args:
        matriz (list): _description_

    Returns:
        list: _description_
    """

    for i in range(len(matriz)):
        print(matriz[i], end= " ")
    print()


def listar_palabras(palabras_asociadas: list, palabras_descubiertas: list) -> list:
    """_summary_

    Args:
        palabras_asociadas (list): _description_
        palabras_descubiertas (list): _description_

    Returns:
        list: _description_
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


# def eliminar_repetidas(lista_palabras: list) -> list:
#     vistas = []
#     resultado = []

#     for i in range(len(lista_palabras)):
#         palabra = lista_palabras[i]

#         repetida = False
#         for j in range(len(vistas)):
#             if palabra == vistas[j]:
#                 repetida = True
#                 break

#         if repetida == False:
#             vistas.append(palabra)
#             resultado.append(palabra)

#     return resultado


# def listar_palabras(palabras_asociadas: list, palabras_descubiertas: list) -> list:
#     palabras_total = []

#     # agregar todas las asociadas
#     for i in range(len(palabras_asociadas)):
#         palabras_total.append(palabras_asociadas[i])

#     # agregar todas las descubiertas
#     for i in range(len(palabras_descubiertas)):
#         palabras_total.append(palabras_descubiertas[i])

#     # eliminar repetidas
#     palabras_total = eliminar_repetidas(palabras_total)

#     return palabras_total


def estado_nivel(bandera: bool, ronda: int) -> int:
    """_summary_

    Args:
        bandera (bool): _description_
        ronda (int): _description_

    Returns:
        int: _description_
    """
    
    if bandera == True and ronda < 6:
        ronda += 1

    return ronda


def sumar_estadisticas(estadisticas: dict, puntuacion_ronda: int, cantidad_de_ingresos_incorrectos: int, tiempo_restante: int, contador: int, tiempo_ronda: float):
    """_summary_

    Args:
        diccionario_stats (dict): _description_
        puntuacion_ronda (int): _description_
        cantidad_de_ingresos_incorrectos (int): _description_
        tiempo_restante (int): _description_
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
        diccionario (dict): _description_
    """

    for clave in diccionario.keys():
       print(f"{clave} : {diccionario[clave]}")


# MODIFICAR LA FUNCION limpiar_lista() PARA QUE RECIBA UN NIVEL Y BORRE LAS LISTAS CORRESPONDIENTES DE ESE DICCIONARIO...

def limpiar_lista(diccionario_juego: list, nivel: int, lista_letras: list, lista_palabras: list):

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


def ocultar_palabras(palabras_asociadas: list, palabras_descubiertas: list):
    """_summary_

    Args:
        palabras_asociadas (list): _description_
        palabras_descubiertas (list): _description_

    Returns:
        _type_: _description_
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

#---------------------------MODIFICACIONES--------------------------------------------------#


def elegir_letras_juego(nivel: dict) -> list:
    """_summary_

    Args:
        nivel (dict): _description_

    Returns:
        list: _description_
    """

    indice = random.randint(0, len(nivel["partidas"]) - 1)
    lista_letras = nivel["partidas"][indice]["letras"]

    return lista_letras


def elegir_palabras_juego(nivel: dict, letras: list) -> list:
    """_summary_

    Args:
        nivel (dict): _description_
        letras (list): _description_

    Returns:
        list: _description_
    """

    palabras = []
    partidas = nivel["partidas"]

    for i in range(len(partidas)):
        if partidas[i]["letras"] == letras:
            palabras = partidas[i]["palabras"]
    
    return palabras


def sumar_puntaje(ingresar: str) -> int:
    """_summary_

    Args:
        ingresar (str): _description_

    Returns:
        int: _description_
    """

    puntos = len(ingresar) * 20

    return puntos


#-----------------------NUEVAS-FUNCIONES--------------------------#


def finalizar_partida(puntaje: int, incorrectas: int, tiempo_restante: int, estadisticas: dict, contador: int, tiempo_inicio: float):
    """_summary_

    Args:
        puntaje (int): _description_
        incorrectas (int): _description_
        tiempo_restante (int): _description_
        estadisticas (dict): _description_
    """
    tiempo_total_ronda = time.time() - tiempo_inicio

    print("Ganaste La Partida !!!")
    print(f"Puntuación: {puntaje}")
    print(f"Tiempo restante: {tiempo_restante}")

    sumar_estadisticas(estadisticas, puntaje, incorrectas, tiempo_restante, contador, tiempo_total_ronda)

    

def procesar_ingreso(ingreso: str, lista_palabras: list, lista_ingresadas: list) -> int:
    """_summary_

    Args:
        ingreso (str): _description_
        lista_palabras (list): _description_
        lista_ingresadas (list): _description_

    Returns:
        int: _description_
    """

    print("")
    acierto = jugar_descifrar_palabras(ingreso, lista_palabras, lista_ingresadas)
    puntos = 0

    if ingreso == "1" or ingreso == "2":
        print("¡ Comodin Utilizado !")

    if acierto:
        puntos = len(ingreso) * 20
        print(f"Ganaste {puntos} puntos")        
    else:
        print("Palabra incorrecta.")

    return puntos

# Ejemplos de uso

# puntos = procesar_ingreso(ingreso, disponibles, ingresadas)
# puntaje_total += puntos


def calcular_tiempo(tiempo_inicio: float, tiempo_limite: int) -> float:
    """_summary_

    Args:
        tiempo_inicio (float): _description_
        tiempo_limite (int): _description_

    Returns:
        float: _description_
    """

    transcurrido = time.time() - tiempo_inicio
    tiempo_restante = tiempo_limite - transcurrido

    return tiempo_restante

# tiempo_restante = calcular_tiempo(tiempo_inicio, tiempo_limite)


def mostrar_estado_partida(lista_letras: list, lista_ocultas: list, incorrectas: int, puntaje: int):
    """_summary_

    Args:
        lista_letras (list): _description_
        lista_ocultas (list): _description_
        incorrectas (int): _description_
        puntaje (int): _description_
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
        lista_original (list): _description_

    Returns:
        list: _description_
    """

    nueva_lista = list()

    for i in range(len(lista_original)):
        nueva_lista.append(lista_original[i])

    return nueva_lista


def transformar_a_mayusculas(cadena: str) -> str:
    """_summary_

    Args:
        cadena (str): _description_

    Returns:
        str: devuelve la cadena transformada a mayusculas. funciona como un .upper()
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