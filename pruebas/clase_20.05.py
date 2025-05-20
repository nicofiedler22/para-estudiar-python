
while True:
    try:
        num1 = int(input("Ingrese el primer dígito:"))
        num2 = int(input("Ingrese el segundo dígito:"))
        break
    except ValueError:
        print("Error")
        continue

while True:
        print("MENÚ")
        print("[1] - Sumar")
        print("[2] - Restar")
        print("[3] - Multiplicar")
        print("[4] - Salir")

        try:
            opc = int(input("Ingrese una opción:"))
        except ValueError:
            print("Sólo se permiten números enteros.")
            continue

        if opc == 1:
            print("El resultado de la suma es: ", num1 + num2)
        elif opc == 2:
            print("El resultado de la resta es: ", num1 - num2)
        elif opc == 3:
            print("El resultado de la multiplicacion es: ", num1 * num2)
        elif opc == 4:
            print("Saliendo...")
            break
        else:
            print("La opción no es correcta o no existe.")
