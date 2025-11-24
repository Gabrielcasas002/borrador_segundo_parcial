from funciones import *
from diccionario_juego import *
import time


# def jugar_partida(diccionario_juego: dict, diccionario_estadisticas: dict):
#     reinicios = 0 
#     nivel = 1

#     while nivel < 6 and reinicios < 3:

#         partida = jugar_palabras(diccionario_juego, nivel, diccionario_estadisticas)
    
#         if partida == False:
#             print(f"Felicidades ganaste el nivel {nivel}")
        
#             print("\nTus estadisticas son:\n")
        
#             mostrar_diccionario(diccionario_estadisticas)
        
#             print("\nPasando al siguiente nivel")
        
#             nivel += 1
    
#         elif partida == True:
#             print("Perdiste el nivel")
#             reinicios += 1
#             if reinicios < 3:
#                 print("Volviendo a empezar...")


#         os.system("pause")
#         os.system("cls")

#     if nivel == 6:
#         print("Felicidades ganaste la partida")
    
#         print("\nTus estadisticas finales son:\n")
        
#         mostrar_diccionario(diccionario_estadisticas)

#     elif reinicios == 3:
#         print("Perdiste la partida 😢")


#-----------------------------------------------------------------------------#

def mostrar_estado_partida(flag_partida: bool, nivel: int, reinicios: int, diccionario_estadisticas: dict):

    if flag_partida == False:
        print(f"Felicidades ganaste el nivel {nivel}")
        
        print("\nTus estadisticas son:\n")
        
        mostrar_diccionario(diccionario_estadisticas)
        
        print("\nPasando al siguiente nivel")
        
        nivel += 1
    
    elif flag_partida == True:
        print("Perdiste el nivel")
        reinicios += 1
        if reinicios < 3:
            print("Volviendo a empezar...")


def jugar_partida(diccionario_juego: dict, diccionario_estadisticas: dict):

    reinicios = 0 
    nivel = 1

    while nivel < 6 and reinicios < 3:

        partida = jugar_palabras(diccionario_juego, nivel, diccionario_estadisticas)
    
        mostrar_estado_partida(partida, nivel, reinicios, diccionario_estadisticas)

        os.system("pause")
        os.system("cls")

    if nivel == 6:
        print("Felicidades ganaste la partida")
    
        print("\nTus estadisticas finales son:\n")
        
        mostrar_diccionario(diccionario_estadisticas)

    elif reinicios == 3:
        print("Perdiste la partida 😢")

jugar_partida(diccionario_juego, diccionario_estadisticas)