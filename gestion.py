
datos = {
    "estudiantes":
    [


    ]
}

def registro():
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = int(input("Ingresa la edad del estudiante: "))
    genero = input("Ingresa el género del estudiante [Femenino(F) o Masculino(M)]: ")
    codigo = int(input("Ingresa el código del estudiante: "))
    promedio = float(input("Ingresa el promedio del estudiante: "))

    agregar_estudiante = {

        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "codigo": codigo,
        "promedio": promedio
    }
    datos["estudiantes"].append(agregar_estudiante)
    print("Estudiante ingresado correctamente.")

while True:
    print("1 - Registrar estudiante")
    print("2 - Buscar estudiante")
    print("3 - Modificar datos de estudiante")
    print("4 - Eliminar estudiante")
    print("5 - Mostrar todos los estudiantes")
    print("6 - Salir")

    opc = int(input("Selecciona una opción: "))

    if opc == 1:
        registro()

    elif opc == 2:
        for i in datos["estudiantes"]:
            print(f"Nombre: {i["nombre"]} Edad: {i["edad"]}")