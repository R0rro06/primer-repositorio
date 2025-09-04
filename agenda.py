#Agenda
contacto = []

def agregar_contacto(nombre, telefono):
    contacto.append({"nombre" : nombre,"telefono" : telefono})

def listar_contactos():
    print("\nlista de contactos : ")
    for c in contacto:
        print(f"{c['nombre']} - [{c}'telefono']")

def buscar_contacto():
    for c in contacto:
        if c ['nombre'].lower() == nombre.lower():
            print(f"contacto encontrado {c['nombre']} - {c['telefono']}")
            return
        print("contacto no encontrado")


listar_contactos()

#nombre = input("Ingrese el nombre :" )
#telefono = input("Ingrese el telefono :")
#agregar_contacto(nombre, telefono)
#print("Contacto agregado")


nombre_buscar = input("nombre a buscar: ")
buscar_contacto(nombre_buscar)