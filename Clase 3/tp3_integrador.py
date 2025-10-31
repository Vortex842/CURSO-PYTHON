# Hash de la contraseña muy segura
import getpass as gp
import hashlib as hash


hash_hex = "e3cdaca6fff993376fd99b3606c400d25ed3bb7ef39461f575fefc39ef016fb6"

maxAttemps = 3    # Maximo de intentos permitidos
countAttemps = 0  # Contador de intentos de contraseñas fallidas

res = 0           # Resultado de la operacion
opValid = True    # Resulta util si la operacion no fue valida, por ejemplo en la division, para no imprimir el resultado

while True:
    if(countAttemps == 0):
        # Dejamos que el usuario elija si quiere ingresar o salir, asi poder cerrar el programa
        #  sin necesidad de parar el programa desde afuera
        print("\n=== Iniciando sesión ===")
        print("1. Ingresar al sistema")
        print("2. Salir")

        option = int(input("Elige una opción (1-2): "))
        if option == 1:
            print("Ingresando al sistema...\n\n")

        elif option == 2:
            print("Saliendo del programa...\n\n")
            break

        else:
            print("Opción no válida. Por favor elige una opción del 1 al 2.")
            continue



    passwordInput = gp.getpass('Ingrese la contraseña: ')

    passwordInput_hash = hash.sha256(passwordInput.encode()).hexdigest()

    if passwordInput_hash == hash_hex:
        print('Bienvenido al sistema')

        while True:
            # Mostramos el menú principal
            print("\n=== Menú de Operaciones Matemáticas ===")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")

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
        countAttemps += 1

        if countAttemps > maxAttemps:
            print("Ha excedido el número máximo de intentos. Saliendo del programa...")
            countAttemps = 0
            break

        print(f"Contraseña incorrecta ({maxAttemps - countAttemps - 1} intentos restantes). Acceso denegado. Hagalo denuevo")