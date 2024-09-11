import os 
from funciones import *

a = None 
b = None 
resultado = None

def menu():
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
        opcion = int(input("Su opcion: "))
        
        if opcion == 1:
            a = ingresar_operando()
        elif opcion == 2:
            b = ingresar_operando()
        elif opcion == 3:
            resultado = calcular_operaciones(a,b)
            print("\nSe realizaron los calculos.")
        elif opcion == 4:
            mostrar_resultados(resultado)
        elif opcion == 5:
            print("Saliendo.")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")

        input("Pulse boton para continuar.\n")
menu()