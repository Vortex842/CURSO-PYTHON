while True:
            # Mostramos el menú principal
            print("--------- Tienda electronica ---------")
            print("1. Ver Telefonos")
            print("2. Ver Notebooks")
            print("3. Ver Televisores")
            print("4. Ver Auriculares")
            print("5. Salir del programa")

            # Pedimos la opción al usuario  
            opcion = int(input("Elige una opción (1-5): "))

            if opcion == 1:
                print("Telefonos disponibles:")
                print("- iPhone 13 Pro Max - $999")
                print("- Samsung Galaxy S21 - $799")
                print("- Xiaomi Redmi Note 10 Pro - $699")
                print("- Huawei Mate 30 Pro - $899")

            elif opcion == 2:
                print("Notebooks disponibles:")
                print("- MacBook Pro 16'' - $2399")
                print("- Dell XPS 13 - $1199")
                print("- HP Spectre x360 - $1299")
                print("- Lenovo ThinkPad X1 Carbon - $1499")
                
            elif opcion == 3:
                print("Televisores disponibles:")
                print("- LG OLED55CXPUA - $1499")
                print("- Samsung QN55QN90AAFXZA - $1299")
                print("- Sony XBR55A8H - $1799")
                print("- TCL 55R635 - $899")
            
            elif opcion == 4:
                print("Auriculares disponibles:")
                print("- Sony WH-1000XM4 - $349")
                print("- Bose QuietComfort 35 II - $299")
                print("- Apple AirPods Pro - $249")
                print("- Sennheiser Momentum 3 - $399")
            
            elif opcion == 5:
                print("Saliendo del programa...")
                break  # Rompemos el bucle para salir del programa

            else:
                print("Opción no válida. Por favor elige una opción del 1 al 5.")
                continue

            while True:
                volver = input("¿Deseas volver al menú principal? (s/n): ").lower()
                if volver == 's':
                    break  # Volvemos al menú principal
                elif volver == 'n':
                    print("Saliendo del programa...")
                    exit()  # Salimos del programa
                else:
                    print("Entrada no válida. Por favor ingresa 's' o 'n'.")