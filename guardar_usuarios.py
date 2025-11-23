import json
from diccionario_juego import *

def crear_archivo_json():
    archivo = open("usuariosprueba.json", "a")
    archivo.close()

    with open("usuariosprueba.json", "r") as archivo:
        contenido = archivo.read()

    if contenido == "":
        with open("usuariosprueba.json", "w") as archivo:
            archivo.write("[]")

def leer_json():
    with open("usuariosprueba.json", "r") as archivo:

        return json.load(archivo)

def guardar_json(lista):
    with open("usuariosprueba.json", "w") as archivo:
        json.dump(lista, archivo, indent = 4)

def agregar_usuario(estadisticas: dict):

    usuarios = leer_json()

    usuario = input("Ingrese el nombre del usuario: ")
    contrasena = input("Ingrese una contrasena: ")


    partida = {
        "Usuario" : usuario ,
        "Contrasena" : contrasena,
        "Puntuacion total" : estadisticas["Puntuacion Total"],
        "Ingresos incorrectos" : estadisticas["Ingresos incorrectos"],
        "Tiempo de partida" : estadisticas["Tiempo restante total en segundos"] 
    }

    usuarios.append(partida)
    guardar_json(usuarios)

# crear_archivo_json()
# agregar_usuario(diccionario_estadisticas)