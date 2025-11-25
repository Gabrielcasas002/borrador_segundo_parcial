from diccionario_juego import *
from juego_muestra import *
import os

def main():


    bandera = True

    while bandera:
        opcion = input("1. Jugar Decifrar Palabra\n2. Ver Estadisticas\n3. Salir del programa\nElija una opcion: ")
        match opcion :
            case "1":
                resultado = jugar_juego(diccionario_prueba, diccionario_estadisticas)
                if resultado:
                    print("\n¡ Felicitaciones, Ganaste El Juego !")
                    print(f"\nEstadisticas Finales:\n")
                    mostrar_diccionario(diccionario_estadisticas)
                else:
                    print("\n💀 Juego terminado. Mejor suerte la próxima.")
                    print(f"\nEstadisticas Finales:\n")
                    mostrar_diccionario(diccionario_estadisticas)
                    
            case "2":
                os.system("cls")
                print("Estadisticas:\n")
                mostrar_diccionario(diccionario_estadisticas)
            case "3":
                print("Saliendo")
                bandera = False
            case _:
                if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and  opcion != "6" and opcion != "7" and opcion != "8":
                    print("ERROR...Elija una opcion valida")
        os.system("pause")
        os.system("cls")


if __name__ == "__main__":
    main()