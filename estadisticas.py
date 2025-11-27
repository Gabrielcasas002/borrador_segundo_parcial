from archivos_json import actualizar_usuario_estadisticas

def limpiar_estadisticas(estadisticas):
    estadisticas["Puntuacion Total"] = 0
    estadisticas["Ingresos incorrectos"] = 0
    estadisticas["Tiempo restante total en segundos"] = 0
    estadisticas["Tiempo entre niveles"] = 0
    estadisticas["Tiempo promedio entre niveles"] = 0


def cargar_estadisticas(usuario: dict):
    estadisticas = {
        "Puntuacion Total": usuario["Puntuacion Total"],
        "Ingresos incorrectos": usuario["Ingresos incorrectos"],
        "Tiempo restante total en segundos": usuario["Tiempo restante total en segundos"],
        "Tiempo entre niveles": usuario["Tiempo entre niveles"],
        "Tiempo promedio entre niveles": usuario["Tiempo promedio entre niveles"]
            }
    
    return estadisticas

def actualizar_estadisticas(usuario: dict, estadisticas: dict):

    usuario["Puntuacion Total"] = estadisticas["Puntuacion Total"]
    usuario["Ingresos incorrectos"] = estadisticas["Ingresos incorrectos"]
    usuario["Tiempo restante total en segundos"] = estadisticas["Tiempo restante total en segundos"]
    usuario["Tiempo entre niveles"] = estadisticas["Tiempo entre niveles"]
    usuario["Tiempo promedio entre niveles"] = estadisticas["Tiempo promedio entre niveles"]

    actualizar_usuario_estadisticas(usuario)