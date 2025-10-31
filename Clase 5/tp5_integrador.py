# Hash de la contraseña muy segura
import getpass as gp
import hashlib as hash


hash_hex = "e3cdaca6fff993376fd99b3606c400d25ed3bb7ef39461f575fefc39ef016fb6"

res = 0           # Resultado de la operacion
opValid = True    # Resulta util si la operacion no fue valida, por ejemplo en la division, para no imprimir el resultado

opciones = [
            "Mostrar la hora actual",
            "Generar contraseña segura",
            "Calcular valor cuadratico medio",
            "Ahorcado",
            "Salir del programa",
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

        if hashPassword(passwordInput) == hash_hex:
            return True
        
        else:
            print(f"Contraseña incorrecta ({maxAttemps - countAttemps - 1} intentos restantes). Hagalo denuevo")
            countAttemps += 1

    return False


def printMenu():
    """Imprime el menú de operaciones matemáticas."""
    print("\n=== Menú de Operaciones Matemáticas ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


#--- Programa principal ---
print("=== Iniciando sesión ===")
if validatePassword():
    print('Bienvenido al sistema')

    while True:
        # Mostramos el menú principal
        printMenu()

        # Pedimos la opción al usuario
        opcion = int(input("Elige una opción (1-5): "))
        if 1 <= opcion and opcion <= 5:
            if opcion == 1:
                print("Has elegido la opción de Sumar")

            elif opcion == 2:
                print("Has elegido la opción de Restar")

            elif opcion == 3:
                print("Has elegido la opción de Multiplicar")

            elif opcion == 4:
                print("Has elegido la opción de Dividir")

            if opcion < 5:
                print("\n\nAhora vamos con los operandos:")
                a = float(input("a: "))
                b = float(input("b: "))

            else:
                print("Saliendo del programa...")
                break  # Rompemos el bucle para salir del programa

        else:
            print("Opción no válida. Por favor elige una opción del 1 al 5.")
            continue

        # Decisiones según la opción elegida
        if opcion == 1:
                res = a + b

        elif opcion == 2:
            res = a - b

        elif opcion == 3:
            res = a * b

        elif opcion == 4:
            if b != 0:
                res = a / b
            else:
                opValid = False
                print("Error: No se puede dividir por cero.")

        if opValid:
            print("El resultado de la operacion es", res)

        opValid = True
else:
    print("Ha excedido el número máximo de intentos. Saliendo del programa...")

    