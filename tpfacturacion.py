#A. Ingresar tres precios de productos y mostrar la suma de los mismos.
#B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
#C. Ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).

pre1 = int(input("Ingrese el primer precio del producto: "))
pre2 = int(input("Ingrese el segundo precio: "))
pre3 = int(input("ingrese el tercer precio: "))

sum1 = (pre1 + pre2 + pre3)
prom1 = ((pre1 + pre2 + pre3)/3)
pfinal = (((pre1 + pre2 + pre3)*21)/100)

print("La suma de los tres precios es: " , sum1)

print("El promedio de los mismos es: " , prom1)

print("El precio final es de: " , sum1 , "y con el 21% IVA= " , pfinal)