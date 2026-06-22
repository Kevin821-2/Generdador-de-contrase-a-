usuarios = {}

def crear_cuenta():
    print("\nCREAR CUENTA")
    usuario = input("Crea tu usuario: ")
    contraseña = input("Crea tu contraseña: ")

    if usuario in usuarios:
        print("Ese usuario ya existe.")
    else:
        usuarios[usuario] = contraseña
        print("Cuenta creada correctamente.")

def iniciar_sesion():
    print("\nINICIAR SESIÓN")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso.")
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False

while True:
    print("\nGENERADOR DE CONTRASEÑAS")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        if iniciar_sesion():
            print("Bienvenido al sistema.")
            break
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción incorrecta.")