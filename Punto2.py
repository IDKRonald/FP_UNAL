#Importamos el modulo random para generar numeros pseudoaleatorios
import random

# Solicitar datos del pasajero
nombre = input("Ingrese el nombre del pasajero: ")
documento = int(input("Ingrese el documento del pasajero (solo números): "))

# Validación del documento
try:
    documento = int(documento)
except ValueError:
    print("El documento debe ser un número entero.")
    documento = input("Ingrese el documento del pasajero (solo números): ")
    
pais_origen = input("Ingrese su pais de origen: ").lower() 

# Asignación del vuelo y asiento
vuelo = random.randint(0, 9999)
asiento = "Primera Clase" if vuelo % 2 == 0 else "Clase Económica"

# Menú interactivo
opcion = 0
while opcion != 4:
    print("\n--- Bienvenido a Vallejo Airlines ---")
    print("1. Ver datos del pasajero")
    print("2. Ver vuelos asignados")
    print("3. Comprobar descuentos")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\n--- Datos del Pasajero ---")
        print(f"Nombre: {nombre}")
        print(f"Documento: {documento}")
        print(f"Nacionalidad: {pais_origen}")
        print(f"Vuelo asignado: {vuelo}")
        print(f"Asiento asignado: {asiento}")
    elif opcion == 2:
        print("\n--- Vuelos asignados ---")
        for i in range(1, 11):
            if i <= 5:
                print(f"{i}) Vuelo {random.randint(0, 9999)} llegando a Colombia")
            else:
                print(f"{i}) Vuelo {random.randint(0, 9999)} saliendo de Colombia")
    elif opcion == 3:
        print("\n--- Comprobación de Descuentos ---")
        if pais_origen == "colombia":
            print("Tiene un descuento del 10% disponible por ser colombiano.")
        else:
            print("No tiene descuentos disponibles.")
    elif opcion == 4:
        print("Gracias por usar Vallejo Airlines. ¡Hasta pronto!")
    else:
        print("Opción no válida. Intente de nuevo.")
