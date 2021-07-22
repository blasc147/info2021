from .vehiculo import Vehiculo

class Bicicleta(Vehiculo):

	def __init__(self, unColor, ruedas, unTipo):
		Vehiculo.__init__(self, unColor, ruedas)
		self.tipo = unTipo

	def get_color(self):
		return "esta es una bici de color", self.color