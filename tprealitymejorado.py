print("🏆 TP: While_Reality_Show")
print("Registro de los Jugadores!")

# Inicialización de variables
cont = 1
votosMa = float('-inf')
votosMe = float('inf')
nombreMas = ""
nombreMenos = ""
edadMenos = 0
sumaEdades = 0
totalVotos = 0

# Bucle para ingresar datos de 3 jugadores
while cont <= 3:
    nombre = input("Ingrese el nombre del jugaror: ")

    # Manejo de entrada de edad con try-except por si se ingresa un valor que no sea numerico.
    while True:
        try:
            edad = int(input("Ingrese la edad del jugador (Mayor a 25): "))
            if edad <= 25:
                print("La edad debe ser mayor a 25.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número entero para la edad.")

    # aca es lo mismo.
    while True:
        try:
            votos = int(input("Ingrese la cantidad de votos: "))
            if votos < 0:
                print("La cantidad de votos no puede ser menor a 0.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número entero para los votos.")

    # Guardo al participante con más votos
    if votos > votosMa:
        votosMa = votos
        nombreMas = nombre

    # Aca con menos votos
    if votos < votosMe:
        votosMe = votos
        nombreMenos = nombre
        edadMenos = edad
        
    # Suma de edades y total de votos
    sumaEdades += edad
    totalVotos += votos
    cont += 1  # Incremento del contador del while del principio solo para los 3 jugadores
# Cálculo del promedio de edades
promedioEdades = sumaEdades / 3
# Muestra por pantalla todo, un exito
print("El candidato con más votos es:", nombreMas)
print("El candidato con menos votos es:", nombreMenos, "de", edadMenos, "años.")
print("El promedio de las edades es:", promedioEdades)
print("El total de votos emitidos son:", totalVotos)
