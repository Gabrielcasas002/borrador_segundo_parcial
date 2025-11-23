from sprint_1 import *
import os

def main():


    bandera = True

    while bandera:
        opcion = input("1. \n2. \n3. Salir del programa\nElija una opcion: ")
        match opcion :
            case "1":
                jugando_descifrar_palabra()
            case "2":
                pass
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