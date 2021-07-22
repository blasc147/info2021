from .vehiculo import Vehiculo

class Coche(Vehiculo):
	def __init__(self, unColor, ruedas, velocidad, cilindrada):
		Vehiculo.__init__(self, unColor, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def get_color(self):
		return "esto es un coche de color",self.color

	def get_velocidad(self):
		return self.velocidad

	def __str__(self):
		return self.color


