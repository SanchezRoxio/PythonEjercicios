'''
Dra. Rocio Sanchez (Diagnostico Veterinario)
Es necesario registrar el ingreso de las mascotas en la próxima hora (solo se pueden atender 20 mascotas), 
para esto hay que considerar los siguientes datos y encasillarlos en ciertos diagnósticos para poder derivarlos 
adecuadamente:
-Edad (Validar entre 1 y 25 años) 
-Tipo: (Validar “gato”, “perro”, “loro”) 
-Peso: (Más de 0 kg) -
-Diagnóstico: (Validar “problemas digestivos”, “parásitos”, “infección”)
-Vacuna antirrábica (validar “si”, ”no”)
CALCULAR
1. Cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, 
que se presentaron por infección o parásitos.
2. El tipo de mascota más ingresada con problemas digestivos.
3. Edad y tipo de la mascota más vieja con vacuna antirrábica.
4. Porcentaje de mascotas vacunadas y no vacunadas.
5. Promedio de edad de los gatos..
'''
total_mascotas = 0 
contador_sinvacunaantirrabica = 0
contador_perros = 0
contador_loros = 0
edad_mayor_mascota_vac = -float('inf')  # Se inicializa con negativo infinito para asegurar que cualquier edad será mayor
tipo_mascotavac = ''
bandera_mayormascotavacuna = False
contador_mascotasvacunadas = 0
contador_mascotasnovacunadas = 0
total_edad_gatos = 0
contador_gatos = 0
t_gatos = 'gato'
t_perros = 'perro'
t_loros = 'loro'

for _ in range(20):
    
    while True:
        edad_mascota = int(input("Ingrese la edad de su mascota: "))
        if edad_mascota < 1 or edad_mascota > 20: 
            print("La edad no puede ser menor a 1 ni mayor a 20. Ingrese nuevamente.")
        else: 
            break

    while True:
        tipo_mascota = input("Ingrese su tipo (gato/perro/loro): ").lower()
        if tipo_mascota in ['gato', 'perro', 'loro']:
            break
        else:
            print("Error. Ingrese 'gato', 'perro' o 'loro'.")

    while True:
        peso_mascota = int(input("Ingrese su peso: "))
        if peso_mascota < 0: 
            print("El peso no puede ser menor a 0. Ingrese nuevamente.")
        else: 
            break
    
    while True:
        diagnostico_mascota = input("Ingrese su diagnóstico (problemas digestivos/parasitos/infeccion): ").lower()
        if diagnostico_mascota in ['problemas digestivos', 'parasitos', 'infeccion']:
            break
        else:
            print("Error. Ingrese 'problemas digestivos', 'parasitos' o 'infeccion'.")
    
    while True:
        vacuna_mascota = input("¿Tiene la vacuna antirrabica? (si/no): ").lower()
        if vacuna_mascota in ['si', 'no']:
            break
        else:
            print("Error. Ingrese 'si' o 'no'.")
    
    # 1. Cantidad de mascotas sin vacuna antirrábica, cuya edad está entre los 4 y 12 años, que se presentaron por infección o parásitos.
    if (diagnostico_mascota in ['parasitos', 'infeccion']) and 4 <= edad_mascota <= 12 and vacuna_mascota == "no":
        contador_sinvacunaantirrabica += 1

    # 2. El tipo de mascota más ingresada con problemas digestivos.
    if diagnostico_mascota == 'problemas digestivos':
        if tipo_mascota == 'gato':
            contador_gatos += 1
        elif tipo_mascota == 'perro':
            contador_perros += 1
        elif tipo_mascota == 'loro':
            contador_loros += 1
  
    # 3. Edad y tipo de la mascota más vieja con vacuna antirrábica.
    if vacuna_mascota == 'si':
        if edad_mascota > edad_mayor_mascota_vac or not bandera_mayormascotavacuna:
            edad_mayor_mascota_vac = edad_mascota
            tipo_mascotavac = tipo_mascota
            bandera_mayormascotavacuna = True

    # 4. Porcentaje de mascotas vacunadas y no vacunadas.
    if vacuna_mascota == 'si':
        contador_mascotasvacunadas += 1
    elif vacuna_mascota == 'no':
        contador_mascotasnovacunadas += 1

    # 5. Promedio de edad de los gatos.
    if tipo_mascota == 'gato':
        total_edad_gatos += edad_mascota
        contador_gatos += 1
        
    total_mascotas += 1

# Imprimir todo por pantalla :D
print(f"La cantidad de mascotas sin vacuna, cuya edad está entre los 4 y 12 años que se presentaron por infección o parásitos es: {contador_sinvacunaantirrabica}")

if total_mascotas > 0:
    if contador_gatos > contador_perros and contador_gatos > contador_loros:
        tipomascota_mas_ingresada = t_gatos
    elif contador_perros > contador_loros:
        tipomascota_mas_ingresada = t_perros
    else:
        tipomascota_mas_ingresada = t_loros
    
    print(f"El tipo de mascota más ingresada con problemas digestivos es: {tipomascota_mas_ingresada}")

# Porcentaje de mascotas vacunadas y no vacunadas.
if total_mascotas > 0:
    porcentaje_mascotasvacunadas = (contador_mascotasvacunadas / total_mascotas) * 100
    porcentaje_mascotasnovacunadas = (contador_mascotasnovacunadas / total_mascotas) * 100
    
    print(f"El porcentaje de mascotas vacunadas es: {porcentaje_mascotasvacunadas:.2f}%")
    print(f"El porcentaje de mascotas no vacunadas es: {porcentaje_mascotasnovacunadas:.2f}%")

# Promedio de edad de los gatos
if contador_gatos > 0:
    promedio_edad_gatos = total_edad_gatos / contador_gatos
    print(f"El promedio de edad de los gatos es: {promedio_edad_gatos:.2f} años.")
else:
    print("No se ingresaron gatos.")