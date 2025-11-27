from diccionario_juego import *
from funciones_csv import *
from especificas import *
import re

def validar_crear_csv(bandera: bool):

    if bandera == False:
        print("El CSV fue creado con exito !!!")
    else:
        print("No se pudo crear el CSV.")


def validar_reconstruir_diccionario(bandera: bool):

    if bandera == False:
        print("Diccionario reconstruido para el juego con exito !!!")
    else:
        print("No se puedo reconstruir el diccionario para el juego.")


def crear_csv(diccionario: dict):

    diccionario_copia = copiar_lista(diccionario)
    hubo_error = False

    try:
        with open("diccionario_juego.csv", "w", encoding="utf8") as archivo:

            for i in range(5):
                nivel = i + 1

                for j in range(3):
                    try:
                        lista_letras = elegir_letras_csv(diccionario_copia)
                        lista_palabras = elegir_palabras_csv(diccionario_copia, lista_letras)

                        datos_validos = True

                        if not lista_letras:
                            datos_validos = False

                        if not lista_palabras:
                            datos_validos = False

                        if datos_validos:

                            recorrer_palabras = recorrer_lista_palabras(lista_palabras)
                            recorrer_letras = recorrer_lista_letras(lista_letras)

                            eliminar_lista_csv(diccionario_copia, lista_letras, lista_palabras)

                            linea = f"{nivel},{recorrer_letras},{recorrer_palabras}\n"
                            archivo.write(linea)

                        else:
                            hubo_error = True

                    except:
                        hubo_error = True

    except:
        hubo_error = True

    validar_crear_csv(hubo_error)



def reconstruir_diccionario(path: str) -> list:
    """
    Reconstruye un diccionario de niveles y partidas desde un archivo CSV.
    """

    lista_final = []
    lista_banderas = [False, False, False]
    hubo_error = False

    for i in range(5):
        lista_final.append({
            "nivel": i + 1,
            "estado_comodines": lista_banderas,
            "partidas": []
        })

    try:
        with open(path, "r", encoding="utf8") as archivo:

            for linea in archivo:

                try:
                    registro = re.split(",|\n", linea)

                    linea_valida = True

                    if len(registro) < 3:
                        linea_valida = False

                    if linea_valida:
                        try:
                            nivel = int(registro[0])
                        except:
                            linea_valida = False

                    if linea_valida:
                        if nivel < 1 or nivel > 5:
                            linea_valida = False

                    if linea_valida:

                        letras_str = registro[1]
                        letras = []
                        for i in range (len(letras_str)):
                            caracter = letras_str[i]
                            if caracter != " ":
                                letras.append(caracter)

                        palabras_str = registro[2]
                        palabras = armar_palabras("", palabras_str)

                        partida = {
                                "letras": letras,
                                "palabras": palabras
                            }

                        lista_final[nivel - 1]["partidas"].append(partida)

                    else:
                        hubo_error = True

                except:
                    hubo_error = True

    except:
        hubo_error = True

    validar_reconstruir_diccionario(hubo_error)

    return lista_final
