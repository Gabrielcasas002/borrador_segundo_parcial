from Funciones_generales_comodin import *
from funciones_recorrer_comodin import * 
import os

grilla = crear_matriz(3, 3, "_")

def jugar_tateti(grilla: list):
    contador = 0
    bandera = True
    maquina = True
    Ganador = 0

    while bandera == True:
        os.system("cls")
        mostrar_matriz(grilla)

        if estado_partida(grilla) == False:
            Ganador = 2
            bandera = False
            break
        
        fila = get_int("En que fila queres ingresar: ", "Error, esa fila no existe", 0, 2, 3)
        columna = get_int("En que columna queres ingresar: ", "Error, esa columna no existe", 0, 2, 3)

        while grilla[fila][columna] != "_" and contador < 3:
            fila = get_int("Vuelva a ingresar otra fila: ", "Error, esa fila no existe", 0, 2, 3)
            columna = get_int("Vuelva a ingresar otra columna: ", "Error, esa columna no existe", 0, 2, 3)
            contador += 1
            
            if contador < 3 :
                print(f"Tienes {3 - contador} reintentos")
            else:
                print("Te quedaste sin reintentos 💀")

            os.system("pause")
            os.system("cls")
        
        if contador == 3:
            os.system("cls")
            print("Error... vuelva a intentarlo mas tarde")
            bandera = False
            break

        if grilla[fila][columna] == "_":
            grilla[fila][columna] = "X"


        os.system("pause")
        os.system("cls")

        if tablero_lleno(grilla) == True:
            print("\nEmpate, no hay más espacios.")
            mostrar_matriz(grilla)
            bandera = False
            break

        
        if estado_partida(grilla) == False:
            mostrar_matriz(grilla)
            Ganador = 1
            break

        while maquina:
            maquina = ingresar_maquina(grilla)
        maquina = True
    
    return Ganador
        
#jugar_tateti(grilla)