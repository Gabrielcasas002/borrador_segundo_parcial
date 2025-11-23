from diccionario_juego import *
from especificas import *
import re


# pasar el diccionario a un modulo csv

def elegir_letras(diccionario: dict) -> list:

    indice = random.randint(0, len(diccionario) - 1)
    lista_letras = diccionario[indice]["letras"]

    return lista_letras


def elegir_palabras(diccionario: dict, letras: list) -> list:

    for i in range(len(diccionario)):

        if diccionario[i]["letras"] == letras:

            lista_palabras = diccionario[i]["palabras"]

    return lista_palabras


def recorrer_lista_letras(lista: list):
    
    cadena = ""

    for i in range(len(lista)):
        cadena += lista[i]

    return cadena


def recorrer_lista_palabras(lista: list):

    cadena = ""

    for i in range(len(lista)):
        cadena += lista[i]
        if i < len(lista) - 1:
            cadena += "-"

    return cadena

# FUNCIONA

def crear_csv(diccionario: dict):


    with open("diccionario_juego.csv", "w") as archivo:

        for i in range (0, 5):
            nivel = i + 1

            for j in range(3):

                lista_letras = elegir_letras(diccionario)
                lista_palabras = elegir_palabras(diccionario, lista_letras)

                recorrer_palabras = recorrer_lista_palabras(lista_palabras)
                recorrer_letras = recorrer_lista_letras(lista_letras)

                limpiar_lista(diccionario, lista_letras, lista_palabras)

                linea = f"{nivel}, {recorrer_letras}, {recorrer_palabras}\n"

                archivo.write(linea)

crear_csv(diccionario_prueba)


# leer csv


def crear_lista_csv(path: str) -> list:
    
    lista_diccionario_juego = []

    with open(path, "r", encoding = "utf8") as archivo:
        
        for linea in archivo:

            diccionario = {}
            registro = re.split(",|\n", linea)
            diccionario["nivel"] = int(registro[0])
            diccionario["letras"] = registro[1]
            diccionario["palabras"] = registro[2]

            lista_diccionario_juego.append(diccionario)

    return lista_diccionario_juego


#----------------FUNCION-NUEVA------------------------------#

# Hacer que guarde una bandera para los comodines de cada nivel.

def reconstruir_diccionario(path: str) -> list:

    lista_final = []
    for i in range(5):
        lista_final.append({"nivel": i + 1, "partidas": []}) # Agregar una bandera para los comodines.

    with open(path, "r", encoding="utf8") as archivo:

        for linea in archivo:

            registro = re.split(",|\n", linea)
            nivel = int(registro[0])
            letras_str = registro[1]
            letras = armar_letras(letras_str)

            palabras_str = registro[2]
            palabras = armar_palabras(palabras_str)

            partida = {
                "letras": letras,
                "palabras": palabras
            }

            lista_final[nivel - 1]["partidas"].append(partida)

    return lista_final


def armar_letras(cadena_letras: str) -> list:
    
    lista_letras = []

    for i in range(len(cadena_letras)):
        if cadena_letras[i] != " ":
            lista_letras.append(cadena_letras[i])

    return lista_letras


def armar_palabras(cadena_palabras: str) -> list:

    lista_palabras = []

    palabra_actual = ""

    for i in range(len(cadena_palabras)):

        if cadena_palabras[i] != "-":
            palabra_actual += cadena_palabras[i]
        else:
            lista_palabras.append(palabra_actual)
            palabra_actual = ""

    if palabra_actual != "":
        lista_palabras.append(palabra_actual)

    return lista_palabras

lista = reconstruir_diccionario("diccionario_juego.csv")
print(lista)



# MODIFICAR LA FUNCION obtener_colaboradores() para reemplazar la linea 128: registro = re.split(",|\n", linea) para no usar (re.split)

def obtener_colaboradores(titulo: str) -> list:
    """_summary_

    Args:
        titulo (str): String recibido por parametro que contiene el nombre de una cancion junto a sus colaboradores.

    Returns:
        list: La funcion retorna una lista que contiene los nombres de los colaboradores.
    """
    lista = []
    colaboradores = ""
    for i in range(len(titulo)):
        if titulo[i] == "-":
            colaboradores = rebanar(titulo, 0, i - 1)
            break 
    
    colaborador = ""

    for i in range(len(colaboradores)):
        if colaboradores[i] == "|":
            espacio = " "
            lista.append(espacio)
        if colaboradores[i] != "|":
            colaborador += colaboradores[i]

    lista.append(colaborador)

    return lista

# Para la funcion reconstruir_diccionario(), modular la funcion y intentar usar la funcion rebanar() para borrar los guiones "-". 