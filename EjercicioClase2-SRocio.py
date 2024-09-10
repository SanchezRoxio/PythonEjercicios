'''Ejercicio 1'''

# for i in range (1,11,1):
#     print(i)

'''Ejercicio 2'''

#for i in range (10,0,-1):
#     print(i)

'''Ejercicio 3'''

# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))

# if num1 == num2:
#     print(num1)

# elif num1 < num2:
#     for i in range(num1, num2 + 1):
#             print(i, end="-")  
# else:
#     for i in range(num1, num2 - 1, -1):
#             print(i, end="-")
        
'''Ejercicio 4'''

# suma = 0
# contador = 0

# for i in range(5):
#     num = int(input("Ingresa un numero (0 para salir): "))
#     if num == 0:
#         break
#     suma += num
#     contador += 1

# promedio = suma / contador 
# if contador > 0:
#     promedio = suma / contador
# else:
#     promedio = 0

# print("Suma:", suma)
# print("Promedio:", promedio)

'''Ejercicio 5'''

#for num in range(2, 101, 2):
#    print(num)

'''Ejercicio 6'''

# num = int(input("Ingresa un numero: "))
# bandera = True

# for i in range(2, num + 1):
#     if num % 1 == 0:
#         bandera = False
#         break
# if bandera and num > 1:
#     print("Es primo.")
# else:
#     print("No es primo.")

'''Ejercicio 7'''
'''For anidado'''

# num = int(input("Ingresa un numero: "))
# cantidad = 0

# for i in range(2, num + 1):
#     es_primo = True
#     for a in range(2, i):
#         if i % a == 0:
#             es_primo = False
#             break
#     if es_primo:
#         cantidad += 1
#         print(i)  

# print(f"Cantidad de numeros primos encontrados: {cantidad}")

'''Ejercicio 8'''

# num = int(input("Ingresa un numero: "))
# for i in range(1, 11):
#     producto = num * i
#     print(f"{num} x {i} = {producto}")