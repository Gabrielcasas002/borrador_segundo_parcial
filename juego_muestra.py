from especificas import *
from diccionario_juego import *
from comodines import *
from funciones_comodines import *
from archivos_csv import *
import os
import time

def jugar_palabras(diccionario: dict, nivel: int, estadisticas: dict, contador: int) -> bool:
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

    Returns:
        bool: True si la ronda fue completada correctamente
              False si terminó por tiempo 
    """


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

            ocultas = actualizar_ocultas(lista_palabras, palabras_ingresadas, lista_ubicar, estado_comodines)

            mostrar_estado_partida(lista_letras, ocultas, incorrectas, puntaje_total)

            ingreso = obtener_ingreso(estado_comodines)
            
            procesar = True
            
            if ingreso == "2":

                procesar = False
                lista_ubicar = usar_comodin_ubicar(estado_comodines, lista_palabras, palabras_ingresadas, lista_letras, lista_ubicar)

            if procesar:

                puntos = verificar_ingreso(ingreso, palabras_disponibles, palabras_ingresadas)    
                if puntos > 0:
                    puntaje_total += puntos
                    print("Tiempo restante:", int(tiempo_restante))                
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

    while rondas < 3:

        os.system("cls")
        print(f"\nNivel {nivel_actual}\n")
        print(f"Ronda {rondas + 1} / 3\n")

        estado_comodines = nivel_diccionario["estado_comodines"]

        mostrar_comodines(estado_comodines)

        bandera_ronda = jugar_palabras(diccionario, nivel_actual, estadisticas, contador)

        if bandera_ronda:
            os.system("pause")

        if bandera_ronda == True:
            rondas += 1
            contador += 1
        elif bandera_ronda == False:
            completar_nivel = False
            rondas = 3    

    os.system("cls")

    return completar_nivel


def jugar_juego(diccionario: list[dict], estadisticas: dict) -> bool:
    """_summary_

    Controla e inicia el juego completo en un formato de 5 niveles

    Arma el csv que contiene el diccionario, lo reconstruye en formato de lista y lo usa para jugar al juego
    Admnistra el avance de niveles, controlando el limite de reinicios permitidos
    Muestra las estadisticas parciales y finales
    Y por ultima determina si el jugador gano o perdio.

    Args:
        diccionario (list[dict]): Diccionario base utilizado para generar el CSV con el que se va a jugar el juego.
        estadisticas (dict): Diccionario donde se van a guardar las estadisticas del nivel o partida

    Returns:
        bool: True si el jugador completa los 5 niveles del juego.
              False si alcanza el límite de reinicios
    """

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