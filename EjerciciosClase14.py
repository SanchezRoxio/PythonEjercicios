import random

'''Ejercicio 1'''
# def convertir_fecha(fecha):
#     fecha = fecha.replace('-','/')
#     componentes = fecha.split('/')
#     fecha_entera = [int(componentes[0]), int(componentes[1]), int(componentes[2])]
#     return fecha_entera

# fecha = "22/10/2024"
# print(convertir_fecha(fecha))  

'''Ejercicio 2'''
# lista = [1,2,2003]
# separador = "-"
# def convertir_lista (lista,separador):
#     if separador != "-" and separador != "/" or len(lista) != 3:
#         lista_replace = None
#     else:
#         lista_string = [str(lista[0]),str(lista[1]),str(lista[2])]
#         lista_join = separador.join(lista_string)
#         lista_replace = lista_join.replace (",","/")
#     return lista_replace
# print(convertir_lista(lista,separador))

'''Ejercicio 3'''
# def reemplazar_vocales(cadena):
#     for vocal in "aeiouAEIOU":
#         cadena = cadena.replace(vocal, random.choice('abcdefghijklmnopqrstuvwxyz'))
#     return cadena

# texto = "Holis, como estas?"
# print(reemplazar_vocales(texto))

'''Ejercicio 4'''
# def generar_legajo():
#     numero = random.randint(1, 125000)
#     legajo = str(numero).zfill(6)
#     return legajo

# legajo_generado = generar_legajo()
# print(f"Numero de legajo generado: {legajo_generado}")

'''Ejercicio 5'''
'''Ejercicio 6'''