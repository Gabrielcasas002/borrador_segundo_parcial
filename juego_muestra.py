from especificas import *
from diccionario_juego import *
from comodines import *
from funciones_comodines import *
from borrador_csv import *
import os
import time


def jugar_palabras(diccionario: dict, nivel: int, estadisticas: dict, contador: int) -> bool:

    nivell_actual = elegir_nivel(diccionario, nivel)
    lista_letras = elegir_letras_nivel(nivell_actual)
    lista_palabras = elegir_palabras_nivel(nivell_actual, lista_letras)
    estado_comodines = nivell_actual["estado_comodines"]

    lista_ubicar = None

    palabras_ingresadas = []
    palabras_disponibles = copiar_lista(lista_palabras)

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
        else:

            if estado_comodines[1] == False:
                ocultas = ocultar_palabras(lista_palabras, palabras_ingresadas)
            else:
                base = ocultar_palabras(lista_palabras, palabras_ingresadas)
                ocultas = combinar_listas_ubicar(lista_ubicar, base, lista_palabras)

            mostrar_estado_partida(lista_letras, ocultas, incorrectas, puntaje_total)

            if estado_comodines[1] == False:
                ingreso = input("Ingrese una palabra o [2] para usar Ubicar Letras: ")
            
            else :
                ingreso = input("Ingrese una palabra: ")
            
            procesar = True

            if ingreso == "2":
                procesar = False

                if estado_comodines[1] == False:
                    lista_ubicar = ubicar_letra(lista_palabras, palabras_ingresadas, lista_letras)
                    estado_comodines[1] = True
                    print("\nComodín 'Ubicar letras' aplicado!")
                else:
                    print("El comodín Ubicar Letras ya fue usado.")

                os.system("pause")
                os.system("cls")

            if procesar:

                ingreso_mayuscula = transformar_a_mayusculas(ingreso)
                puntos = procesar_ingreso(ingreso_mayuscula,palabras_disponibles,palabras_ingresadas)

                if puntos > 0:
                    puntaje_total += puntos
                    print("Tiempo restante:", int(tiempo_restante))
                    print(contador)
                else:
                    incorrectas += 1
                    print("Tiempo restante:", int(tiempo_restante))

                os.system("pause")
                os.system("cls")

            if len(palabras_disponibles) == 0:
                limpiar_lista(diccionario, nivel, lista_letras, lista_palabras)
                finalizar_partida(puntaje_total, incorrectas, int(tiempo_restante), estadisticas, contador, tiempo_inicio)
                resultado_partida = True
                bandera = False

    return resultado_partida



def jugar_nivel(diccionario: dict, nivel_actual: int, estadisticas: dict, contador: int) -> bool:

    rondas = 0
    completar_nivel = True
    nivel_diccionario = diccionario[nivel_actual - 1]

    while rondas < 3:

        os.system("cls")
        print(f"\nNivel {nivel_actual}\n")
        print(f"Ronda {rondas + 1} / 3\n")

        estado_comodines = nivel_diccionario["estado_comodines"]

        mostrar_comodines(estado_comodines)

        bandera_ronda = jugar_palabras(diccionario, nivel_actual, estadisticas, contador)

        if bandera_ronda:

            os.system("pause")

        if bandera_ronda:
            rondas += 1
            contador += 1
        else:
            completar_nivel = False
            rondas = 3    

    os.system("cls")

    return completar_nivel


def jugar_juego(diccionario: list[dict], estadisticas: dict) -> bool:

    nivel = 1
    reinicios = 0
    limite_reinicios = 3
    bandera = True
    juego_ganado = False
    contador = 0

    crear_csv(diccionario)
    diccionario_juego = reconstruir_diccionario("diccionario_juego.csv")

    while nivel <= 5 and bandera:

        nivel_completo = jugar_nivel(diccionario_juego, nivel, estadisticas, contador)


        if not nivel_completo:
            reinicios += 1
            print(f"Cantidad de Reinicios: ({reinicios}/{limite_reinicios})")
            os.system("pause")
            os.system("cls")

        if reinicios == limite_reinicios:
            print("\nAlcanzaste el límite de reinicios.")
            bandera = False
            
            print(f"\nEstadisticas Finales:\n")
            mostrar_diccionario(estadisticas)
            
            os.system("pause")
            os.system("cls")

        if bandera and nivel_completo:
            nivel += 1
            contador += 3
            print(f"\nEstadisticas Juego:\n")
            mostrar_diccionario(estadisticas)

            os.system("pause")
            os.system("cls")

        if nivel == 6:
            juego_ganado = True
            bandera = False
            print(f"\nEstadisticas Finales:\n")
            mostrar_diccionario(estadisticas)
            
            os.system("pause")
            os.system("cls")

    return juego_ganado