
print("¡Bienvenido! Este programa, permite pagar y simular compras.")
deuda = 100000
cupo = 500000

while True:
    print("[1] - Pagar Tarjeta de Crédito")
    print("[2] - Simular un crédito")
    print("[3] - Salir")

    try:
        opc = int(input("Seleccione una de estás opciones: "))
        if opc > 3 or opc <= 0:
            print("Esa no es una opción válida.")
    except ValueError:
        print("ERROR. Sólo puedes ingresar números. [1, 2 o 3]")
        continue

    if opc == 1:
        print(f"Su deuda actual es de {deuda}")
        try:
            pago = int(input("Ingrese la cantidad a pagar:"))
        except ValueError:
            print("ERROR. Sólo puedes ingresar números. [1, 2 o 3]")
            continue
        if pago > deuda:
            print("No puede pagar más de lo que debe.")
        elif pago > cupo:
            print("El pago supera el saldo total de la tarjeta.")
        elif pago >= 0:
            deuda = deuda - pago
            print(f"La deuda actual corresponde a {deuda}")
        else:
            print("El monto ingresado es incorrecto.")
        continue

    if opc == 2:
        print(f"El cupo actual disponible es de {cupo}")
        try:
            cantidad = int(input("¿Cuántas compras desea realizar? "))
        except ValueError:
            print("ERROR. Sólo puedes ingresar números. [1, 2 o 3]")
            continue
        
        for i in range (cantidad):
                compra = int(input(f"Ingrese el valor de la compra número {i + 1}: $"))
                if compra > cupo:
                    print(f"El monto de la compra no puede superar tu cupo disponible.")
                    continue
                elif compra >= 0:
                    cupo = cupo - compra
                    print(f"Su nuevo cupo equivale a: {cupo}")
    if opc == 3:
        print("Saliendo... ¡Gracias por usar el programa!")
        break
    