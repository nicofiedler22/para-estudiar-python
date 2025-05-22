
print("¡Bienvenido! Como registrador de la Liga de la Justicia, este programa te ayudará a registrar a los superhéroes.")

elite_cant = 0
novato_cant = 0

while True:
    try:
        sh_registros = int(input("Ingrese la cantidad de superhéroes que desea registrar: "))
        if sh_registros <= 0:
            print("¡Ese número no es correcto! La cantidad de superhéroes debe ser un número entero positivo.")
    except ValueError:
        print("ERROR: Sólo puedes ingresar números.")

    for i in range (sh_registros):
        try:
            name_sh = (input(f"({i + 1}) Nombre del superhéroe: "))
            años_exp = int(input(f"({i + 1}) Años de experiencia: "))
        except ValueError:
            print("ERROR: Los años de experiencia deben registrarse con números.")
            break
        if años_exp > 60:
            elite_cant = elite_cant + sh_registros
            print(f'El superhéroe llamado "{name_sh}" ha sido calificado como Élite.')
        else:
            novato_cant = novato_cant + sh_registros
            print(f'El superhéroe llamado "{name_sh}" ha sido calificado como Novato.')

    print(f"Cantidad de superhéroes élites: {elite_cant}")
    print(f"Cantidad de superhéroes novatos: {novato_cant}")
    