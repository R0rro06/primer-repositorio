#Agenda
contacto = []

def agregar_contacto(nombre, telefono)
    contacto.append({"nombre" : nombre,"telefono" : telefono})

nombre = input("Ingrese el nombre :" )
telefono = input("Ingrese el telefono :")
agregar_contacto(nombre, telefono)
print("Contacto agregado")