from funciones_jugar_tateti import *

def usar_comodin_tateti(estado_bandera: dict, resultado_partida: bool, estadisticas: dict):

    if estado_bandera[2] == False:
        estado_bandera[2] = True

        valor = jugar_tateti(grilla)

        if valor == 1: 
            estadisticas["Puntuacion Total"] += 500
            resultado_partida = True
            print("\nGanaste 500 puntos")
            print("Pasaste a la siguiente ronda\n")

        elif valor == 2: 
            resultado_partida = False
            print("\nPerdiste. Reiniciando el nivel...")
            
            os.system("pause")
            os.system("cls")

        else:
            print("\nEmpate ! Reiniciando el nivel...")
            resultado_partida = False
    
            os.system("pause")
            os.system("cls")
    
    else:
        print(f"El comodin 3 -Jugar Tateti- Ya fue usado")

    
    return resultado_partida