menu = """Restaurante el gustoso
    1. Hamburguesa      -> $15000
    2. Pizza            -> $10000
    3. Ensalada         -> $5000
    4. Salchipapa       -> $13000
    5. Perro caliente   -> $13000
    6. Salir
    """
print(menu)
opcion = 0
total_hamburguesa = 0
total_pizza = 0
total_ensalada = 0
total_salchipapa = 0
total_perroCaliente = 0
cant_hamburguesa = 0
cant_pizza = 0
cant_ensalada = 0
cant_salchipapa = 0
cant_perroCaliente = 0
total = 0
while opcion != 6:
    opcion = int(input("Ingrese una opción del menú: "))
    if opcion == 1:
        cant_hamburguesa += 1
        total_hamburguesa += 15000
        print("Has elegido hamburguesa")
    elif opcion == 2:
        cant_pizza += 1
        total_pizza += 10000
        print("Has elegido pizza")
    elif opcion == 3:
        cant_ensalada += 1
        total_ensalada += 5000
        print("Has elegido Ensalada")
    elif opcion == 4:
        cant_salchipapa  += 1
        total_salchipapa += 13000
        print("Has elegido Salchipapa")
    elif opcion == 5:
        cant_perroCaliente += 1
        total_perroCaliente += 13000
        print("Has elegido perro caliente")
    elif opcion == 6:
        total = total_hamburguesa + total_pizza + total_ensalada + total_salchipapa + total_perroCaliente
        print(f"El total de la cuenta es: ${total}")
        print(f"Para {cant_hamburguesa} hamburguesas, el total hamburguesas: ${total_hamburguesa}")
        print(f"Para {cant_pizza} hamburguesas, el total pizza: ${total_pizza}")
        print(f"Para {cant_ensalada} hamburguesas, el total ensalada: ${total_ensalada}")
        print(f"Para {cant_salchipapa} hamburguesas, el total salchipapa: ${total_salchipapa}")
        print(f"Para {cant_perroCaliente} hamburguesas, el total perro caliente: ${total_perroCaliente}")
        break
    else:
        print("Opción no válida, por favor ingrese de nuevo.")
        
    print(menu)