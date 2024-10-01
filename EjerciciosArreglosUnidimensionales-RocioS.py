'''Ejercicio 1'''

# def contar_largos(lista):
#     contador = 0  #iniciar el contador
#     for elemento in lista:  #recorremos cada elemento de la lista
#         if len(elemento) > 5:  #verificamos si tiene mas de 5 caracteres
#             contador += 1  #incrementamos el contador
#     return contador  #retornamos

# lista_de_strings = ["hola", "mundo", "programación", "python", "desarrollador", "código"]
# resultado = contar_largos(lista_de_strings)
# print(f"La cantidad de elementos con más de cinco caracteres es: {resultado}")

'''Ejercicio 2'''

# def filtrar_largos(lista):
#     nueva_lista = []  # Inicializamos una lista vacía
#     for elemento in lista:  # Recorremos cada elemento de la lista
#         if len(elemento) > 5:  # Verificamos si tiene más de cinco caracteres
#             nueva_lista.append(elemento)  # Agregamos el elemento a la nueva lista
#     return nueva_lista  # Retornamos la nueva lista

# # Ejemplo de uso
# lista_de_strings = ["hola", "mundo", "programación", "python", "desarrollador", "código"]
# resultado = filtrar_largos(lista_de_strings)
# print(f"La nueva lista con elementos de más de cinco caracteres es: {resultado}")

'''Ejercicio 3'''

# def nombres_mas_cortos():
#     nombres = []  #lista vacía
#     #Pedimos ingresar
#     for i in range(5):
#         nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
#         nombres.append(nombre)  #agregamos el nombre a la lista

#     #encontrar la longitud mínima de los nombres
#     longitud_minima = len(nombres[0])  #inicializamos
    
#     for nombre in nombres:  #Recorremos 
#         if len(nombre) < longitud_minima:  #si se encuentra un nombre + corto
#             longitud_minima = len(nombre)  #actualizamos 

#     nombres_cortos = []  #inicializamos una lista para los nombres + cortos
#     for nombre in nombres:
#         if len(nombre) == longitud_minima:  #si el nombre tiene la longitud mínima
#             nombres_cortos.append(nombre)  #agregamos a la lista
#     return nombres_cortos  #retornamos la lista de nombres + cortos

# resultado = nombres_mas_cortos()
# print(f"Los nombres más cortos son: {resultado}")

'''Ejercicio 4'''

# def contar_apellidos_repetidos(apellidos_comunes):
#     apellidos_ingresados = []  #inicializa una lista para los apellidos ingresados
    
#     for i in range(10):
#         apellido = input(f"Ingrese el apellido {i + 1}: ")
#         apellidos_ingresados.append(apellido)  #agregamos el apellido a la lista

#     #contar las repeticiones de los apellidos comunes
#     conteo_repetidos = {}
    
#     for apellido in apellidos_comunes:
#         conteo_repetidos[apellido] = apellidos_ingresados.count(apellido)  #contamos

#     #mostramos el resultado
#     for apellido, cantidad in conteo_repetidos.items():
#         print(f"{apellido} se repite {cantidad} veces")

# # Ejemplo de uso
# apellidos_comunes = ["lopez", "gomez", "fernandez", "perez", "martinez"]
# contar_apellidos_repetidos(apellidos_comunes)

'''Ejercicio 5'''

# def cargar_personas():
#     nombres = []  #lista para almacenar nombres
#     edades = []   #lista para almacenar edades

#     #cargar 5 nombres y edades
#     for i in range(5):
#         nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
#         edad = int(input(f"Ingrese la edad de {nombre}: "))
#         nombres.append(nombre)  #agregar nombre a la lista
#         edades.append(edad)   #agregar edad a la lista
#     return nombres, edades  #retornar listas

# def mostrar_mayores(nombres, edades):
#     print("Personas mayores de edad:")
#     for i in range(len(nombres)):
#         if edades[i] >= 18:  #verificar si es mayor de edad
#             print(nombres[i])  #imprimir el nombre

# nombres, edades = cargar_personas()  #cargar datos
# mostrar_mayores(nombres, edades)     #mostrar los mayores de edad

'''Ejercicio 6'''

# def cargar_productos():
#     productos = [] 
#     precios = [] 
#     #cargar productos y precios
#     for i in range(5):
#         producto = input(f"Ingrese el nombre del producto {i + 1}: ")
#         precio = float(input(f"Ingrese el precio de {producto}: "))
#         productos.append(producto)  #Agregar producto a la lista
#         precios.append(precio)      #Agregar precio a la lista

#     return productos, precios  #retornar listas

# def mostrar_productos_mayores(precios):
#     precio_base = precios[0]  #tomar el precio del primer producto
#     contador = 0  #inicializo contador

#     for precio in precios:
#         if precio > precio_base:  #verificar si el precio es mayor que el primero
#             contador += 1  #incrementar el contador
#     print(f"La cantidad de productos con un precio mayor al primer producto es: {contador}")
# #uso
# productos, precios = cargar_productos()  #cargar datos
# mostrar_productos_mayores(precios)       #mostrar cantidad de productos mayores

'''Ejercicio 7'''

import random

def cargar_alumnos():
    alumnos = []

    for i in range(5):
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
        apellido = input(f"Ingrese el apellido del alumno {i + 1}: ")
        
        #validar que el legajo entre 10000 y 99999
        while True:
            legajo = int(input(f"Ingrese el legajo del alumno {i + 1} (entre 10000 y 99999): "))
            if 10000 <= legajo <= 99999:
                break
            else:
                print("El legajo debe estar entre 10000 y 99999. Intente nuevamente.")

        #notas aleatorias entre 1 y 10
        nota1 = random.randint(1, 10)
        nota2 = random.randint(1, 10)
        #promedio
        promedio = (nota1 + nota2) / 2
        #agregar la información del alumno a la lista
        alumnos.append({
            "nombre": nombre,
            "apellido": apellido,
            "legajo": legajo,
            "promedio": promedio
        })
    return alumnos

def mostrar_mejores_alumnos(alumnos):
    max_promedio = 0  #Inicializo el promedio maximo
    
    #buscar el promedio mas alto
    for alumno in alumnos:
        if alumno["promedio"] > max_promedio:
            max_promedio = alumno["promedio"]
    
    mejores_alumnos = []  #almacena los mejores
    
    #filtrar alumnos que tienen el promedio mas alto
    for alumno in alumnos:
        if alumno["promedio"] == max_promedio:
            mejores_alumnos.append(alumno)  #agregar a la lista de los mejores

    #mostrar resultados
    print("Los alumnos con la nota promedio mas alta son:")
    for alumno in mejores_alumnos:
        print(f"{alumno['nombre']} {alumno['apellido']} (Legajo: {alumno['legajo']}) - Promedio: {alumno['promedio']}")

alumnos = cargar_alumnos()  #cargar datos de los alumnos
mostrar_mejores_alumnos(alumnos)  #mostrar los alumnos con el promedio mas alto