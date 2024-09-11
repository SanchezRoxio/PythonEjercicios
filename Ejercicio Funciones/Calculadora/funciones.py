def ingresar_operando():  
    while True:
        return  int(input("Ingrese Operando: "))

def sumar (a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b 

def dividir(a,b):
    if(b >= 0):
        return a / b
    else:
        return "No se puede dividir por 0."
    
def potencia(a,b):
        return a ** b

def resto(a,b):
    if(b >= 0):
        return a % b
    else:
        return "No se puede dividir por 0."

def factorial(n):
    if n < 0:
        return "\nEl factorial solo esta definido para enteros no negativos."
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def calcular_operaciones(a, b):
    if a is None or b is None:
        print("Primero ingrese los operandos.")
    suma = sumar(a, b)
    resta = restar(a, b)
    division = dividir(a, b)
    multiplicacion = multiplicar(a, b)
    potenciar = potencia(a, b)
    restos = resto(a, b)
    factorial_a = factorial(a)
    factorial_b = factorial(b)
    return [suma, resta, division, multiplicacion, potenciar, restos, factorial_a, factorial_b]
         
def mostrar_resultados(resultados):
    if resultados is None:
        print("No se han calculado las operaciones.")
        return    
    print(f"El resultado de A + B es: {resultados[0]}")
    print(f"El resultado de A - B es: {resultados[1]}")
    print(f"El resultado de A / B es: {resultados[2]}")
    print(f"El resultado de A * B es: {resultados[3]}")
    print(f"A elevado a la B da como resultado: {resultados[4]}")
    print(f"El resultado de A % B es: {resultados[5]}")
    print(f"El factorial de A es: {resultados[6]} \n El factorial de B es: {resultados[7]}")