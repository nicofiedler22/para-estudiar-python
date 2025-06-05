
datos = {
    "estudiantes":
    [
        

    ]
}

while True:
    print("1 - Crear estudiante")
    print("2 - Listar estudiantes")
    print("3 - Actualizar estudiantes")
    print("4 - Eliminar estudiantes")
    print("5 - Salir")

    opc = int(input("Ingresa una opción: "))

    if opc == 1:
        id = int(input("Ingresa una ID: "))
        nombre = (input("Ingresa tu nombre: "))
        apellido = (input("Ingresa tu apellido: "))
        edad = int(input("Ingresa tu edad: "))
        carrera = input("Ingresa tu carrera: ")

        agregar_est = {
            "id": id,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "carrera": carrera
        }

        datos["estudiantes"].append(agregar_est)
        print("¡Estudiante creado satisfactoriamente!")

    elif opc == 2:
        for i in datos["estudiantes"]:
            print(f"ID: {i["id"]}")
            print(f"nombre: {i["nombre"]}")
            print(f"apellido: {i["apellido"]}")
            print(f"edad: {i["edad"]}")
            print(f"carrera: {i["carrera"]}")

    elif opc == 3:
        id = int(input("Ingresa el ID del estudiante: "))
        for i in datos["estudiantes"]:
            if i["id"] == id:
                nombre = input("Ingresa el nuevo nombre: ")
                apellido = (input("Ingresa el nuevo apellido: "))
                edad = int(input("Ingresa la nueva edad: "))
                carrera = input("Ingresa la nueva carrera: ")
                i["nombre"] = nombre
                i["apellido"] = apellido
                i["edad"] = edad
                i["carrera"] = carrera
                print("¡Estudiante actualizado satisfactoriamente!")

    elif opc == 4:
        id = int(input("Ingresa el ID del estudiante que se borrará: "))
        for i in datos["estudiantes"]:
            if i["id"] == id:
                datos["estudiantes"].remove(i)
                print("Estudiante eliminado.")

    elif opc == 5:
        print("Saliendo... ¡Gracias por usar este programa!")
        break

    else:
        print("Opción no válida.")
        continue
