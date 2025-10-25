contra = "-O_O-"  # Contraseña muy segura
res = 0           # Resultado de la operacion
opValid = True    # Resulta util si la operacion no fue valida, por ejemplo en la division, para no imprimir el resultado

while True:
    ingresar_contra = input('Ingrese la contraseña: ')
    if ingresar_contra == str(contra):
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
            if 1 <= opcion and opcion < 5:
                print("Ahora vamos con los operandos:\n")
                a = float(input("a: "))
                b = float(input("b: "))
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

            elif opcion == 5:
                print("Saliendo del programa...")
                break  # Rompemos el bucle para salir del programa

            if opValid:
                print("El resultado de la operacion es", res)

            opValid = True
    else:
        print("Contraseña incorrecta. Acceso denegado. Hagalo denuevo")

