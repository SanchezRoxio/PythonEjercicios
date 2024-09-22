def obtener_numeros():
    numeros = []
    while True:
        entrada = input("Ingresa un numero entero (o escribe 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingresa un numero entero valido.")
    return numeros