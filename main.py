from juego_muestra import *
# from borrador_juego import *
# from funciones_juego import *
from diccionario_juego import *

def main(diccionario_juego, diccionario_estadisticas):
    
    resultado = jugar_juego(diccionario_juego, diccionario_estadisticas)

    if resultado:
        print("\n¡ Felicitaciones, Ganaste El Juego !")

    else:
        print("\n💀 Juego terminado. Mejor suerte la próxima.")


#---------------------------PRUEBAS---------------------------------#

main(diccionario_prueba, diccionario_estadisticas)

# Buscar posibles errores para poder completar el sprint 1