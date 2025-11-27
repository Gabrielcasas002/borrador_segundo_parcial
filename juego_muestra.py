from especificas import *
from diccionario_juego import *
from funciones_comodines import *
from archivos_csv import *
from comodin_extra import *
import os

def jugar_palabras(diccionario: dict, nivel: int, estadisticas: dict, contador: int, partidas_temporales: list) -> bool:
    """_summary_

    Juega una ronda completa del juego, eligiendo las letras, palabras del nivel
    La funcion: asigna el tiempo de la ronda, el estado y uso de los comodines, controla las palabras ingresadas
    calcula el puntaje del ingreso, y la cantidad de ingresos incorrectos
    Finaliza la ronda si es que gano o perdio por tiempo, y actualiza las estadisticas en el diccionario estadisticas.

    Args:
        diccionario (dict): Diccionario del juego que contiene todas las palabras, niveles, letas, etc del juego
        nivel (int): Nivel actual a jugar 
        estadisticas (dict): Diccionario donde se guardan las estadisticas de la partida
        contador (int): Contador que cuenta cuantas rondas se jugaron 
        partidas_temporales (list): Lista de diccionario obtenida por parametro utilizada para cada ronda.

    Returns:
        bool: True si la ronda fue completada correctamente
              False si terminó por tiempo 
    """

    partida_actual = partidas_temporales.pop(0)

    lista_letras = copiar_lista(partida_actual["letras"])
    lista_palabras = copiar_lista(partida_actual["palabras"])

    estado_comodines = diccionario[nivel - 1]["estado_comodines"]

    lista_revelar = None
    lista_ubicar = None

    palabras_ingresadas = []
    palabras_disponibles = copiar_lista(lista_palabras)

    ocultas = ocultar_palabras(lista_palabras, palabras_ingresadas)

    incorrectas = 0
    puntaje_total = 0

    tiempo_inicio = time.time()
    tiempo_limite = 17

    bandera = True
    resultado_partida = False

    while bandera:

        tiempo_restante = calcular_tiempo(tiempo_inicio, tiempo_limite)

        if tiempo_restante <= 0:
            print("\nSe terminó el tiempo !!!")
            sumar_estadisticas(estadisticas, puntaje_total, incorrectas, tiempo_restante, contador, tiempo_limite)
            bandera = False
        
        else:
            ocultas = actualizar_ocultas(lista_palabras,palabras_ingresadas,lista_ubicar,lista_revelar,estado_comodines)

            mostrar_estado_partida(lista_letras, ocultas, incorrectas, puntaje_total)

            ingreso = obtener_ingreso(estado_comodines)
            procesar = True
            
            if ingreso == "1":
                procesar = False
                lista_revelar = usar_comodin_revelar(estado_comodines,lista_palabras,palabras_ingresadas,lista_revelar)

            elif ingreso == "2":
                procesar = False
                lista_ubicar = usar_comodin_ubicar(estado_comodines,lista_palabras,palabras_ingresadas,lista_letras,lista_ubicar)
            
            elif ingreso == "3":
                procesar = False
                resultado_partida = usar_comodin_tateti(estado_comodines, resultado_partida, diccionario_estadisticas)
                break

            if procesar:
                puntos = verificar_ingreso(ingreso,palabras_disponibles,palabras_ingresadas)

                if puntos > 0:
                    puntaje_total += puntos
                else:
                    incorrectas += 1

                print("Tiempo restante:", int(tiempo_restante))
                os.system("pause")
                os.system("cls")

            if len(palabras_disponibles) == 0:
                finalizar_partida(puntaje_total,incorrectas,int(tiempo_restante),estadisticas,contador,tiempo_inicio)
                resultado_partida = True
                bandera = False

    return resultado_partida


def jugar_nivel(diccionario: dict, nivel_actual: int, estadisticas: dict, contador: int) -> bool:
    """_summary_

    Juega las 3 rondas correspondientes al nivel del juego, mostrando los comodines disponibles.
    Y muestra en que nivel y ronda esta jugando el usuario

    Args:
        diccionario (dict): Diccionario del juego que contiene todas las palabras, niveles, letas, etc del juego
        nivel_actual (int): Numero del nivel que se esta jugando
        estadisticas (dict): Diccionario donde se guardan las estadisticas
        contador (int): Contador que cuenta el total de rondas jugas 

    Returns:
        bool: True si el jugador completa las 3 rondas del nivel,
              False si no completa el nivel.
    """

    rondas = 0
    completar_nivel = True
    nivel_diccionario = diccionario[nivel_actual - 1]

    partidas_temporales = copiar_lista(nivel_diccionario["partidas"])

    while rondas < 3:

        os.system("cls")
        print(f"\nNivel {nivel_actual}\n")
        print(f"Ronda {rondas + 1} / 3\n")

        estado_comodines = nivel_diccionario["estado_comodines"]
        mostrar_comodines(estado_comodines)

        bandera_ronda = jugar_palabras(diccionario,nivel_actual,estadisticas, contador, partidas_temporales)

        if bandera_ronda:
            os.system("pause")

        if bandera_ronda == True:
            rondas += 1
            contador += 1
        else:
            completar_nivel = False
            rondas = 3    

    os.system("cls")

    return completar_nivel
