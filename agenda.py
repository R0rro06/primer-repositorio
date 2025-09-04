#Agenda
contacto = []
opciones = 0

def agregar_contacto(nombre, telefono):
    contacto.append({"nombre" : nombre,"telefono" : telefono})

def listar_contactos():
    print("\nlista de contactos : ")
    for c in contacto:
        print(f"{c['nombre']} - [{c['telefono']}]")

def buscar_contacto(nombre):
    for c in contacto:
        if c['nombre'].lower() == nombre.lower():
            print(f"contacto encontrado {c['nombre']} - {c['telefono']}")
            return
    print("contacto no encontrado")

listar_contactos()

#nombre = input("Ingrese el nombre :" )
#telefono = input("Ingrese el telefono :")
#agregar_contacto(nombre, telefono)
#print("Contacto agregado")


#nombre_buscar = input("nombre a buscar: ")
#buscar_contacto(nombre_buscar)

while opciones != 4:
    print("-----MENU-----")
    print("1-Agregar contacto")
    print("2-Listar contacto")
    print("3-buscar contacto")
    print("4-Salir del programa")

    opciones = int(input("Escoja una de las opciones : "))

    if opciones == 1:
        nombre = input("Ingrese el nombre:")
        telefono = input("Ingrese el numero de telefono : ")
        agregar_contacto(nombre,telefono)

    elif opciones == 2:
        listar_contactos()

    elif opciones == 3:
        nombre_buscar = input("ingrese el nombre que desea buscar: ")
        buscar_contacto(nombre_buscar)

    elif opciones == 4:
        print("Hasta luego")
        break
    else:
        print("Ingrese una opcion valida")



