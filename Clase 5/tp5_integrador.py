# Hash de la contraseña muy segura
import getpass as gp
import hashlib as hash
import time


passHash = "e3cdaca6fff993376fd99b3606c400d25ed3bb7ef39461f575fefc39ef016fb6"


def showCurrentTime():
    """Muestra la hora actual"""
    # Te devuelve la hora actual en formato HH:MM:SS (24 horas en localtime)
    current_time = time.strftime("%H:%M:%S")
    print(f"La hora actual es: {current_time}\n\n")

def generateSecurePassword():
    """Genera una contraseña segura"""
    print("Contraseña segura generada: ...")

def RMSValue():
    """Calcula el valor cuadrático medio"""
    print("Calculando valor cuadrático medio...")

def ahorcado():
    """Inicia el juego del ahorcado"""
    print("Iniciando juego del ahorcado...")

def exitProgram():
    """Sale del programa"""
    print("Saliendo del programa...\n\n")
    exit(0)


menuPrincipal = [
            ["Mostrar la hora actual", showCurrentTime],
            ["Generar contraseña segura", generateSecurePassword],
            ["Calcular valor cuadratico medio", RMSValue],
            ["Ahorcado", ahorcado],
            ["Salir del programa", exitProgram],
           ]



def hashPassword(password: str) -> str:
    """Devuelve el hash SHA-256 de la contraseña dada."""
    return hash.sha256(password.encode()).hexdigest()

def validatePassword() -> bool:
    """Valida la contraseña ingresada comparándola con el hash almacenado."""
    
    maxAttemps = 3    # Maximo de intentos permitidos
    countAttemps = 0  # Contador de intentos de contraseñas fallidas

    while countAttemps < maxAttemps:
        passwordInput = gp.getpass('Ingrese la contraseña: ')

        if hashPassword(passwordInput) == passHash:
            return True
        
        else:
            print(f"Contraseña incorrecta ({maxAttemps - countAttemps - 1} intentos restantes). Hagalo denuevo")
            countAttemps += 1

    return False


def printMenu():
    """Imprime el menú"""
    print("\n=== Menú Principal ===")
    for i, opcion in enumerate(menuPrincipal, 1):
        print(f"({i}) {opcion[0]}")



#--- Programa principal ---
print("=== Iniciando sesión ===")
if validatePassword():
    print('Bienvenido al sistema')

    while True:
        # Mostramos el menú principal
        printMenu()

        # Pedimos la opción al usuario y verificamos que sea válida
        opcion = int(input(f"Elige una opción (1-{len(menuPrincipal)}): "))
        if opcion < 1 or opcion > len(menuPrincipal):
            print("Opción no válida. Por favor elige una opción del 1 al 5.")
            continue


        # Decisiones según la opción elegida
        menuPrincipal[opcion - 1][1]()  # Llamamos a la función correspondiente

else:
    print("Ha excedido el número máximo de intentos. Saliendo del programa...")

    