from comodines import *
from especificas import *

bandera_ubicar_letra = False
# bandera = False
# bandera = False

# Falta agregar los demas comodines.

# def mostrar_comodines(diccionario: dict, bandera_uno: bool, bandera_dos: bool):

#     if diccionario["comodines"] == False:
#         if bandera_uno == False:
#             print("Ingrese [1] para usar el comodin Revelar Palabra")
#         if bandera_uno == True:
#             print("El Comodin Revelar Palabra [1] ya fue utilizado !")
#         if bandera_dos == False:
#             print("Ingrese [2] para usar el comodin Ubicar Letras")
#         if bandera_dos == True:
#             print("El Comodin Ubicar Palabra [2] ya fue utilizado !")
#     else:
#         print("Ya se usaron todos los comodines.")


def mostrar_comodines(estado_comodines: dict):

    if not estado_comodines["revelar"]:
        print("Ingrese [1] para usar Revelar Palabra")
    else:
        print("El comodín Revelar Palabra ya fue usado.")

    if not estado_comodines["ubicar"]:
        print("Ingrese [2] para usar Ubicar Letras")
    else:
        print("El comodín Ubicar Letras ya fue usado.")


# def usar_comodines(diccionario: dict, numero: str, bandera_uno: bool, bandera_dos: bool):

#     if diccionario["comodines"] == False:
#         if numero == "1":
#             if bandera_uno == False:
#                 bandera_uno = True

#         if numero == "2":
#             if bandera_dos == False:
#                 bandera_dos = True

#         if bandera_uno == True and bandera_dos == True:
#             diccionario["comodines"] = True


def usar_comodines(estado_comodines: dict, ingreso: str):


    if ingreso == "1" and not estado_comodines["revelar"]:
        estado_comodines["revelar"] = True

    elif ingreso == "2" and not estado_comodines["ubicar"]:
        estado_comodines["ubicar"] = True

    else:
        print("Ese comodín ya fue usado.")
    

# lista_combinada = combinar_listas(lista_ubicar, lista_revelar, lista_palabras)

# return lista_combinada
