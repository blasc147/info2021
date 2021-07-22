from clases.agenda import Agenda
from clases.contacto import Contacto

agenda = Agenda()



nombre = input("ingresar nombre : ")

contacto1 = Contacto(nombre)

agenda.agregar_contacto(contacto1)

agenda.imprimir_lista()

