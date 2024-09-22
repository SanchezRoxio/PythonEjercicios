import os 
import random
from ejercicioarraydefobtener import *

'''Ejercicio 1'''
# def calcular_promedio(lista):
#     if not lista:
#         return 0
#     return sum(lista) / len(lista)

# numeros = obtener_numeros()
# promedio = calcular_promedio(numeros)
# print(f"El promedio es: {promedio}")

'''Ejercicio 2'''

# def calcular_promedio_positivos(lista):
#     numeros_positivos = []
#     for num in lista:
#         if num > 0:  # comprobamos si es positivo
#             numeros_positivos.append(num)  #añadimos el numero a la lista
#     if not numeros_positivos:  # Verificar si la lista esta vacia
#         return 0
#     return sum(numeros_positivos) / len(numeros_positivos)  # Calcula el promedio

# numeros = obtener_numeros()
# promedio_positivos = calcular_promedio_positivos(numeros)
# print(f"El promedio de los numeros positivos es: {promedio_positivos}")

'''Ejercicio 3'''
# def calcular_producto(lista):
#     producto = 1
#     for num in lista:
#         producto *= num  #multiplicamos el numero actual al producto
#     return producto  #retornamos

# numeros = obtener_numeros()
# producto_total = calcular_producto(numeros)
# print(f"El producto de los elementos es: {producto_total}")

'''Ejercicio 4'''

# def indice_maximo(lista):
#     if not lista:
#         return None
#     maximo = lista[0]
#     indice = 0

#     for i in range(1, len(lista)):
#         if lista[i] > maximo:
#             maximo = lista[i]
#             indice = i
#     return indice

# numeros = obtener_numeros()
# indice_max = indice_maximo(numeros)
# if indice_max is not None:
#     print(f"El indice del valor maximo es: {indice_max}")
# else:
#     print("La lista esta vacia.")

'''Ejercicio 5'''

# def indice_maximo(lista):
#     if not lista:
#         return None
#     maximo = lista[0]
#     indice = 0
#     for i in range(1, len(lista)):
#         if lista[i] > maximo:
#             maximo = lista[i]
#             indice = i
#     return indice

# def mostrar_indice_y_valor_maximo(lista):
#     indice = indice_maximo(lista)
#     if indice is not None:
#         print(f"El indice del valor maximo es: {indice} y su valor es: {lista[indice]}")
#     else:
#         print("La lista esta vacia.")

# numeros = obtener_numeros()
# mostrar_indice_y_valor_maximo(numeros)

'''Ejercicio 6'''

# def indices_maximo(lista):
#     if not lista:  
#         return [] 
#     maximo = max(lista) 
#     indices = []  
    
#     for i in range(len(lista)):  
#         if lista[i] == maximo:  
#             indices.append(i)          
#     return indices

# numeros = obtener_numeros()
# indices_max = indices_maximo(numeros)
# print(f"Los indices del valor maximo son: {indices_max}")

'''Ejercicio 7'''

# def indices_maximo(lista):
#     if not lista: 
#         return []   
#     maximo = max(lista) 
#     indices = [] 
    
#     for i in range(len(lista)): 
#         if lista[i] == maximo:  
#             indices.append(i)             
#     return indices 

# def mostrar_indices_y_valores_maximo(lista):
#     indices = indices_maximo(lista) 
#     if indices: 
#         for indice in indices: 
#             print(f"Indice: {indice}, Valor: {lista[indice]}")
#     else:
#         print("La lista esta vacia.")

# numeros = obtener_numeros()
# mostrar_indices_y_valores_maximo(numeros)

'''Ejercicio 8'''

def generar_sueldos(cantidad, minimo, maximo):
    return [random.randint(minimo, maximo) for _ in range(cantidad)]

def calcular_porcentaje_superan_promedio(sueldos):
    # Calcula el salario promedio
    suma_sueldos = sum(sueldos)
    cantidad_sueldos = len(sueldos)
    promedio = suma_sueldos / cantidad_sueldos

    #cuenta cuantos sueldos superan el promedio
    superan_promedio = 0
    for sueldo in sueldos:
        if sueldo > promedio:
            superan_promedio += 1
    #porcentaje
    porcentaje = (superan_promedio / cantidad_sueldos) * 100
    return promedio, porcentaje

#definición de parametros
cantidad_sueldos = 10
minimo_sueldo = 350000
maximo_sueldo = 1250000
#generar sueldos
sueldos = generar_sueldos(cantidad_sueldos, minimo_sueldo, maximo_sueldo)

#calcular promedio y porcentaje
promedio, porcentaje = calcular_porcentaje_superan_promedio(sueldos)

print(f"Sueldos generados: {sueldos}")
print(f"Salario promedio: ARS {promedio:.2f}")
print(f"Porcentaje de personas que superan el salario promedio: {porcentaje:.2f}%")