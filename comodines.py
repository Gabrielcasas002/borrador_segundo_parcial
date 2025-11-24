# 💡 Comodines
# Durante la partida, el jugador dispone de 3 comodines de uso único, que podrá activar en cualquier momento:
# 2. 🔗 Ubicar letra: Selecciona una letra aleatoriamente y la ubicará en todas las palabras restantes.
# 3. 🧠 Comodín extra (A definir por el equipo).

from especificas import *
from diccionario_juego import *
import random


# 1. 🔍 Revelar palabra: Muestra parcialmente una de las palabras a descubrir.

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

def seleccionar_string_aleatoria(lista: list):

    indice = random.randint(0, len(lista) - 1)

    indice_string = lista[indice]

    return indice_string


def revelar_mitad(palabras_ingresadas: list, palabras_asociadas: list):

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



# 2. 🔗 Ubicar letra: Selecciona una letra aleatoriamente y la ubicará en todas las palabras restantes.

def ubicar_letra(lista_palabras: list, lista_descubiertas: list, lista_letras: list) -> list:

    palabras_ocultas = ocultar_palabras(lista_palabras, lista_descubiertas)

    letra = seleccionar_string_aleatoria(lista_letras)

    lista_ubicar = []

    for i in range(len(lista_palabras)):
        palabra_real = lista_palabras[i]
        palabra_oculta = palabras_ocultas[i]

        nueva = ""
        
        j = 0
        while j < len(palabra_real):

            if palabra_real[j] == letra:
                nueva += letra
            elif palabra_real[j] != letra:
                nueva += palabra_oculta[j]

            j += 1

        lista_ubicar.append(nueva)

    return lista_ubicar


# def combinar_listas(lista_ubicar: list, lista_revelada: list, lista_palabras: list) -> list:

#     lista = list()

#     for i in range(len(lista_revelada)):
#         palabra_revelada = lista_revelada[i]
#         palabra_ubicada = lista_ubicar[i]
#         palabra = lista_palabras[i]

#         palabra_combinada = ""

#         for j in range(len(palabra)):
#             caracter_ubicar = palabra_ubicada[j]
#             caracter_revelada = palabra_revelada[j]

#             if caracter_ubicar != "_" and caracter_ubicar == palabra[j]:
#                 palabra_combinada += caracter_ubicar
#             elif caracter_revelada != "_" and caracter_revelada == palabra[j]:
#                 palabra_combinada += caracter_revelada
#             else:
#                 palabra_combinada += "_"

#         lista.append(palabra_combinada)

#     return lista

def copiar_lista(lista: list):
    nueva = []
    for i in range(len(lista)):
        nueva.append(lista[i])
    return nueva


def ubicacion_valida(palabra_ubicada, palabra_real):
    bandera = True
    
    if palabra_ubicada == None:
        bandera = False

    elif len(palabra_ubicada) != len(palabra_real):
        bandera = False
    
    return bandera


def combinar_palabra(base_actual, palabra_real, palabra_ubicada):
    combinada = ""
    
    for i in range(len(palabra_real)):
        if palabra_ubicada[i] != "_":
            combinada += palabra_ubicada[i]
        elif palabra_ubicada[i] == "_":
            combinada += base_actual[i]
    
    return combinada


def combinar_listas_ubicar(lista_ubicar, base, lista_palabras):
    nueva_lista = []

    if lista_ubicar == None:
        nueva_lista = copiar_lista(base)

    else:
        for i in range(len(lista_palabras)):
            palabra_real = lista_palabras[i]
            base_actual = base[i]
            palabra_ubicada = lista_ubicar[i]
            bandera = ubicacion_valida(palabra_ubicada, palabra_real)

            if bandera == False:
                nueva_lista.append(base_actual)
            elif bandera == True:
                combinada = combinar_palabra(base_actual, palabra_real, palabra_ubicada)
                nueva_lista.append(combinada)

    return nueva_lista



#--------------------------------------PRUEBAS----------------------------------------------#


# nivel = diccionario_juego[0] 
# lista_letras = elegir_letras_juego(nivel)
# lista_palabras = elegir_palabras_juego(nivel, lista_letras)
# lista_descubiertas = []
# lista_ocultas = ocultar_palabras(lista_palabras, lista_descubiertas)
# lista_ubicar = ubicar_letra(lista_palabras, lista_descubiertas, lista_letras)
# lista_revelar = revelar_mitad(lista_ocultas, lista_palabras)
# lista = combinar_listas(lista_ubicar, lista_revelar, lista_palabras)
# print(lista_letras)
# print(lista_palabras)
# print(lista_ubicar)
# print(lista_revelar)
# print(lista)

