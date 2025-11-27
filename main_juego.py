from juego_muestra import *

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
    diccionario_jueguito = reconstruir_diccionario("diccionario_juego.csv")

    while nivel <= 5 and bandera:

        nivel_completo = jugar_nivel(diccionario_jueguito, nivel, estadisticas, contador)


        if not nivel_completo:
            reinicios += 1
            print(f"Cantidad de Reinicios: ({reinicios}/{limite_reinicios})")
            os.system("pause")
            os.system("cls")

        if reinicios == limite_reinicios:
            print("\nAlcanzaste el límite de reinicios.")
            bandera = False
            
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

    return juego_ganado