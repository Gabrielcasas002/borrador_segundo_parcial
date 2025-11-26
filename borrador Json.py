import json

def crear_archivo_json():
    try:
        with open("usuariosprueba.json", "r") as archivo:
            contenido = archivo.read()

        if contenido == "":
            with open("usuariosprueba.json", "w") as archivo:
                archivo.write("[]")

    except:
        with open("usuariosprueba.json", "w") as archivo:
            archivo.write("[]")


def leer_json():
    try:
        with open("usuariosprueba.json", "r") as archivo:
            return json.load(archivo)
    except:
        with open("usuariosprueba.json", "w") as archivo:
            archivo.write("[]")
        return []


def guardar_json(lista):
    try:
        with open("usuariosprueba.json", "w") as archivo:
            json.dump(lista, archivo, indent=4)
    except:
        print("Error al guardar el archivo JSON.")


def registrar_usuario():
    resultado = None
    usuarios = leer_json()

    print("\n--- REGISTRAR NUEVO USUARIO ---")

    nombre = input("Ingrese un nombre de usuario: ")

    existe = False
    for i in range(len(usuarios)):
        if usuarios[i]["Usuario"] == nombre:
            existe = True

    if existe:
        print("❌ Ese usuario ya existe. Elija otro.")
    else:
        contrasena = input("Ingrese una contraseña: ")
        nuevo_usuario = {
            "Usuario": nombre,
            "Contrasena": contrasena,
            "Puntuacion Total" : 0,
            "Ingresos incorrectos" : 0,
            "Tiempo restante total en segundos" : 0,
            "Tiempo entre niveles" : 0,
            "Tiempo promedio entre niveles" : 0
        }

        usuarios.append(nuevo_usuario)
        guardar_json(usuarios)
        print("✔ Usuario registrado con éxito.")
        resultado = True

    return resultado     # único return



def login():
    resultado = None
    usuarios = leer_json()

    print("\n--- INICIAR SESIÓN ---")

    nombre = input("Usuario: ")
    contrasena = input("Contraseña: ")

    encontrado = None
    for i in range(len(usuarios)):
        if usuarios[i]["Usuario"] == nombre and usuarios[i]["Contrasena"] == contrasena:
            encontrado = usuarios[i]

    if encontrado != None:
        print("✔ Inicio de sesión exitoso.")
        resultado = encontrado
    else:
        print("❌ Usuario o contraseña incorrectos.")

    return resultado  



def menu_inicio():
    crear_archivo_json()
    usuario_logueado = None
    salir = False

    while not salir:
        print("\n1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            usuario = login()
            if usuario != None:
                usuario_logueado = usuario
                salir = True

        elif opcion == "2":
            registrar_usuario()

        elif opcion == "3":
            print("Saliendo...")
            salir = True

        else:
            print("Opción inválida.")

    return usuario_logueado  


jugador = menu_inicio()

if jugador != None:

    print("Bienvenido", jugador["Usuario"])


