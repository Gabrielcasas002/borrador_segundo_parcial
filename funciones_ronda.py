import time

def jugar_descifrar_palabras(ingresar: str, palabras: list, lista_palabras_ingresadas: list) -> bool:
    """_summary_

    Args:
        ingresar (str): String recibido por parametro que representa un dato ingresado por el usuario.
        palabras (list): Lista de palabras recibida por parametro.
        lista_palabras_ingresadas (list): Lista de palabras ingresadas por el usuario recibida por paremtero

    Returns:
        bool: La funcion verifica si el string (ingresar) se encunetra en la lista de palabras, si la encuentra, la agrega a la lista de palabras ingresadas y la elimina de la lista de palabras.
              Ademas, la funcion retorna una bandera que cambia su estado a True si la palabra ingresada por el usuario fue encontrada.
    """

    bandera  = False

    for respuesta in range(len(palabras)):
        if palabras[respuesta] == ingresar:
           lista_palabras_ingresadas.append(ingresar)
           palabras.remove(palabras[respuesta])
           bandera = True
           break

    return bandera


def sumar_estadisticas(estadisticas: dict, puntuacion_ronda: int, cantidad_de_ingresos_incorrectos: int, tiempo_restante: int, contador: int, tiempo_ronda: float):
    """_summary_

    Args:
        estadisticas (dict): Diccionario recibido por parametro que representa las estadisticas del juego.
        puntuacion_ronda (int): Entero recibido por parametro que representa la puntuacion obtenida en la ronda.
        cantidad_de_ingresos_incorrectos (int): Entero recibido por parametro que representa la cantidad de ingresos incorrectos obtenidos en la ronda.
        tiempo_restante (int): Entero recibido por parametro que representa el tiempo restante en la ronda. 
        contador (int): Entero obtenido por parametro que representa al contador de la partida.
        tiempo_ronda (float): Flotante obtenido por parametro que representa el tiempo obtenido en la ronda.
    """
    contador += 1
    tiempo_entre_niveles = 0
    tiempo_entre_niveles += int(tiempo_ronda)

    estadisticas["Puntuacion Total"] += puntuacion_ronda
    estadisticas["Ingresos incorrectos"] += cantidad_de_ingresos_incorrectos
    estadisticas["Tiempo restante total en segundos"] += tiempo_restante
    estadisticas["Tiempo entre niveles"] += tiempo_entre_niveles
    
    promedio_entre_niveles = estadisticas["Tiempo entre niveles"]
    
    estadisticas["Tiempo promedio entre niveles"] = promedio_entre_niveles / contador


def finalizar_partida(puntaje: int, incorrectas: int, tiempo_restante: int, estadisticas: dict, contador: int, tiempo_inicio: float):
    """_summary_

    Args:
        puntaje (int): Entero recibido por parametro que representa el puntaje obtenido en el juego.
        incorrectas (int): Entero recibido por parametro que representa la cantidad de ingresos incorrectos obtenidos en el juego.
        tiempo_restante (int): Entero recibido por parametro que representa el tiempo restante obtenido en el juego.
        estadisticas (dict): Diccionario recibido por parametro que contiene las estadisticas obtenidas en el juego y donde se guardarán todos los datos.
        contador (int): Entero recibido por parametro que representa el contador utilizado obtenido en el juego.
        tiempo_inicio (float): Flotante recibido por parametro que representa el tiempo de inicio del juego.
    """

    tiempo_total_ronda = time.time() - tiempo_inicio

    print("Ganaste La Partida !!!")
    print(f"Puntuación: {puntaje}")
    print(f"Tiempo restante: {tiempo_restante}")

    sumar_estadisticas(estadisticas, puntaje, incorrectas, tiempo_restante, contador, tiempo_total_ronda)


def procesar_ingreso(ingreso: str, lista_palabras: list, lista_ingresadas: list) -> int:
    """_summary_

    Args:
        ingreso (str): String recibido por parametro que representa a un dato ingresado por el usuario.
        lista_palabras (list): Lista de palabras recibida por parametro.
        lista_ingresadas (list): lista de palabras ingresadas por el usuario recibida por parametro.

    Returns:
        int: La funcion utiliza los datos obtenidos para generar una bandera. Si la bandera es True, la funcion calcula los puntos, lo muestra y lo retorna. 
    """

    print("")
    acierto = jugar_descifrar_palabras(ingreso, lista_palabras, lista_ingresadas)
    puntos = 0

    if acierto:
        puntos = len(ingreso) * 20
        print(f"Ganaste {puntos} puntos")        
    else:
        print("Palabra incorrecta.")

    return puntos


def calcular_tiempo(tiempo_inicio: float, tiempo_limite: int) -> float:
    """_summary_

    Args:
        tiempo_inicio (float): Flotante recibido por parametro que representa al tiempo de inicio de la partida.
        tiempo_limite (int): Entero recibido por parametro que representa al tiempo limite de la partida.

    Returns:
        float: La funcion retorna un flotante que representa al tiempo restante de la partida.
    """

    transcurrido = time.time() - tiempo_inicio
    tiempo_restante = tiempo_limite - transcurrido

    return tiempo_restante


def verificar_ingreso(ingreso: str, palabras_disponibles: list, palabras_ingresadas: list) -> int:
    """_summary_

    Args:
        ingreso (str): String recibido por parametro que representa a un dato ingresado por el usuario.
        palabras_disponibles (list): Lista de palabras obtenida por parametro.
        palabras_ingresadas (list): Lista de palabras ingresadas por el usuario recibida por parametro.

    Returns:
        int: La funcion utiliza los datos recibidos, transforma el string en mayusculas y luego verifica el string para ver si se encuentra en la lista de palabras.
             Finalmente, retorna los puntos obtenidos si los hay.
    """

    ingreso_mayuscula = transformar_a_mayusculas(ingreso)
    puntos = procesar_ingreso(ingreso_mayuscula,palabras_disponibles,palabras_ingresadas)

    return puntos


def transformar_a_mayusculas(cadena: str) -> str:
    """_summary_

    Args:
        cadena (str): String recibido por parametro que sera recorrido elemento por elemento.

    Returns:
        str: devuelve la cadena transformada a mayusculas. su funcion es hacer lo mismo que el comando .upper()
    """

    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    cadena_mayuscula = ""

    for i in range(len(cadena)):
        letra = cadena[i]

        for j in range(len(minusculas)):

            if letra == minusculas[j]:
                cadena_mayuscula += mayusculas[j]

            elif letra == mayusculas[j]:
                cadena_mayuscula += letra

    return cadena_mayuscula