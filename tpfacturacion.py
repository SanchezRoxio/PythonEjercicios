#A. Ingresar tres precios de productos y mostrar la suma de los mismos.
pre1 = int(input("Ingrese el primer precio del producto: "))
pre2 = int(input("Ingrese el segundo precio: "))
pre3 = int(input("ingrese el tercer precio: "))
sum1 = (pre1 + pre2 + pre3)

print("La suma de los tres precios es de: " , sum1)

#B. Ingresar tres precios de productos y mostrar el promedio de los mismos.
pre1 = int(input("Ingrese el primer precio del producto: "))
pre2 = int(input("Ingrese el segundo precio: "))
pre3 = int(input("ingrese el tercer precio: "))
prom1 = ((pre1 + pre2 + pre3)/3)

print("El promedio de los mismos es de: " , prom1)

#C. Ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
pre1 = int(input("Ingrese el primer precio del producto: "))
pre2 = int(input("Ingrese el segundo precio: "))
pre3 = int(input("ingrese el tercer precio: "))
sum1 = (pre1 + pre2 + pre3)
pfinal = (((pre1 + pre2 + pre3)*21)/100)
sum2 = pfinal + sum1 
print("El precio es de: " , sum1 , "+ el 21% IVA de= " , pfinal)
print("El precio final es de: " , sum2)