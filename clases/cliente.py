
class Cliente:

	def __init__(self, unNombre, laRaza,casado, elDni):
		self.nombre = unNombre
		self.apellido = laRaza
		self.casado = casado
		self.dni = elDni
		self.saldo = 0

	def depositar(self, monto):
		self.saldo+= monto

	def retirar(self, monto):
		self.saldo-=monto

	def imprimir(self):
		print("Nombre :", self.nombre)
		print("Saldo :", self.saldo)

	def __str__(self):
		return self.nombre


class ClienteEspecial(Cliente):
	def __init__(self, unNombre, laRaza,casado, elDni, descuento):
		Cliente.__init__(self, unNombre, laRaza,casado, elDni)
		self.descuento = descuento


