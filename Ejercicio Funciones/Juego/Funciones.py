import random
import os

#Constantes -> para fecilitar el uso de eso números.
PIEDRA = 1
PAPEL = 2
TIJERA = 3
MAYOR = 1
MENOR = 2

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...\n")
    os.system('cls')

#PEDIR DATOS
def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    numero = int(input(mensaje))
    while numero > maximo or numero < minimo:
        numero = int(input(mensaje_error))
    
    return numero

#RANKINGS
def calcular_maximo(numero_uno:int,numero_dos:int) -> int:
    if numero_uno > numero_dos:
        return numero_uno
    else:
        return numero_dos

def calcular_porcentaje(cantidad_victorias:int,cantidad_partidas:int)->float:
    porcentaje = cantidad_victorias / cantidad_partidas * 100
    return porcentaje

#JUEGOS EN GENERAL
def generar_respuesta_maquina(minimo:int,maximo:int) -> int:
    resultado = random.randint(minimo, maximo)
    return resultado

#PIEDRA PAPEL O TIJERA
def verificar_ganador_ronda(respuesta_jugador:int,respuesta_maquina:int) -> str:

    if (respuesta_jugador == PIEDRA and respuesta_maquina == TIJERA) or (respuesta_jugador == PAPEL and respuesta_maquina == PIEDRA) or (respuesta_jugador == TIJERA and respuesta_maquina == PAPEL):
        ganador = "Jugador"
    
    elif (respuesta_maquina == PIEDRA and respuesta_jugador == TIJERA) or (respuesta_maquina == PAPEL and respuesta_jugador == PIEDRA) or (respuesta_maquina == TIJERA and respuesta_jugador == PAPEL):
        ganador = "Máquina"
    else:
        ganador = "Empate"

    return ganador

def verificar_ganador_partida(aciertos_jugador:int,aciertos_maquina:int) -> str:
    if aciertos_jugador > aciertos_maquina:
        ganador = "Ganaste!!!" 
    else:
        ganador = "Perdiste!!!"
    return ganador

def verificar_estado_partida(aciertos_jugador:int,aciertos_maquina:int,ronda_actual:int) -> bool:
    retorno = True
    if aciertos_jugador == 2 or aciertos_maquina == 2:
        retorno = False
    
    elif ronda_actual > 2:
        if aciertos_jugador > aciertos_maquina or aciertos_maquina > aciertos_jugador:
            retorno = False
    return retorno

def obtener_elemento(respuesta:int) -> str:
    if respuesta == 1:
        retorno = "PIEDRA"
    elif respuesta == 2:
        retorno = "PAPEL"
    else:
        retorno = "TIJERA"    
    return retorno

def jugar_piedra_papel_tijera() -> str:
    aciertos_jugador = 0
    aciertos_maquina = 0
    contador_rondas = 0
    
    print("Bienvenido a la partida de Piedra Papel o Tijera!")

    while verificar_estado_partida(aciertos_jugador,aciertos_maquina,contador_rondas):
        contador_rondas +=1
        print(f"Ronda: {contador_rondas}")
        
        numero_jugador = pedir_numero("Ingrese una opción:\nPiedra (1), Papel (2) o Tijera (3): ","Ingrese una opción válida.\nPiedra (1), Papel (2) o Tijera (3): ",1,3)
        numero_maquina = generar_respuesta_maquina(1,3)

        ganador_ronda = verificar_ganador_ronda(numero_jugador, numero_maquina)
        print(f"La máquina eligió {obtener_elemento(numero_maquina)}")

        if ganador_ronda == "Jugador":
            aciertos_jugador += 1
        
        elif ganador_ronda == "Máquina":
            aciertos_maquina += 1
        #Pista: Debo elegir el elemento de la maquina
        #Pista: Debo saber quien gano la ronda (deberia mostrarlo tambien)                     
        #NO BORRAR
        limpiar_consola()
        
    #Pista: Debo saber quien gano la partida
    ganador = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
         
    return ganador
        
        
#ADIVINA EL NUMERO
def mostrar_mensaje_final(puntaje_final:int)->None:
    print("??????? (Ver documento)")

def jugar_adivina_numero() -> int:
    contador_intentos = 3
    puntaje_final = 0
    
    while(contador_intentos != 0):
        #Pista debo reutilizar funciones anteriores que use en el de piedra papel tijera no hacer todo de cero.
        
        print(f"Intentos restantes: {contador_intentos}")
        #NO BORRAR
        limpiar_consola()
    
    return puntaje_final

#MAYOR MENOR
def verificar_cartas(carta:int, carta_posterior:int,eleccion_jugador:int) -> str:    
    pass

def jugar_mayor_menor():
    puntuaje_final = 0 
    
    #Pista : Debo generar primero la carta random antes de jugar
    while(True):
        #Pista : Cuando pierdo debo salir del while
        #NO BORRAR
        limpiar_consola()

    return puntuaje_final
