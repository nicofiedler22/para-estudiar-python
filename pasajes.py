
pasajes = int(input("Ingresa la cantidad de pasajes que deseas vender: "))
for i in range (pasajes):
    try:
        total_ingresos = float(input(f"Ingresa el precio del pasaje número {i + 1}: $"))
    except ValueError as e:
        print("ERROR: Sólo puedes ingresar números en el precio del pasaje.")
        break

print(f"El valor total de ingresos es: ${total_ingresos}")