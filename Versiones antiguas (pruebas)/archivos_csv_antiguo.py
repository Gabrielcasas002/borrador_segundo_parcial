from diccionario_juego import *
from funciones_csv import *
import re


def crear_csv(diccionario: dict):
    """_summary_

    Crea un archivo CSV con niveles y partidas generadas aleatoriamente.
    Cada nivel genera 3 partidas con letras y palabras asociadas.

    Args:
        diccionario (dict): Diccionario base con letras y palabras 
    """

    with open("diccionario_juego.csv", "w") as archivo:

        for i in range (0, 5):
            nivel = i + 1

            for j in range(3):

                lista_letras = elegir_letras_csv(diccionario)
                lista_palabras = elegir_palabras_csv(diccionario, lista_letras)

                recorrer_palabras = recorrer_lista_palabras(lista_palabras)
                recorrer_letras = recorrer_lista_letras(lista_letras)

                eliminar_lista_csv(diccionario, lista_letras, lista_palabras)

                linea = f"{nivel},{recorrer_letras},{recorrer_palabras}\n"

                archivo.write(linea)


def reconstruir_diccionario(path: str) -> list:
    """_summary_

    Reconstruye un diccionario de niveles y partidas a partir del archivo CSV generado previamente

    Args:
        path (str): Ruta del diccionario CSV.

    Returns:
        list: Lista de niveles, cada uno con sus partidas usada para jugar al juego.
    """

    lista_final = []
    lista_banderas = [False, False, False]


    for i in range(5):
        lista_final.append({"nivel": i + 1,"estado_comodines": lista_banderas, "partidas": []})
        

    with open(path, "r", encoding="utf8") as archivo:

        for linea in archivo:

            registro = re.split(",|\n", linea)
            nivel = int(registro[0])
            letras_str = registro[1]
            letras = []

            for i in range(len(letras_str)):
                if letras_str[i] != " ":
                    letras.append(letras_str[i])

            palabras_str = registro[2]
            palabra_actual = ""
            palabras = armar_palabras(palabra_actual, palabras_str)

            partida = {
                "letras": letras,
                "palabras": palabras
            }

            lista_final[nivel - 1]["partidas"].append(partida)

    return lista_final




