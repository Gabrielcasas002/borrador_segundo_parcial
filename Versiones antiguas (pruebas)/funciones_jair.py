from diccionario_juego import *
from guardar_usuarios import *
import os
import random
import time


def elegir_letras(diccionario: dict) -> list:

    indice = random.randint(0, len(diccionario) - 1)
    lista_letras = diccionario[indice]["letras"]

    return lista_letras


def elegir_palabras(diccionario: dict, letras: list) -> list:

    for i in range(len(diccionario)):

        if diccionario[i]["letras"] == letras:

            lista_palabras = diccionario[i]["palabras"]

    return lista_palabras


def sumar_puntaje(puntaje: int, puntos: int, ingresar: int):

    puntaje += len(ingresar) * puntos

    return puntaje


def jugar_descifrar_palabras(ingresar: str, palabras: list, lista_palabras_ingresadas: list):

    bandera  = False

    for respuesta in range(len(palabras)):
        if palabras[respuesta] == ingresar:
           lista_palabras_ingresadas.append(ingresar)
           palabras.remove(palabras[respuesta])
           bandera = True
           break

    return bandera


def mostrar_estado_ronda(lista_palabras, contador, puntuacion_total):

    mostrar_lista(lista_palabras)

    print(f"Palabras Incorrectas: {contador}")

    print("Total de puntos:", puntuacion_total)


def nivel_actual(ronda: int) -> str:

    for i in range(ronda + 1):
        if i == ronda:
            print(f"Nivel {i + 1}")
            break


def mostrar_lista(matriz: list) -> list:

    for i in range(len(matriz)):
        print(matriz[i], end= " ")
    print()


def listar_palabras(palabras_asociadas: list, palabras_descubiertas: list):

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
            ocultas.append("" * len(palabras_total[i]))

    return ocultas


def estado_nivel(bandera: bool, ronda: int):

    if bandera == True and ronda < 6:
        ronda += 1

    return ronda


def limpiar_lista(diccionario: list, lista_letras: list, lista_palabras: list):

    for i in range(len(diccionario)):
        seccion = diccionario[i]
        if seccion["letras"] == lista_letras and seccion["palabras"] == lista_palabras:
            diccionario.remove(seccion)
            break


def sumar_estadisticas(diccionario_stats: dict, puntuacion_ronda: int, cantidad_de_ingresos_incorrectos: int, tiempo_restante: int):

 
    diccionario_stats["Puntuacion Total"] += puntuacion_ronda
    diccionario_stats["Ingresos incorrectos"] += cantidad_de_ingresos_incorrectos
    diccionario_stats["Tiempo total"] += tiempo_restante


def mostrar_diccionario(diccionario: dict):

    for clave in diccionario.keys():
       print(f"{clave} : {diccionario[clave]}")


def jugar_palabras(diccionario: dict, nivel: int, estadisticas: dict):
    
    lista_palabras_ingresadas = list()

    letras_seleccionadas = elegir_letras(diccionario)
    palabras_asociadas = elegir_palabras(diccionario, letras_seleccionadas)
    contador_palabras_incorrectas = 0
    bandera = True
    puntuacion_total = 0
    tiempo_inicio = time.time()

    while bandera ==  True:

        nivel_actual(nivel)
        
        if time.time() - tiempo_inicio > 90:
            print("\nSe termino el tiempo !")
            break


        print("Letras seleccionadas:")
        mostrar_lista(letras_seleccionadas)
        
        print("Palabras ocultas:")
        ocultas = ocultar_palabras(palabras_asociadas, lista_palabras_ingresadas)
        mostrar_lista(ocultas)
        
        if contador_palabras_incorrectas > 0:
            print(f"Cantidad de ingresos incorrectos: {contador_palabras_incorrectas}")

        ingresar = input("\nIngrese una palabra: ")
        
        tiempo_total_ronda = time.time() - tiempo_inicio
        tiempo_restante = int(90 - tiempo_total_ronda)

        acierto = jugar_descifrar_palabras(ingresar, palabras_asociadas, lista_palabras_ingresadas) 
        
        if acierto == True:

            puntuacion_parcial = sumar_puntaje(puntaje, puntos, ingresar)
            puntuacion_total += puntuacion_parcial

            print(f"Ganaste: {puntuacion_parcial} Puntos")
            print(f"Tiempo restante: {tiempo_restante} segundos")

        elif acierto == False:

            contador_palabras_incorrectas += 1
            print("Palabra Incorrecta")   
        
        print("Puntuacion total:",puntuacion_total)
        
        os.system("pause")
        os.system("cls")


        if len(palabras_asociadas) == 0:
            print("GANASTE")
            print(f"Puntuacion de esta ronda: {puntuacion_total}")
            print(f"Tiempo restante: {tiempo_restante} segundos")
            limpiar_lista(diccionario, letras_seleccionadas, palabras_asociadas)
            sumar_estadisticas(estadisticas, puntuacion_total, contador_palabras_incorrectas, tiempo_restante)
            bandera = False
            break
    
    return bandera



#---------------------------------------------------------------------------#

# jugando_descifrar_palabra(diccionario_juego)