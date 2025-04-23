
peso = float(input("Ingrese su peso (kg):"))
altura = float(input("Ingrese su altura (mts):"))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Estás bajo peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Estás en peso normal.")
elif imc >= 25 and imc < 29.9:
    print("Estás en sobrepeso.")
else:
    print("Obesidad.")
