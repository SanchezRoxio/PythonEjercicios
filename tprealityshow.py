 #Informar:
#a. nombre del candidato con más votos
#b. nombre y edad del candidato con menos votos
#c. el promedio de edades de los candidatos
#d. total de votos emitidos.
#Todos los datos se ingresan mediante input

print("🏆 TP: While_Reality_Show")
print("Registro de los Jugadores!")
#Inicializo la variable del contador
cont = 1
votosMa = float('inf')
votosMe = float('-inf')
nombreMas = ""
nombreMenos = ""
#se inicializa en 0 para almacenar la edad del participante con menos votos
edadMe = 0
edadt = 0
votost = 0
#el while se ejecuta 3 veces
while cont <= 3:
    nombre = input("Ingrese el nombre del participante: ")
    edad = int(input("Ingrese la edad del participante (Mayor a 25): "))
    #Comparo la edad, si es o no mayor a 25
    while edad < 25:
        print("La edad debe ser mayor a 25.")
        edad = int(input("Ingrese la edad del participante (Mayor a 25): "))
    #Comparo los votos, no pueden ser menor a 0
    votos = int(input("Ingrese la cantidad de votos: "))
    while votos < 0:   
        print("La cantidad de votos no puede ser 0")
        votos = int(input("Ingrese la cantidad de votos: "))
    #guardo en la variable votosMa si se ingresa un numero grande, si no es asi, se va a reemplazar por otro que sea mayor.
    if cont == 1 or votos > votosMa:
        votosMa = votos
        nombreMas = nombre
    #aca lo mismo que antes pero con el menor voto y guarda la menor edad
    if cont == 1 or votos < votosMe:
        votosMe = votos
        nombreMenos = nombre
        edadMe = edad
    #hago los contadores que autosumen las edades y los votos
    edadt += edad
    votost += votos
    #contador del bucle while que se repita 3 veces
    cont = cont + 1
    #y finalizo con el calculo del promedio.
    promedad = edadt/3

print("El candidato con mas votos es: " , nombreMas)
print("El candidato con menos votos es: " , nombreMenos ," de " ,edadMe, " años." )
print("El promedio de las edades es: ", promedad)
print("El total de votos emitidos son: ", votost)
#se muestra todo por pantalla, un exito 