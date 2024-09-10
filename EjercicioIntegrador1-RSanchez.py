productos = 2
bandera = False
bandera_barbijo = False
acumulador_soap = 0 

for i in (0, productos, 1):

    tipo=input("Ingrese el tipo de producto (barbijo, jabon o alcohol): ")
    while tipo != 'barbijo' and tipo != 'jabon' and tipo != 'alcohol':
        tipo=input("Error. Ingrese el tipo de producto (barbijo, jabon o alcohol): ")

    precio = float(input("Ingrese el precio (entre 100/300): "))
    while precio < 100 or precio > 300:
        precio = float(input("Error. Ingrese el precio (entre 100/300): "))

    cantidad = int(input("Ingrese la cantidad (no debe ser 0, ni negativo y ni superar las 1000 unidades): "))
    while cantidad < 1 or cantidad > 1000:
        cantidad = int(input("Ingrese la cantidad (no debe ser 0, ni negativo y ni superar las 1000 unidades): "))
    
    marca = input("Ingrese la marca: ")
    fabricante = input("Ingrese el fabricante: ")

    if tipo == 'barbijo':
        if bandera_barbijo == False or precio > max_precio_barbijo:
            max_precio_barbijo = precio
            fabricante_max = fabricante
            cantidad_max = cantidad
            bandera_barbijo = True
    elif tipo == 'jabon':
        acumulador_soap +1
    
    if bandera == False or cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        fabricante_max_cantidad = fabricante
        bandera = True
if bandera_barbijo == False:
    print("No se cargaron barbijos.")
else:
    print(f"El más caro de los barbijos, la cantidad de unidades: {cantidad_max} y el fabricante: {fabricante_max}")

print(f"Del ítem con más unidades su fabricante es: {fabricante_max_cantidad}")
print(f"El total de jabones es: {acumulador_soap}")