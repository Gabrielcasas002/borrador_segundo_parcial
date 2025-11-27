from funciones_recorrer_comodin import *
import random


def crear_matriz(filas: int, columnas: int, valor_inicial: any):
    matriz = []
    for _ in range(filas):
        una_fila = [valor_inicial] * columnas

        matriz += [una_fila]
    
    return matriz


def mostrar_matriz(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= " ")
        print()


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:

    numero_valido = int(input(mensaje)) - 1
 
    while numero_valido < minimo or numero_valido > maximo:
        
        if reintentos == 0:
            print("Error... vuelvalo a intentar mas tarde")
            return None
        else:
            print(f"Numero invalido, le quedan {reintentos} reintentos")
            numero_valido = int(input(mensaje_error))
            reintentos -= 1 
    
    
    return numero_valido


def tablero_lleno(grilla: list) -> bool:
    lleno = True

    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            if grilla[i][j] == "_":
                lleno = False

    return lleno


def ingresar_maquina(grilla: list):

    maquina = True

    while maquina:
            fila_aleatoria = random.randint(0,2)
            columna_aleatoria = random.randint(0,2)

            if grilla[fila_aleatoria][columna_aleatoria] == "_":
                grilla[fila_aleatoria][columna_aleatoria] = "O"
                maquina = False

    return maquina


def estado_partida(grilla: list) -> bool:
    seguir = True

    if seguir == True and verificar_filas(grilla) == False:
        seguir = False

    if seguir == True and verificar_columnas(grilla) == False:
        seguir = False

    if seguir == True and verificar_diagonal(grilla) == False:
        seguir = False

    if seguir == True and verificar_diagonal_inversa(grilla) == False:
        seguir = False

    return seguir
