'''Ejercicio 1'''
# def sumar_naturales(numero: int) -> int:
#     if numero == 1:
#         return 1
#     else:
#         return numero + sumar_naturales(numero - 1)

# numero = int(input("Ingrese un numero: "))
# print(f"La suma de los números naturales desde {numero} hasta 1 es: {sumar_naturales(numero)}")

'''Ejercicio 2'''
# def calcular_potencia(base: int, exponente: int) -> int:
#     if exponente == 0:
#         return 1
#     else:
#         return base * calcular_potencia(base, exponente - 1)

# base = int(input("Ingrese la base: "))
# exponente = int(input("Ingrese el exponente: "))
# print(f"{base} elevado a la potencia de {exponente} es: {calcular_potencia(base, exponente)}")

'''Ejercicio 3'''
def calcular_fibonacci(numero: int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    #la suma de los dos numeros Fibonacci anteriores
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

numero = int(input("Ingrese el numero para calcular el Fibonacci: "))
resultado = calcular_fibonacci(numero)
print(f"El numero de Fibonacci en la posicion {numero} es: {resultado}")