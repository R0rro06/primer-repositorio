#Agenda
contacto = []

def agregar_contacto(nombre, telefono)
    contacto.append({"nombre" : nombre,"telefono" : telefono})

def listar_contactos()
    print("\nlista de contactos : ")
    for c in contacto:
        print(f"{c['nombre']} - [{c}'telefono']")

listar_contactos()
nombre = input("Ingrese el nombre :" )
telefono = input("Ingrese el telefono :")
agregar_contacto(nombre, telefono)
print("Contacto agregado")