#Ejemplo de ejercicio
#1 Hacer un reoj que se actualice   
import time
import os
while True:
    hora = time.strftime ("%H:%M:%S")
    os.system("cls")
    print(hora)
    time.sleep(1)