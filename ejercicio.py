import math

print("Bienvenido al Programa qeu determina raiz cuarta de un numero real\n")

numero = float(input("Ingrese el numero real: "))

raizCuarta = math.sqrt(math.sqrt(numero))

print(f"la raiz cuarta de {numero} es: {raizCuarta}\n\n")


radio = float(input("ingrese el radio del circulo: "))
area = math.pi * radio ** 2
print(f"el area del circulo es: {area}\n\n")


print("Bienvenido al programa que determina el precio de venta de un aritculo con utilidad e impuestos.")

nombre = input("el nombre del producto es: ")
costoProd = float(input("El costo de produccion es: "))


impuestoPv = costoProd * 0.15
pV = (costoProd * 1.12) + impuestoPv

print(f"el producto {nombre} tiene un precio de venta de: {pV}")

