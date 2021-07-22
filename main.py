from clases.cliente import Cliente
from clases.vehiculo import Vehiculo
from clases.coche import Coche
from clases.bicicleta import Bicicleta

coche1 = Coche("Rojo", 4, 200, 6)
coche2 = Coche("Azul", 4, 180, 6)
bici1= Bicicleta("Azul", 2, "urbana")

def catalogar(lista, cant_ruedas):
	for item in lista:
		print(item.get_color())

vehiculos= []

vehiculos.append(coche1)
vehiculos.append(coche2)
vehiculos.append(bici1)



catalogar(vehiculos, 4)
#velocidad = coche1.get_color()

#print(velocidad)