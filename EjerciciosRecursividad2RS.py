'''Ejercicio 1'''
# def verificar_dni(dni: str) -> bool:
#     #verificar la longitud del DNI
#     longitud = len(dni)
#     #verificar si la longitud
#     if 6 <= longitud <= 8:
#         return True
#     else:
#         return False

# dni = input("Ingrese el DNI: ")
# resultado = verificar_dni(dni)
# print(f"El DNI es valido: {resultado}")


'''Ejercicio 2'''
def verificar_dni(dni: str) -> bool:
    """ Verifica si el DNI tiene una longitud valida entre 6 y 8 caracteres. """
    longitud = len(dni)
    return 6 <= longitud <= 8

def completar_dni(dni: str) -> str:
    """ Completa el DNI con ceros a la izquierda hasta alcanzar 8 caracteres o indica si es invalido. """
    if verificar_dni(dni):
        #completar el DNI con ceros a la izquierda
        longitud_actual = len(dni)
        cantidad_ceros = 8 - longitud_actual
        return '0' * cantidad_ceros + dni
    else:
        return "DNI INVALIDO!"

dni = input("Ingrese el DNI: ")
resultado = completar_dni(dni)
print(f"Resultado: {resultado}")