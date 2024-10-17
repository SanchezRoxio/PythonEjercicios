'''Ejercicio 1'''

# def validar_dimensiones(matriz_a, matriz_b):
#     """Valida que ambas matrices tengan las mismas dimensiones."""
#     if len(matriz_a) != len(matriz_b):
#         return False
#     if len(matriz_a) > 0 and len(matriz_a[0]) != len(matriz_b[0]):
#         return False
#     return True

# def sumar_matrices(matriz_a, matriz_b):
#     """Suma dos matrices si tienen las mismas dimensiones."""
#     if not validar_dimensiones(matriz_a, matriz_b):
#         return []  # si las dimensiones no coinciden se retorna vacia
    
#     filas = len(matriz_a)
#     columnas = len(matriz_a[0])
    
#     # Crear una matriz resultado con ceros
#     matriz_resultado = [[0 for _ in range(columnas)] for _ in range(filas)]
    
#     # Realizar la suma
#     for i in range(filas):
#         for j in range(columnas):
#             matriz_resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]
    
#     return matriz_resultado

# matriz_a = [[1, 2, 3], [4, 5, 6]]
# matriz_b = [[7, 8, 9], [10, 11, 12]]

# resultado = sumar_matrices(matriz_a, matriz_b)
# print(resultado)

'''Ejercicio 2'''

# def multiplicar_matriz_por_escalar(matriz, escalar):
#     """Multiplica una matriz por un escalar y devuelve la matriz resultante."""
#     #Obtener dimensiones de la matriz
#     filas = len(matriz)
#     columnas = len(matriz[0])
    
#     #crear una matriz resultado con las mismas dimensiones que la original
#     matriz_resultado = []
#     for i in range(filas):
#         fila_resultado = []  #inicializa una nueva fila para la matriz resultado
#         for j in range(columnas):
#             fila_resultado.append(0)  #añadir ceros a la fila
#         matriz_resultado.append(fila_resultado)  #añadir la fila a la matriz resultado
    
#     #Multiplicar cada elemento de la matriz por el escalar
#     for i in range(filas):
#         for j in range(columnas):
#             matriz_resultado[i][j] = matriz[i][j] * escalar
            
#     return matriz_resultado

# matriz = [[1, 2, 3], [4, 5, 6]]
# escalar = 3
# resultado = multiplicar_matriz_por_escalar(matriz, escalar)
# print(resultado)

'''Ejercicio 3'''

# def matriz_opuesta(matriz):
#     """Calcula y retorna la matriz opuesta de la matriz dada."""
#     #Crear una matriz resultado con las mismas dimensiones que la original
#     matriz_resultado = []
    
#     for i in range(len(matriz)):
#         fila_resultado = []  #Inicializa una nueva fila para la matriz opuesta
#         for j in range(len(matriz[0])):
#             fila_resultado.append(-matriz[i][j])  # Multiplica por -1
#         matriz_resultado.append(fila_resultado)  # Añadir la fila a la matriz opuesta
    
#     return matriz_resultado

# matriz = [[1, 2, 3], [4, 2, 6]]
# resultado = matriz_opuesta(matriz)
# print(resultado) 

'''Ejercicio 4'''

# def matriz_traspuesta(matriz):
#     """Calcula y retorna la matriz traspuesta de la matriz dada."""
#     # Inicializa la matriz resultado con dimensiones intercambiadas
#     matriz_resultado = []
    
#     #recorre las columnas de la matriz original
#     for j in range(len(matriz[0])):
#         fila_resultado = [] 
#         #recorre las filas de la matriz original
#         for i in range(len(matriz)):
#             fila_resultado.append(matriz[i][j])  #añade el elemento de la fila original
#         matriz_resultado.append(fila_resultado)  #añade la fila a la matriz traspuesta
    
#     return matriz_resultado

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# resultado = matriz_traspuesta(matriz)
# print(resultado)

'''Ejercicio 5'''

def validar_multiplicacion(matriz_a, matriz_b):
    """Valida si la multiplicación de matriz_a y matriz_b es posible."""
    # Retorna True si la cantidad de columnas de matriz_a es igual a la cantidad de filas de matriz_b
    return len(matriz_a[0]) == len(matriz_b)

def multiplicar_matrices(matriz_a, matriz_b):
    """Multiplica dos matrices si la multiplicación es válida y devuelve la matriz resultante."""
    if validar_multiplicacion(matriz_a, matriz_b) == False:
        return []  #retorna una lista vacía si la multiplicación no es válida
    
    filas_a = len(matriz_a)
    columnas_a = len(matriz_a[0])
    columnas_b = len(matriz_b[0])
    
    #matriz resultado con ceros
    matriz_resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]
    
    #realizar la multiplicación
    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_a):  # O la cantidad de filas de matriz_b
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    
    return matriz_resultado

matriz_a = [[1, 2, 3], [4, 5, 6]]
matriz_b = [[7, 8], [9, 10], [11, 12]]

resultado = multiplicar_matrices(matriz_a, matriz_b)
print(resultado)