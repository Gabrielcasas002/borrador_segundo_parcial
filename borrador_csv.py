from diccionario_juego import *
import re
import random


def elegir_letras_csv(diccionario: dict) -> list:

    indice = random.randint(0, len(diccionario) - 1)
    lista_letras = diccionario[indice]["letras"]

    return lista_letras


def elegir_palabras_csv(diccionario: dict, letras: list) -> list:

    for i in range(len(diccionario)):

        if diccionario[i]["letras"] == letras:

            lista_palabras = diccionario[i]["palabras"]

    return lista_palabras


def limpiar_lista_csv(diccionario: list, lista_letras: list, lista_palabras: list):

    for i in range(len(diccionario)):
        seccion = diccionario[i]
        if seccion["letras"] == lista_letras and seccion["palabras"] == lista_palabras:
            diccionario.remove(seccion)
            break


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



def mostrar_diccionario(diccionario: dict):

    for clave in diccionario.keys():
       print(f"{clave} : {diccionario[clave]}")


def rebanar(cadena: str, inicio: int, finalizacion: int) -> str:
    """_summary_

    Args:
        cadena (str): String recibido por parametro.
        inicio (int): Entero que recibido por parametro que marca el inicio.
        finalizacion (int): Entero recibido por parametro que marca la finalizacion

    Returns:
        str: La funcion retorna un nuevo string, recortando el anterior desde el inicio hasta la finalizacion. 
    """
    cadena_auxiliar = ""
    for caracter in range(inicio, finalizacion):
        cadena_auxiliar += cadena[caracter]

    return cadena_auxiliar

def crear_csv(diccionario: dict):
    
    diccionario_aux = []
    for i in range(len(diccionario)):
        diccionario_aux.append(diccionario[i])


    with open("diccionario_juego.csv", "w") as archivo:

        for i in range (0, 5):
            nivel = i + 1

            for j in range(3):

                lista_letras = elegir_letras_csv(diccionario)
                lista_palabras = elegir_palabras_csv(diccionario, lista_letras)

                recorrer_palabras = recorrer_lista_palabras(lista_palabras)
                recorrer_letras = recorrer_lista_letras(lista_letras)

                limpiar_lista_csv(diccionario, lista_letras, lista_palabras)

                linea = f"{nivel},{recorrer_letras},{recorrer_palabras}\n"

                archivo.write(linea)




def armar_palabras(palabra_actual: str, palabras_str: str):

    palabras_lista = []

    for i in range(len(palabras_str)):
                if palabras_str[i] != "-":
                    palabra_actual += palabras_str[i]
                else:
                    palabras_lista.append(palabra_actual)
                    palabra_actual = ""

    if palabra_actual != "":
        palabras_lista.append(palabra_actual)

    return palabras_lista

def reconstruir_diccionario(path: str) -> list:

    lista_final = []
    lista_banderas = [False, False, False]


    for i in range(5):
        lista_final.append({"nivel": i + 1,"estado comodines": lista_banderas, "partidas": []})
        

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

def elegir_letras_nivel(nivel: list) -> list:
    """_summary_

    Args:
        nivel (dict): _description_

    Returns:
        list: _description_
    """

    indice = random.randint(0, len(nivel["partidas"]) - 1)
    lista_letras = nivel["partidas"][indice]["letras"]

    return lista_letras


def elegir_palabras_nivel(nivel: list, letras: list) -> list:
    """_summary_

    Args:
        nivel (dict): _description_
        letras (list): _description_

    Returns:
        list: _description_
    """

    palabras = []
    partidas = nivel["partidas"]

    for i in range(len(partidas)):
        if partidas[i]["letras"] == letras:
            palabras = partidas[i]["palabras"]
    
    return palabras


def mostrar_lista(list: list):
    for i in range(len(list)):
        print(f"{list[i]}\n")


def elegir_nivel(diccionario_niveles: list, numero: int) -> dict:

    for i in range(len(diccionario_niveles)):
        if diccionario_niveles[i]["nivel"] == numero:
            return diccionario_niveles[i]



# crear_csv(diccionario_juego)
# listfinal = reconstruir_diccionario("diccionario_juego.csv")
# mostrar_lista(listfinal)
# nivell_actual = elegir_nivel(listfinal, 1)
# lista_letras = elegir_letras_nivel(nivell_actual)
# lista_palabras = elegir_palabras_nivel(nivell_actual, lista_letras)


