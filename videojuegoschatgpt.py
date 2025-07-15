
videojuegos = {}
stock = {}

def busca_juego_por_nombre(nombre_juego: str):
    for codigo, datos in videojuegos.items():
        if datos[0].lower() == nombre_juego.lower():
            return [codigo] + datos
    return None

def buscar_stock_por_juego(codigo_juego: str):
    return stock.get(codigo_juego)

def disminuir_stock(codigo_juego: str, cantidad: int):
    if codigo_juego in stock:
        if stock[codigo_juego][1] >= cantidad:
            stock[codigo_juego][1] -= cantidad
            print(f"¡Venta realizada! Quedan {stock[codigo_juego][1]} unidades.")
        else:
            print("No hay stock suficiente!")
    else:
        print("El código del juego no existe.")

def mostrar_todos_juegos():
    if not videojuegos:
        print("No hay juegos registrados.")
    for datos in videojuegos.values():
        print(f"NOMBRE: {datos[0]} || PLATAFORMA: {', '.join(datos[1])}")

def actualizar_precio_juego(nombre_juego: str, precio_nuevo: int):
    for codigo, datos in videojuegos.items():
        if datos[0].lower() == nombre_juego.lower():
            stock[codigo][0] = precio_nuevo
            print(f"Precio actualizado para {datos[0]}: {precio_nuevo} CLP")
            return
    print("El juego que desea actualizar no se encuentra.")

def buscar_juego_por_anio(rango_minimo: int, rango_maximo: int):
    encontrados = False
    for codigo, datos in videojuegos.items():
        if rango_minimo <= datos[5] <= rango_maximo:
            encontrados = True
            print(f"{codigo}: {datos}")
    if not encontrados:
        print("No se encontraron juegos en ese rango de años.")

while True:
    print("\n===== TIENDA DE VIDEOJUEGOS =====")
    print("1. Agregar nuevo videojuego")
    print("2. Vender juego (disminuir stock)")
    print("3. Mostrar todos los juegos")
    print("4. Actualizar precio de un juego")
    print("5. Filtrar juegos por año de lanzamiento")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Agregar Videojuego ---")
        codigo = input("Código único del juego: ").strip()
        if codigo in videojuegos:
            print("Ese código ya existe.")
            continue
        nombre = input("Nombre del juego: ").strip()
        plataformas = input("Plataformas (separadas por coma): ").strip().split(",")
        plataformas = [p.strip() for p in plataformas]
        genero = input("Género: ").strip()
        clasificacion = input("Clasificación ESRB (E, T, M): ").strip().upper()
        desarrollador = input("Desarrollador: ").strip()
        try:
            anio = int(input("Año de lanzamiento: ").strip())
        except ValueError:
            print("Año inválido.")
            continue
        publicador = input("Publicador: ").strip()

        try:
            precio = int(input("Precio en CLP: ").strip())
            cantidad = int(input("Cantidad en stock: ").strip())
        except ValueError:
            print("Precio o cantidad inválidos.")
            continue

        videojuegos[codigo] = [nombre, plataformas, genero, clasificacion, desarrollador, anio, publicador]
        stock[codigo] = [precio, cantidad]
        print("Juego agregado correctamente.")

    elif opcion == "2":
        print("\n--- Vender Juego ---")
        nombre = input("Ingrese el nombre del juego: ")
        datos_juego = busca_juego_por_nombre(nombre)
        if datos_juego:
            try:
                cantidad = int(input("¿Cuántas unidades desea vender?: "))
                disminuir_stock(datos_juego[0], cantidad)
            except ValueError:
                print("Cantidad inválida.")
        else:
            print("Juego no encontrado.")

    elif opcion == "3":
        print("\n--- Todos los Juegos ---")
        mostrar_todos_juegos()

    elif opcion == "4":
        print("\n--- Actualizar Precio ---")
        nombre = input("Ingrese el nombre del juego: ")
        try:
            nuevo_precio = int(input("Ingrese el nuevo precio (CLP): "))
            actualizar_precio_juego(nombre, nuevo_precio)
        except ValueError:
            print("Precio inválido.")

    elif opcion == "5":
        print("\n--- Filtrar por Año de Lanzamiento ---")
        try:
            anio_min = int(input("Año mínimo: "))
            anio_max = int(input("Año máximo: "))
            buscar_juego_por_anio(anio_min, anio_max)
        except ValueError:
            print("Debe ingresar años válidos.")

    elif opcion == "6":
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
