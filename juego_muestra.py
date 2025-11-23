from especificas import *
from diccionario_juego import *
from comodines import *
from funciones_comodines import *
import os
import time



def jugar_palabras(diccionario: dict, nivel: int, estadisticas: dict) -> bool:

    nivel_diccionario = diccionario[nivel - 1]
    estado_comodines = nivel_diccionario["estado_comodines"]

    lista_letras = elegir_letras_juego(nivel_diccionario)
    lista_palabras = elegir_palabras_juego(nivel_diccionario, lista_letras)

    palabras_ingresadas = []
    palabras_disponibles = copiar_lista(lista_palabras)

    lista_revelar = None
    lista_ubicar = None

    ocultas = ocultar_palabras(lista_palabras, palabras_ingresadas)

    incorrectas = 0
    puntaje_total = 0

    tiempo_inicio = time.time()
    tiempo_limite = 90

    bandera = True
    resultado_partida = False

    while bandera:

        tiempo_restante = calcular_tiempo(tiempo_inicio, tiempo_limite)

        if tiempo_restante <= 0:
            print("\nSe terminó el tiempo !!!")
            bandera = False

        if bandera:

            if not estado_comodines["revelar"] and not estado_comodines["ubicar"]:
                ocultas = ocultar_palabras(lista_palabras, palabras_ingresadas)

            elif estado_comodines["revelar"] and not estado_comodines["ubicar"]:
                ocultas = lista_revelar

            elif estado_comodines["ubicar"] and not estado_comodines["revelar"]:
                ocultas = lista_ubicar

            else:
                ocultas = combinar_listas(lista_ubicar, lista_revelar, lista_palabras)

            mostrar_estado_partida(lista_letras, ocultas, incorrectas, puntaje_total)

            ingreso = input("Ingrese una palabra: ")
            procesar_palabra = True


            if ingreso == "1" or ingreso == "2":

                procesar_palabra = False

                if ingreso == "1" and not estado_comodines["revelar"]:
                    lista_revelar = revelar_mitad(palabras_ingresadas, lista_palabras)
                    estado_comodines["revelar"] = True

                elif ingreso == "2" and not estado_comodines["ubicar"]:
                    lista_ubicar = ubicar_letra(lista_palabras, palabras_ingresadas, lista_letras)
                    estado_comodines["ubicar"] = True

                else:
                    print("Ese comodín ya fue usado.")

                os.system("pause")
                os.system("cls")

            if procesar_palabra:

                ingreso_mayuscula = transformar_a_mayusculas(ingreso)
                puntos = procesar_ingreso(ingreso_mayuscula, palabras_disponibles, palabras_ingresadas)

                if puntos > 0:
                    puntaje_total += puntos
                    print("Tiempo restante:", int(tiempo_restante))

                if puntos == 0:
                    incorrectas += 1

                os.system("pause")
                os.system("cls")

            if len(palabras_disponibles) == 0:
                limpiar_lista(diccionario, nivel, lista_letras, lista_palabras)
                finalizar_partida(puntaje_total, incorrectas, int(tiempo_restante), estadisticas)
                resultado_partida = True
                bandera = False

    return resultado_partida



def jugar_nivel(diccionario: dict, nivel_actual: int, estadisticas: dict) -> bool:

    rondas = 0
    completar_nivel = True

    nivel_diccionario = diccionario[nivel_actual - 1]

    while rondas < 3:

        print(f"\nRonda {rondas + 1} / 3")

        # 🔥 ESTA ERA LA FUNCIÓN QUE ROMPÍA
        mostrar_comodines(nivel_diccionario["estado_comodines"])

        bandera_ronda = jugar_palabras(diccionario, nivel_actual, estadisticas)

        if bandera_ronda:
            rondas += 1
        else:
            completar_nivel = False
            rondas = 3    

    return completar_nivel


def jugar_juego(diccionario_juego: list[dict], estadisticas: dict) -> bool:

    nivel = 1
    reinicios = 0
    limite_reinicios = 3
    bandera = True
    juego_ganado = False

    while nivel <= 5 and bandera:

        print(f"\nNivel {nivel}")

        nivel_completo = jugar_nivel(diccionario_juego, nivel, estadisticas)

        if not nivel_completo:
            reinicios += 1
            print(f"Cantidad de Reinicios: ({reinicios}/{limite_reinicios})")

        if reinicios == limite_reinicios:
            print("\nAlcanzaste el límite de reinicios.")
            bandera = False

        if bandera and nivel_completo:
            nivel += 1

        if nivel == 6:
            juego_ganado = True
            bandera = False

    return juego_ganado