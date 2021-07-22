

class Agenda():

	def __init__(self):
		self.contactos = []

	
	def agregar_contacto(self, un_contacto):
		self.contactos.append(un_contacto)
		return

	def imprimir_lista(self):
		for item in self.contactos:
			print(item.nombre)

	"""implementar el metodo para buscar un contacto"""
	def buscar_contacto(self, nombre):
		pass
		#return un_contacto


	def editar_contacto(self, nombre_busqueda, nombre_modificar):
		contacto = self.buscar_contacto(nombre_busqueda)
		contacto.nombre = nombre_modificar