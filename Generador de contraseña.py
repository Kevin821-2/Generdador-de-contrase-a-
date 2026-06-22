"""usuarios = {}

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
        print("Opción incorrecta.")"""


import random
import string

def generar_contrasena(longitud, mayusculas=True, minusculas=True, numeros=True, simbolos=True):
    caracteres = ""

    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += "!@#$%^&*"

    if caracteres == "":
        return "Error: debes seleccionar al menos un tipo de carácter."

    contrasena = ""
    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


print("GENERADOR DE CONTRASEÑAS")

longitud = int(input("Ingrese la longitud de la contraseña: "))

usar_mayusculas = input("¿Incluir mayúsculas? (si/no): ") == "si"
usar_minusculas = input("¿Incluir minúsculas? (si/no): ") == "si"
usar_numeros = input("¿Incluir números? (si/no): ") == "si"
usar_simbolos = input("¿Incluir símbolos? (si/no): ") == "si"

contrasena = generar_contrasena(
    longitud,
    usar_mayusculas,
    usar_minusculas,
    usar_numeros,
    usar_simbolos
)

print("Contraseña generada:", contrasena)