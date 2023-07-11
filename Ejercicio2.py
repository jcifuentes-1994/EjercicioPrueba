import funciones as fn

print("Bienvenidos")

personas = {}

menu = 0

while menu != 4:
    print("Seleccione una de las siguientes opciones: ")
    print("1.Grabar \n2.Buscar \n3.Imprimir certificados \n4.Salir")
    menu = int(input())

    if menu == 1:
        print("Grabar")
        while True:
            nif = fn.crearNif()
            if nif not in personas:
                print("El NIF nuevo es: ",nif)
                break

        nombre = fn.nombrePersona()
        edad = fn.edadPersona()
        fecNac = input("Ingrese su fecha de nacimiento: ")
        eCivil = input("Ingrese su estado Civil: ").upper()
        personas[nif] = nombre,edad,fecNac,eCivil

    elif menu == 2:
        print("Buscar")
        while True:
            nif = input("Ingrese su NIF: ")
            if personas[nif] == "":
                print("El NIF no existe")
                print("La persona no pertenece a la Unión Europea")
                break
            else:
                print("La persona pertenece a la Unión Europea")
                print("NIF: ",nif)
                print("Nombre: ",personas[nif][0])
                print("Edad: ",personas[nif][1])
                break
    
    elif menu == 3:
        print("Imprimir certificados")
        while True:
            nif = input("Ingrese su NIF: ")
            if personas[nif] == "":
                print("El NIF no existe")
                break
            else:
                print("Certificado de Nacimiento: ")
                print("NIF: ",nif)
                print("Nombre: ",personas[nif][0])
                print("Edad: ",personas[nif][1])
                print("Fecha de Nacimiento: ",personas[nif][2])
                print("")
                print("Certificado de Estado Conyugal: ")
                print("Estado Civil: ",personas[nif][3])
                print("")
                print("Certificado de pertenecencia a la UE")
                print("La persona pertenece a la Unión Europea")
                print("")
                break
    elif menu == 4:
        print("Muchas gracias por utilizar el programa")
        print("Creado por Julio Cifuentes")
        print("Versión 1.1")



