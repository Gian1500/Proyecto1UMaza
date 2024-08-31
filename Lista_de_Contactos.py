import os
import re

contactos = []

def validar_email(email):
    expresion_regular = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(expresion_regular,email) is not None # re.MATCH devuelve un objeto de tipo MATCH que muestra la coincidencias encontradas dentro de la cadena, caso contrario NONE

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    
    validacion = False
    while not validacion:
        email = input("Ingrese el correo electrónico: ")
        validacion = validar_email(email)
        if not validacion:
            print("El correo electrónico ingresado no tiene formato correcto.")
            print("-" * 30)

    for contacto in contactos:
        if contacto['nombre'].lower() == nombre.lower():
            print("Un contacto con ese nombre ya existe.")
            print("¿Desea agregarlo igualmente?")
            
            while True:
                try:
                    opc = int(input("1- SI        2- NO: "))
                    if opc == 1:
                        nuevo_contacto = {
                            'nombre': nombre,
                            'telefono': telefono,
                            'email': email
                        }
                        contactos.append(nuevo_contacto)
                        print(f"Contacto {nombre} agregado exitosamente.")
                        return
                    elif opc == 2:
                        print("Contacto NO añadido.")
                        return
                    else:
                        print("Por favor, elija una opción válida: 1 para Sí, 2 para No.")
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese 1 para Sí o 2 para No.")

    nuevo_contacto = {
        'nombre': nombre,
        'telefono': telefono,
        'email': email
    }
    contactos.append(nuevo_contacto)
    print(f"Contacto {nombre} agregado exitosamente.")

def ver_contacto():

    if len(contactos) == 0:
        print("No tiene contactos agregados")
        return
    else:
        contador = 0
        for i in contactos:
            print(f"CONTACTO {contador} => Nombre: {i['nombre']} // Teléfono: {i['telefono']} // Email: {i['email']}")
            print("-" * 30)
            contador += 1

def buscar_contacto():
    
    busqueda = input("Ingrese el nombre del contacto: ")
    encontrado = False
    contador = 0
    for i in contactos:
        contador += 1
        if i['nombre'] == busqueda:
            print(f"CONTACTO ENCONTRADO => Posicion:{contador} // Nombre: {i['nombre']} // Teléfono: {i['telefono']} // Email: {i['email']}")
            encontrado = True
            break
    if not encontrado:
            print(f"CONTACTO `{busqueda}` NO ENCONTRADO ")

def eliminar_contacto():

    eliminar = input("Ingrese el nombre del contacto a eiiminar: ")
    encontrado = False
    contador = 0
    for i in contactos:
        contador += 1
        if i['nombre'] == eliminar:
            print(f"CONTACTO Eliminado => Posicion:{contador} // Nombre: {i['nombre']} // Teléfono: {i['telefono']} // Email: {i['email']}")
            contactos.remove(i)
            encontrado = True
            break
    if not encontrado:
            print(f"CONTACTO `{eliminar}` NO ENCONTRADO ")

def guardar_contactos():
    try:
        with open('contactos.txt', 'w', encoding='utf-8') as archivo:
            if len(contactos) == 0:
                archivo.write("No tiene contactos agregados\n")
            else:
                for contador, contacto in enumerate(contactos, start=1):
                    archivo.write("-" * 60 + "\n")
                    archivo.write(f"CONTACTO Nro.{contador}\n")
                    archivo.write(f"Nombre: {contacto['nombre']}\n")
                    archivo.write(f"Teléfono: {contacto['telefono']}\n")
                    archivo.write(f"Email: {contacto['email']}\n")
                    archivo.write("-" * 60 + "\n")
        return True
    except IOError as error:
        print(f"No fue posible crear el archivo. Error: {error}")
        return False
    
def cargar_contactos():
    try:
        with open('contactos.txt', 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            contactos.clear()  
            
            contacto = {}
            for linea in lineas:
                linea = linea.strip() 
                
                if linea.startswith('CONTACTO Nro.'):
                    if contacto:
                        contactos.append(contacto)  
                    contacto = {} 
                elif linea.startswith('Nombre:'):
                    contacto['nombre'] = linea[len('Nombre: '):]
                elif linea.startswith('Teléfono:'):
                    contacto['telefono'] = linea[len('Teléfono: '):]
                elif linea.startswith('Email:'):
                    contacto['email'] = linea[len('Email: '):]
                
            if contacto:
                contactos.append(contacto)  
        return True
    except FileNotFoundError:
        print("El archivo 'contactos.txt' no se encontró.")
        return False
    except IOError as e:
        print(f"No fue posible leer el archivo. Error: {e}")
        return False

while True:
    
    print("============ LISTA DE CONTACTOS ==============")
    print("1. Agregar")
    print("2. Ver")
    print("3. Buscar")
    print("4. Eliminar")
    print("5. Guardar en Fichero")
    print("6. Cargar desde Fichero")
    print("0. Salir")
    
    
    try:
        opcion = int(input("Elija una opcion: "))
        if opcion < 0 or opcion > 6:
            os.system("cls")
            print("*" * 30)
            print("Elija una opcion valida.")
            print("*" * 30)
            opcion = -1

    except ValueError:
        os.system("cls")
        print("*" * 30)
        print("Elija numeros y no letras.")
        print("*" * 30)
        opcion = -1
    
    cambios_guardados = False
    match opcion:
        case 1:
            os.system("cls")
            print("====== Agregar ======")
            agregar_contacto()

        case 2:
            os.system("cls")
            print("====== Ver ======")
            ver_contacto()
            
        case 3:
            os.system("cls")
            print("======  Buscar ====== ")
            buscar_contacto()

        case 4:
            os.system("cls")
            print("======  Eliminar ====== ")
            eliminar_contacto()

        case 5:
            os.system("cls")
            print("======  Guardar ====== ")
            if guardar_contactos():
                print("Contactos Guardados Satisfactoriamente")
                cambios_guardados = True
            else:
                print("Error al Guardar los Contactos")

        case 6:
            os.system("cls")
            print("======  Cargar ====== ")
            if cargar_contactos():
                print("Contactos Guardados Satisfactoriamente")
            else:
                print("Error al Guardar los Contactos")
        
        case 0:
            os.system("cls")
            if cambios_guardados == False:
                print("Autoguardado Activado ")
                guardar_contactos()
            print("================")
            print("||  Saliendo  ||")
            print("================")
            break

