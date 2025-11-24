from especificas import *
import os
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

def verificar_ingreso(ingreso: str, palabras_disponibles: list, palabras_ingresadas: list):
    ingreso_mayuscula = transformar_a_mayusculas(ingreso)
    puntos = procesar_ingreso(ingreso_mayuscula,palabras_disponibles,palabras_ingresadas)

    return puntos

def obtener_ingreso(estado_comodines):

    estado_comodin_ubicar = estado_comodines[1]

    if estado_comodin_ubicar:
        ingreso = input("Ingrese una palabra: ")
    else:
        ingreso = input("Ingrese una palabra o [2] para usar Ubicar Letras: ")

    return ingreso

def actualizar_ocultas(lista_palabras, palabras_ingresadas, lista_ubicar, estado_comodines):

    estado_comodin_ubicar = estado_comodines[1]

    lista_ocultas_base = ocultar_palabras(lista_palabras, palabras_ingresadas)
    combinada = lista_ocultas_base
    if estado_comodin_ubicar:
        combinada = combinar_listas_ubicar(lista_ubicar, lista_ocultas_base, lista_palabras)

    return combinada
