from diccionario_juego import *
import re
import random

def mostrar_lista(list: list):
    """_summary_

    Args:
        list (list): Recibe una lista como parametro para mostrarla
    """

    for i in range(len(list)):
        print(f"{list[i]}\n")


def elegir_letras_csv(diccionario: dict) -> list:
    """_summary_

    Args:
        diccionario (dict): Recibe el diccionario_juego como paramatetro, para luego seleccionar una lista de letras aleatoriamente

    Returns:
        list: Lista de letras aleatoria del diccionario
    """

    indice = random.randint(0, len(diccionario) - 1)
    lista_letras = diccionario[indice]["letras"]

    return lista_letras


def elegir_palabras_csv(diccionario: dict, letras: list) -> list:
    """_summary_

    Args:
        diccionario (dict): Recibe el diccionario_juego como parametro
        letras (list): Recibe la lista de letras seleccionada anteriormente, para elegir la lista de palabras asociadas a la lista de letras
    Returns:
        list: Devuelve la lista de palabras seleccionadas
    """


    for i in range(len(diccionario)):

        if diccionario[i]["letras"] == letras:

            lista_palabras = diccionario[i]["palabras"]

    return lista_palabras


def limpiar_lista_csv(diccionario: list, lista_letras: list, lista_palabras: list):
    """_summary_

    Elimina del diccionario la sección que coincide exactamente con las letras y palabras dadas.

    Args:
        diccionario (list): Recibe el diccionario_juego
        lista_letras (list): Recibe la lista de letras seleccionada anteriormente
        lista_palabras (list): Recibe la lista de palabras dada anteriormente
    """

    for i in range(len(diccionario)):
        seccion = diccionario[i]
        if seccion["letras"] == lista_letras and seccion["palabras"] == lista_palabras:
            diccionario.remove(seccion)
            break


def recorrer_lista_letras(lista: list):
    """_summary_

    Convierte una lista de letras en un string sin separadores.

    Args:
        lista (list): Lista a recorrer

    Returns:
        _type_: Devuelve la lista letras como una cadena
    """

    cadena = ""

    for i in range(len(lista)):
        cadena += lista[i]

    return cadena


def recorrer_lista_palabras(lista: list):
    """_summary_

    Convierte una lista de palabras en un string separado por guiones.

    Args:
        lista (list): Lista de palabras

    Returns:
        _type_: Devuelve una cadena separando cada palabra con guiones
    """

    cadena = ""

    for i in range(len(lista)):
        cadena += lista[i]
        if i < len(lista) - 1:     
            cadena += "-"

    return cadena



def mostrar_diccionario(diccionario: dict):
    """_summary_

    Recibe un diccionario como parametro para mostrar sus claves, y el valor de las claves

    Args:
        diccionario (dict): Recibe un diccionario
    """

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
    """_summary_

    Crea un archivo CSV con niveles y partidas generadas aleatoriamente.
    Cada nivel genera 3 partidas con letras y palabras asociadas.

    Args:
        diccionario (dict): Diccionario base con letras y palabras 
    """

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
    """_summary_

    Convierte un string de palabras unidas por guiones en una lista de palabras.

    Args:
        palabra_actual (str): Variable auxiliar para construir cada palabra
        palabras_str (str): Cadena formada anteriormente separada en guiones

    Returns:
        list: Lista de palabras separadas.
    """

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


def elegir_nivel(diccionario_niveles: list, numero: int) -> dict:
    """_summary_

    Devuelve el diccionario correspondiente al nivel solicitado.

    Args:
        diccionario_niveles (list): Lista de niveles cargados.
        numero (int): Nivel a seleccionar.

    Returns:
        dict: Retorna el Nivel encontrado
    """

    for i in range(len(diccionario_niveles)):
        if diccionario_niveles[i]["nivel"] == numero:
            return diccionario_niveles[i]


def elegir_letras_nivel(nivel: list) -> list:
    """_summary_

    Selecciona aleatoriamente las letras de una partida dentro de un nivel.

    Args:
        nivel (dict): Diccionario que contiene partidas del nivel.

    Returns:
        list: Devuelve la lista de letras seleccionada.
    """

    indice = random.randint(0, len(nivel["partidas"]) - 1)
    lista_letras = nivel["partidas"][indice]["letras"]

    return lista_letras


def elegir_palabras_nivel(nivel: list, letras: list) -> list:
    """_summary_

    Devuelve la lista de palabras correspondiente a un conjunto de letras dentro de un nivel.

    Args:
        nivel (dict): Diccionario que contiene partidas del nivel.
        letras (list): Lista de letras de la partida seleccionada

    Returns:
        list: Lista de palabras asociada a las letras.
    """

    palabras = []
    partidas = nivel["partidas"]

    for i in range(len(partidas)):
        if partidas[i]["letras"] == letras:
            palabras = partidas[i]["palabras"]
    
    return palabras




