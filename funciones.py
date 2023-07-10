def nifPersona():
    while True:
        nif = input("Ingrese su NIF: ").upper()
        if len(nif) == 12:
            if nif[:8].isdigit():
                if nif[9:].isalnum():
                    print("NIF ingresado correctamente")
                    break
                else:
                    print("El NIF no corresponde")
            else:
                print("El NIF no corresponde")
        else:
            print("El NIF no corresponde")
    return nif

def nombrePersona():
    while True:
        nombre = input("Ingrese su nombre: ").upper()
        if len(nombre) < 8:
            print("El nombre debe ser mayor a 8 caracteres")
        else:
            print("Nombre registrado correctamente")
            break
    return nombre

def edadPersona():
    while True:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            print("La edad debe ser mayor a 0")
        else:
            print("Edad registrada correctamente")
            break
    return edad
