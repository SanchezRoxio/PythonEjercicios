'''Ejercicio 1'''
# def calcular_promedio(acumulador, contador):
#     '''
#     Calcula el promedio 
#     '''
#     if contador == 0:
#         promedio = 0
#     else:
#         promedio = acumulador / contador
#     return promedio

# resultado = calcular_promedio(float(input("Ingrese el acumulador: ")), float(input("Ingrese el contador: ")))
# if resultado == 0:  #evitar la division por cero
#     print("Error: División por cero")
# else:
#     print(f"Promedio: {resultado}")

'''Ejercicio 2'''
# def calcular_area_rectangulo(base, altura):
#     '''
#     Calcula el area de un rectangulo
#     '''
#     return base * altura
# area = calcular_area_rectangulo( float(input("Ingrese la base: ")), float(input("Ingrese la altura: ")))
# print(f"Área del rectángulo: {area}")

'''Ejercicio 3'''
# def es_par(numero):
#     '''
#     Verifica si un numero es par.
#     '''
#     if numero % 2 == 0:
#         print(f"{numero} es par. ")
#     else:
#         print(f"{numero} no es par.")
#     return es_par

# numero = es_par(int(input("Ingrese un numero: ")))

# '''Ejercicio 4'''
# def es_primo(numero):
#     '''
#     Verifica si un numero es primo e imprime un mensaje apropiado.
#     '''
#     # los numeros menores o iguales a 1 no son primos
#     if numero <= 1:
#         print(f"{numero} no es primo.")
#         return
#     # numero**0.5 saca la raíz cuadrada
#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             print(f"{numero} no es primo.")
#             return    
#     print(f"{numero} es primo.")

# numero = int(input("Ingrese un número: "))
# es_primo(numero)

'''Ejercicio 5'''

# def encontrar_maximo(a, b, c):
#     '''
#     Encuentra el maximo entre tres numeros.
#     return: El mas grande entre a, b y c.
#     '''
#     #inicializamos el máximo con el primer número
#     maximo = a  
#     #comparamos con el segundo
#     if b > maximo:
#         maximo = b
#     #comparamos con el tercero
#     if c > maximo:
#         maximo = c
#     return maximo

# a = int(input("Ingrese un número: "))
# b = int(input("Ingrese un número: "))
# c = int(input("Ingrese un número: "))
# print(f"El maximo es: {encontrar_maximo(a, b, c)}") #el max

'''Ejercicio 6'''
# def encontrar_minimo(a, b, c):
#     '''
#     Encuentra el minimo entre tres numeros.
#     return:el numero minimo entre a, b y c.
#     '''
#     #inicializamos el máximo con el primer número
#     minimo = a  
#     #comparamos con el segundo
#     if b < minimo:
#         minimo = b
#     #comparamos con el tercero
#     if c < minimo:
#         minimo = c
#     return minimo

# aaa = int(input("Ingrese un número: "))
# bbb = int(input("Ingrese un número: "))
# ccc = int(input("Ingrese un número: "))
# print(f"El minimo es: {encontrar_minimo(aaa, bbb, ccc)}") #el min

'''Ejercicio 7'''
# def multiplicacion(a,b):
#     '''
#     Multiplica 2 numeros
#     '''
#     return a*b
# a = int(input("Ingrese un número: "))
# b = int(input("Ingrese un número: "))
# print(f"El resultado de la multiplicacion es: {multiplicacion(a,b)}")  #resultado