# Hash de la contraseña muy segura
import getpass as gp
import hashlib as hash
import math
import time
import random


passHash = "e3cdaca6fff993376fd99b3606c400d25ed3bb7ef39461f575fefc39ef016fb6"


def showCurrentTime():
    """Muestra la hora actual"""
    # Te devuelve la hora actual en formato HH:MM:SS (24 horas en localtime)
    current_time = time.strftime("%H:%M:%S")
    print(f"La hora actual es: {current_time}\n\n")

def generateSecurePassword():
    """Genera una contraseña segura"""
    # Usando la libreria random para generar una contraseña segura
    txt = input("Ingrese el texto base para generar la contraseña segura: ")
    txtGen = ""

    for i in range(len(txt)):  # Rango igual a la longitud del texto base
        caracter = random.choice(txt)   # Selecciona un caracter aleatorio del texto base
        
        # Reemplaza el caracter en la posición i con el caracter aleatorio seleccionado
        txtGen += caracter

    print("Contraseña segura generada:", txtGen, "\nHash:", hashPassword(txtGen), "\n\n")


def rootsEquation():
    """Calcula las raíces de una ecuación cuadrática"""
    print("Calculando raíces de la ecuación cuadrática...")

    # Pedimos los coeficientes de la ecuación
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))

    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        # Dos raíces reales y diferentes
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"x1 = {raiz1} y x2 = {raiz2}")

    elif discriminante == 0:
        # Una raíz real doble
        raiz = -b / (2*a)
        print(f"x1,2 = {raiz}")

    else:
        # No hay raíces reales
        print("No hay raíces reales.")

def mostrarAhorcado(intentos):
    dibujos = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]
      # Evita error si intentos > 6, es decir que retornara el dibujo final cuando se pierda
    return dibujos[min(intentos, 6)]

def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""

    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "_"

    return resultado


def pedir_letra(letras_usadas):
    while True:
        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, escribe una única letra.")

        elif letra in letras_usadas:
            print("Ya la usaste. Probá otra.")

        else:
            return letra

def ahorcado():
    """Inicia el juego del ahorcado"""
    print("Iniciando juego del ahorcado...")
    palabras = ["python", "programacion", "curso", "seguridad"]

    palabraOculta = random.choice(palabras)

    intentos = 0
    letrasAdivinadas = []
    while True:
        print(mostrarAhorcado(intentos))
        
        print(f"Palabra oculta ({len(palabraOculta)} letras): ", mostrar_palabra(palabraOculta, letrasAdivinadas))

        # El usuario intenta con una letra
        letra = pedir_letra(letrasAdivinadas)
        letrasAdivinadas.append(letra)

        # Verificamos si ya todas las letras fueron adivinadas
        # Lo que hace es iterar con el for por cada letra de "palabraOculta"
        # Usa esa letra para verificar si está en "letrasAdivinadas"
        # Si todas dan true, significa que se adivinaron todas las letras
        if(all(letra in letrasAdivinadas for letra in palabraOculta)):
            print("¡Felicidades! ¡Adivinaste la palabra:", palabraOculta, "!")
            break

        if not letra in palabraOculta: # La letra no está en la palabra oculta
            intentos += 1
            print("Letra incorrecta.")


        if intentos >= 6:
            print("¡Perdiste! La palabra era:", palabraOculta)
            break

        # Mostrar letras usadas separadas por comas y la palabra oculta con guiones bajos
        # para ocultar las letras no adivinadas
        print("Letras usadas:", ", ".join(letrasAdivinadas))
        print("Palabra oculta:", mostrar_palabra(palabraOculta, letrasAdivinadas))
        
        # El usuario puede intentar adivinar la palabra completa
        palabra = input("Ya sabes la palabra? (deja en blanco si no la sabes): ").lower()

        if palabra.strip() != "":
            if palabra == palabraOculta:
                print("¡Felicidades! ¡Adivinaste la palabra:", palabraOculta, "!")
                break

            else:
                intentos += 1
                print("Palabra incorrecta.")

def exitProgram():
    """Sale del programa"""
    print("Saliendo del programa...\n\n")
    exit(0)


menuPrincipal = [
            ["Mostrar la hora actual", showCurrentTime],
            ["Generar contraseña segura", generateSecurePassword],
            ["Calcular raíces de una ecuación cuadrática", rootsEquation],
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
            countAttemps += 1

            if(countAttemps == maxAttemps):
              return False
              
            print(f"Contraseña incorrecta ({maxAttemps - countAttemps} intentos restantes). Hagalo denuevo")
            

    return False


def printMenu():
    """Imprime el menú"""
    print("\n=== Menú Principal ===")
    for i, opcion in enumerate(menuPrincipal, 1):
        print(f"({i}) {opcion[0]}")

def validateOptionInput(opcion: str) -> bool:
    """Verifica que la opción ingresada sea válida."""

    if not opcion.isdigit():
        print("Opción no válida. Por favor ingresa un número.")
        return False

    opcion = int(opcion)
    if opcion < 1 or opcion > len(menuPrincipal):
        print("Opción no válida. Por favor elige una opción del 1 al 5.")
        return False

    return True


#--- Programa principal ---
print("=== Iniciando sesión ===")
if validatePassword():
    print('Bienvenido al sistema')

    while True:
        # Mostramos el menú principal
        printMenu()

        # Pedimos la opción al usuario y verificamos que sea válida
        opcion = input(f"Elige una opción (1-{len(menuPrincipal)}): ")
        if not validateOptionInput(opcion):
            continue

        # Decisiones según la opción elegida
        opcion = int(opcion)
        menuPrincipal[opcion - 1][1]()  # Llamamos a la función correspondiente

else:
    print("Ha excedido el número máximo de intentos. Saliendo del programa...")