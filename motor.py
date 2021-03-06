import RPi.GPIO as GPIO
import time
from os import system, name

##################################################################################
# Ejemplo de control completo para motor paso a paso 28BYJ-48 con driver ULN2003 #
##################################################################################

# DIR: 10.2.41.38
# SSH: pi@10.2.41.38
 
def limpiar_pantalla ():
    _ = system ('clear')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

coil_A_pin = 4    # PIN 7     (ULN2003 IN 1)
coil_B_pin = 17   # PIN 11    (ULN2003 IN 2)
coil_C_pin = 27   # PIN 13    (ULN2003 IN 3)
coil_D_pin = 22   # PIN 15    (ULN2003 IN 4)

total_pasos = 2038

# SELECCION DE MODO
modo = 1    # 0 - Wave Drive: Un estator a la vez.
            #                 2048 pasos / revolución.
            #                 Suave, poco torque.
            # 1 - Full Drive: Dos estatores a la vez.
            #                 2048 pasos / revolución.
            #                 Máximo torque.
            # 2 - Half Drive: Uno o dos estatores alternativamente.
            #                 4096 pasos / revolución.
            #                 Torque medio. Mayor resolucion angular (doble)

if modo == 0:
    pasos = 4
    sec = list(range(0, pasos))
    sec[0] = [1,0,0,0]
    sec[1] = [0,1,0,0]
    sec[2] = [0,0,1,0]
    sec[3] = [0,0,0,1]
elif modo == 1:
    pasos = 4
    sec = list(range(0, pasos))
    sec[0] = [1,1,0,0]
    sec[1] = [0,1,1,0]
    sec[2] = [0,0,1,1]
    sec[3] = [1,0,0,1]
elif modo == 2:
    pasos = 8
    sec = list(range(0, pasos))
    sec[0] = [1,0,0,0]
    sec[1] = [1,1,0,0]
    sec[2] = [0,1,0,0]
    sec[3] = [0,1,1,0]
    sec[4] = [0,0,1,0]
    sec[5] = [0,0,1,1]
    sec[6] = [0,0,0,1]
    sec[7] = [1,0,0,1]

GPIO.setup(coil_A_pin, GPIO.OUT)
GPIO.setup(coil_B_pin, GPIO.OUT)
GPIO.setup(coil_C_pin, GPIO.OUT)
GPIO.setup(coil_D_pin, GPIO.OUT)

 
def setPaso(w1, w2, w3, w4):
    GPIO.output(coil_A_pin, w1)
    GPIO.output(coil_B_pin, w2)
    GPIO.output(coil_C_pin, w3)
    GPIO.output(coil_D_pin, w4)
 
def adelante(delay, cant_pasos):
    j = 0
    for i in range(cant_pasos):
        setPaso(sec[j][0], sec[j][1], sec[j][2], sec[j][3])
        j = j + 1
        if j >= pasos:
            j = 0
        time.sleep(delay)
 
def reversa(delay, cant_pasos):
    j = pasos
    for i in range(cant_pasos):
        j = j - 1
        setPaso(sec[j][0], sec[j][1], sec[j][2], sec[j][3])
        if j == 0:
            j = pasos
        time.sleep(delay)
 
def desenergizar_bobinas ():
    setPaso(0,0,0,0)

if __name__ == '__main__':
    
    limpiar_pantalla()
    while True:
        limpiar_pantalla()
        delay = input("Delay (ms)?: ")
        #print(" ")
        #direccion = input ("Direccion? [1:adelante / 2:reversa]: ")
        print(" ")
        opcion = input("Modo? [1:pasos / 2:angulo]: ")
        print(" ")
        while True:
            if opcion == "1":
                cant_pasos = input("Pasos?: ")
                if (abs(int(cant_pasos)) == int(cant_pasos)):
                    reversa(int(delay) / 1000.0, int(cant_pasos))
                else:
                    adelante(int(delay) / 1000.0, abs(int(cant_pasos)))
            elif opcion == "2":
                angulo = input("Angulo? (+/-): ")
                cant_pasos = int((total_pasos / 360) * abs(int(angulo)))
                if (abs(int(angulo)) == int(angulo)):
                    reversa(int(delay) / 1000.0, int(cant_pasos))
                else:
                    adelante(int(delay) / 1000.0, abs(int(cant_pasos)))
            desenergizar_bobinas()
