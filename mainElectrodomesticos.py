from clases.electrodomestico import Electrodomestico
from clases.lavarropa import Lavarropa


electrodomestico1 = Electrodomestico("Blanco", 1000, "B")
lavarropas1 = Lavarropa("Plata", 30000, "C", 20)

lista = []

lista.append(electrodomestico1)
lista.append(lavarropas1)

for item in lista:
	print("El precio es de : ",item.calcular_precio())
