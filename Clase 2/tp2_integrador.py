contra = 123
ingresar_contra = input('Ingrese la contraseña: ')

if ingresar_contra == str(contra):
    print('Bienvenido')

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

        # Decisiones según la opción elegida
        if opcion == 1:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print("La suma de", num1, "y", num2, "es:", num1 + num2)

        elif opcion == 2:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print("La resta de", num1, "menos", num2, "es:", num1 - num2)

        elif opcion == 3:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print("La multiplicación de", num1, "por", num2, "es:", num1 * num2)

        elif opcion == 4:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            if num2 != 0:
                print("La división de", num1, "entre", num2, "es:", num1 / num2)
            else:
                print("Error: No se puede dividir por cero.")

        elif opcion == 5:
            print("Saliendo del programa...")
            break  # Rompemos el bucle para salir del programa

        else:
            print("Opción no válida. Por favor elige una opción del 1 al 5.")
else:
    print("Contraseña incorrecta. Acceso denegado.")

