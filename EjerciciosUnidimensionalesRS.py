'''Ejercicio 1'''
# def ordenar_lista(lista):
#     #verificar si la lista ya esta ordenada
#     esta_ordenada = False
#     #len: obtiene la longitud (o el n de elementos) de un objeto, como una lista, una cadena, etc
#     for i in range(len(lista)):
#         for j in range(0, len(lista) - i - 1):
#             if lista[j] > lista[j + 1]:
#                 esta_ordenada = True
#                 #intercambia
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#     return esta_ordenada

# lista = [3, 1, 2, 9, 10, 22, 4, 50]
# resultado = ordenar_lista(lista)
# print(lista) 
# print(resultado)

'''Ejercicio 2'''
# def ordenar_lista(lista):
#     #verificar si la lista ya esta ordenada
#     esta_ordenada = True
#     #len: obtiene la longitud (o el n de elementos) de un objeto, como 1 lista, 1 cadena, etc
#     #el metodo burbuja
#     for i in range(len(lista)):
#         for j in range(0, len(lista) - i - 1):
#             if lista[j] < lista[j + 1]:
#                 esta_ordenada = False
#                 #intercambia
#                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
#     return esta_ordenada

# lista = [3, 1, 2, 9, 10, 22, 4, 50]
# resultado = ordenar_lista(lista)
# print(lista) 
# print(resultado)

'''Ejercicio 3'''