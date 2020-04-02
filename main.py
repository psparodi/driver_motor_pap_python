from motor import *


if __name__ == '__main__':
    
    limpiar_pantalla()
    
    deteccion_de_cero()
    #otras_posiciones()
    posicion_1 = 0
    posicion_2 = 320
    posicion_3 = 620
    #explorar_posiciones()

    while True:
        limpiar_pantalla()
        delay = input("Delay (ms)?: ")
        print(" ")
        opcion = input("Modo? [1:pasos / 2:angulo]: ")
        print(" ")
        while True:
            if opcion == "1":
                cant_pasos = input("Pasos?: ")
                if (abs(int(cant_pasos)) == int(cant_pasos)):
                    adelante(int(delay) / 1000.0, int(cant_pasos))
                else:
                    reversa(int(delay) / 1000.0, abs(int(cant_pasos)))
            elif opcion == "2":
                angulo = input("Angulo? (+/-): ")
                cant_pasos = int((total_pasos / 360) * abs(int(angulo)))
                if (abs(int(angulo)) == int(angulo)):
                    adelante(int(delay) / 1000.0, int(cant_pasos))
                else:
                    reversa(int(delay) / 1000.0, abs(int(cant_pasos)))
            desenergizar_bobinas()
