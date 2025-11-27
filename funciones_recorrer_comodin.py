def verificar_cadena(cadena):
    bandera = True

    if cadena == "XXX":
        print("El Jugador gano la partida")
        bandera = False

    elif cadena == "OOO":
        print("La Maquina gano la partida")
        bandera = False

    return bandera

def verificar_diagonal(grilla: list):
    bandera = True

    cadena = ""
    for i in range(len(grilla)):
        if grilla[i][i] == "X":
            cadena += grilla[i][i]
        
        elif grilla[i][i] == "O":
            cadena += grilla[i][i]
    

    bandera = verificar_cadena(cadena)
    
    return bandera

def verificar_diagonal_inversa(matriz: list):
    cadena = ""
    for i in range(len(matriz)):
        if matriz[i][2-i] == "X":
            cadena += "X"
        
        elif matriz[i][2-i] == "O":
            cadena += "O"
        
    bandera = verificar_cadena(cadena)

    return bandera


def recorrer_filas(matriz: list, fila: int):
    
    cadena = ""
    for i in range(len(matriz[0])):

        if matriz[fila][i] == "X":
            cadena += matriz[fila][i]
            
        elif matriz[fila][i] == "O":
            cadena += matriz[fila][i]

    return cadena


def recorrer_columnas(matriz: list, columna: int):

    cadena = ""
    for i in range(len(matriz)):

        if matriz[i][columna] == "X":
            cadena += matriz[i][columna]

        elif matriz[i][columna] == "O":
            cadena += matriz[i][columna]
    
    return cadena




def verificar_filas(grilla: list):
    for i in range(len(grilla) - 1):
        cadena_filas = recorrer_filas(grilla, i)

        bandera = verificar_cadena(cadena_filas)
        if bandera == False:
            break

    return bandera


def verificar_columnas(grilla: list):
    
    for i in range(len(grilla[0])):
        cadena_columna = recorrer_columnas(grilla, i)

        bandera = verificar_cadena(cadena_columna)
        if bandera == False:
            break

    return bandera
