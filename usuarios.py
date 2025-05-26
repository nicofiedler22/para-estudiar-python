
usuario1 = None
usuario2 = None
usuario3 = None
contraseña1 = None
contraseña2 = None
contraseña3 = None

while True:
    print("1) Iniciar sesión")
    print("2) Registrar usuario")
    print("3) Salir")
    
    try:
        opc = int(input("¡Bienvenido! Escoja una de estás opciones: "))
        if opc <= 0 or opc > 3:
            print("Opción inválida.")
    except ValueError:
        print("ERROR: Sólo puedes ingresar números (1, 2 o 3).")
        continue

    if opc == 1:
        if usuario1 == None:
            print("Debes registrar un usuario antes.")
        else:
            while True:
                print("1) Realizar llamada")
                print("2) Enviar correo electrónico")
                print("3) Cerrar sesión")

                try:
                    opc2 = int(input("Selecciona una opción: "))
                except ValueError:
                    print("ERROR: Sólo puedes ingresar números (1, 2 o 3).")
                    continue

                if opc2 == 1:
                    print("Nota: El número telefónico debe empezar por 9 y debe tener 9 dígitos.")
                    llamada = int(input("Ingresa el número telefónico al que deseas llamar: "))

                    if llamada < 100000000:
                        print("Error: El número telefónico es menor a 9 dígitos.")
                    elif llamada > 999999999:
                        print("Error: El número telefónico es mayor a 9 dígitos.")
                    elif llamada < 900000000:
                        print("El número telefónico debe comenzar con 9.")
                    else:
                        print("¡Llamada realizada con éxito!")
                        continue

                if opc2 == 2:

                    correo_valido = False
                    while correo_valido == False:
                        correo = input("Ingresa el correo electrónico: ")

                        for arroba in correo:
                            if arroba == "@":
                                correo_valido = True
                            
                        if correo_valido == False:
                            print('Error: El correo debe contener un "@"')
                        else:
                            print(f'El correo "{correo}" fue guardado exitosamente.')
                    mensaje = input("Ingresa el mensaje a enviar: ")
                    print(f"Mensaje exitosamente enviado. Destinatario del mensae: {correo}")

                if opc2 == 3:
                    print("Cerrando sesión...")
                    break
    
    if opc == 2:
        print("¡Aquí crearás tu usuario! Puedes registrar un máximo de 3 usuarios.")
        registro = int(input("Ingresa la cantidad de usuarios que deseas registrar: "))

        if registro == 1:
            usuario1 = input("Crea un nombre de usuario: ")
            contraseña1 = input("Crea una contraseña: ")
            print("¡Usuario creado correctamente!")
        elif registro == 2:
            usuario1 = input("Crea un nombre de usuario: ")
            contraseña1 = input("Crea una contraseña: ")
            print("¡Usuario creado! Ahora, crea el segundo usuario:")
            usuario2 = input("Crea un nombre de usuario: ")
            contraseña2 = input("Crea una contraseña: ")
            print("¡Usuarios creados correctamente!")
        elif registro == 3:
            usuario1 = input("Crea un nombre de usuario: ")
            contraseña1 = input("Crea una contraseña: ")
            print("¡Usuario creado! Ahora, crea el segundo usuario:")
            usuario2 = input("Crea un nombre de usuario: ")
            contraseña2 = input("Crea una contraseña: ")
            print("¡Usuarios creados correctamente! Ahora, crea el tercer y último usuario:")
            usuario3 = input("Crea un nombre de usuario: ")
            contraseña3 = input("Crea una contraseña: ")
            print("¡Felicidades, has creado tres usuarios correctamente!")
        else:
            print("Error: Sólo puedes registrar 3 usuarios.")
            continue

    if opc == 3:
        print("¡Gracias por usar este programa!")
        break