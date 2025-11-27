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
    datos = []  

    try:
        with open("usuariosprueba.json", "r") as archivo:
            datos = json.load(archivo)
    except:
        with open("usuariosprueba.json", "w") as archivo:
            archivo.write("[]")
        datos = [] 

    return datos

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
        print("Ese usuario ya existe. Elija otro.")
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
        print("Usuario registrado con éxito.")
        resultado = True

    return resultado   


def login():
    resultado = None
    usuarios = leer_json()

    print("INICIAR SESION:\n")

    nombre = input("Usuario: ")
    contrasena = input("Contraseña: ")

    encontrado = None
    for i in range(len(usuarios)):
        if usuarios[i]["Usuario"] == nombre and usuarios[i]["Contrasena"] == contrasena:
            encontrado = usuarios[i]

    if encontrado != None:
        print("Inicio de sesión exitoso.\n")
        resultado = encontrado
    else:
        print("Usuario o contraseña incorrectos.\n")

    return resultado  

def actualizar_usuario_estadisticas(usuario_modificado: dict):
    usuarios = leer_json()
    indice = -1 
    resultado = None

    for i in range(len(usuarios)):
        if usuarios[i]["Usuario"] == usuario_modificado["Usuario"]:
            indice = i

    if indice != -1:
        usuarios[indice] = usuario_modificado
        guardar_json(usuarios)
        resultado = True
    else:
        print("No se pudo actualizar el usuario porque no existe.")

    return resultado

