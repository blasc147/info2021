class Electrodomestico():

	def __init__(self, color, precio, tipo_consumo):
		self.color = color
		self.precio_base = precio
		self.tipo_consumo = tipo_consumo


	def calcular_precio(self):
		precio = 0

		if self.tipo_consumo=="A":
			precio = self.precio_base*1.1
		else:
			precio = self.precio_base*1.2

		return precio
	


