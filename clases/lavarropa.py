from .electrodomestico import Electrodomestico

class Lavarropa(Electrodomestico):

	def __init__(self, color, precio, tipo_consumo, kgs):
		Electrodomestico.__init__(self, color, precio, tipo_consumo)
		self.kgs = kgs

	def calcular_precio(self):
		precio = 0

		precio = Electrodomestico.calcular_precio(self)

		if self.kgs>10:
			precio+= precio*0.1

		return precio