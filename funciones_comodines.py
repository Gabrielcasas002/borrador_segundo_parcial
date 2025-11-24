from comodines import *
from especificas import *
import os


def mostrar_comodines(estado_comodines):

    # if estado_comodines[0] == False:
    #     print("Ingrese [1] para usar Revelar Palabra")
    # else:
    #     print("El comodín Revelar Palabra ya fue usado.")

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
    
def usar_comodin_revelar(estado_comodines: bool, lista_palabras: list, palabras_ingresadas: list, lista_letras: list, lista_ubicar: list):

    if estado_comodines[1] == False:
        lista_ubicar = ubicar_letra(lista_palabras, palabras_ingresadas, lista_letras)
        estado_comodines[1] = True
        print("\nComodín 'Ubicar letras' aplicado!")
    else:
        print("El comodín Ubicar Letras ya fue usado.")

    os.system("pause")
    os.system("cls")
    
    return lista_ubicar


def actualizar_ocultas(lista_palabras, palabras_ingresadas, lista_ubicar, estado_comodines):

    estado_comodin_ubicar = estado_comodines[1]

    lista_ocultas_base = ocultar_palabras(lista_palabras, palabras_ingresadas)
    combinada = lista_ocultas_base
    if estado_comodin_ubicar:
        combinada = combinar_listas_ubicar(lista_ubicar, lista_ocultas_base, lista_palabras)

    return combinada