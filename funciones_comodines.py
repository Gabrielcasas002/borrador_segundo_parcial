from comodines import *
from especificas import *


def mostrar_comodines(estado_comodines):

    if estado_comodines[0] == False:
        print("Ingrese [1] para usar Revelar Palabra")
    else:
        print("El comodín Revelar Palabra ya fue usado.")

    if estado_comodines[1] == False:
        print("Ingrese [2] para usar Ubicar Letras\n")
    else:
        print("El comodín Ubicar Letras ya fue usado.\n")


def usar_comodines(estado_comodines: dict, ingreso: str):


    if ingreso == "1" and estado_comodines[0] == False:
        estado_comodines[0] = True

    elif ingreso == "2" and estado_comodines[1] == False:
        estado_comodines[1] = True

    else:
        print("Ese comodín ya fue usado.")
    
