def agregar_pelicula(titulo,anio,genero,vista):
    """Agrega los datos de la película al programa."""
    datos_agregar = {
        "título": titulo,
        "año": anio,
        "género": genero,
        "vista": vista
    }
    datos["peliculas"].append(datos_agregar)
    print("¡Datos agregados exitosamente!")
    return datos_agregar

datos = {
    "peliculas":[
        {
            "título": str,
            "año": int,
            "género": str,
            "vista": bool
        }
    ]
}

while True:
    print("1 - Agregar película")
    print("2 - Mostrar todas las peliculas")
    print("3 - Buscar película por título")
    print("4 - Eliminar una película")
    print("5 - Salir del programa")
    opc = int(input("Seleccione una opción: "))

    if opc == 1:
        titulo = input("Ingresa el título de la película: ")
        año = int(input("Ingresa el año de lanzamiento de la película: "))
        genero = input("Ingresa el género de la película: ")
        vista = input("¿La has visto? (si/no): ").strip().lower()
        print(agregar_pelicula(titulo,año,genero,vista))
