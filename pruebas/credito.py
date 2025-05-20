

print("¡Bienvenido! Este programa, permite pagar y simular créditos.")
deuda = 100000
cupo = 500000

while True:
    print("[1] - Pagar Tarjeta de Crédito")
    print("[2] - Simular un crédito")
    print("[3] - Salir")

    try:
        opc = int(input("A continuación, seleccione una opción:"))
    except ValueError:
        print("ERROR. Sólo puedes ingresar números.")

    if opc == 1:
        print(f"Su deuda actual es de {deuda}")
        pago = int(input("Ingrese la cantidad a pagar:"))
        deuda = deuda - pago
        if pago > deuda:
            print("No puede pagar más de lo que debe.")
            break
        elif pago >= 0:
            print(f"La deuda actual corresponde a {deuda}")
        else:
            print("El monto ingresado es incorrecto.")
        continue
