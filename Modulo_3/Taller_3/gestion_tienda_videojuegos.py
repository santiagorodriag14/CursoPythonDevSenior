videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }}

def agregar_videojuego(videojuegos):
    codigo = input("Ingrese el código del videojuego: ")
    for codigo_juego in videojuegos.keys():
        if codigo == codigo_juego:
            codigo_ant = codigo
            while codigo == codigo_ant:
                print("Error! El código ingresado ya existe")
                codigo = input("Ingrese el código del videojuego nuevamente: ")
   
    nombre = input("Ingrese el nombre del videojuego: ")
    plataforma = input("Ingrese la plataforma (PC, PlayStation, Xbox, Nintendo): ")
    precio = float(input("Ingrese el precio: "))
    while precio <= 0:
        precio = float(input("Error! El precio debe ser mayor que cero, ingreselo de nuevo: "))
    cant_inventario = int(input("Ingrese la cantidad en inventario: "))
    while cant_inventario <= 0:
        cant_inventario = int(input("Error! La cantidad en inventario debe ser mayor que cero, ingreselo de nuevo: "))
    
    videojuegos[codigo]={
        "nombre" : nombre,
        "plataforma" : plataforma,
        "precio" : precio,
        "cantidad" : cant_inventario
    }
    print("\n")


def mostrar_inventario(videojuegos):
    print("""===== INVENTARIO =====""")
    for cod,juego in videojuegos.items():
        print(f"Código : {cod}")
        print(f"Nombre: {juego['nombre']}")
        print(f"Plataforma: {juego['plataforma']}")
        print(f"Precio: {juego['precio']}")
        print(f"Cantidad: {juego['cantidad']}")
        print("\n")

def buscar_videojuego(videojuegos):
    buscar_cod = input("Ingrese el código del videojuego a buscar: ")
    mensaje = f"El videojuego con el código {buscar_cod} no existe. \n"
    for cod,juego in videojuegos.items():
        if buscar_cod == cod:
            mensaje = f"""Código : {cod} \nNombre: {juego['nombre']} \nPlataforma: {juego['plataforma']} \nPrecio: {juego['precio']} \nCantidad: {juego['cantidad']} \n"""
    print(mensaje)


def actualizar_precio(videojuegos):
    buscar_cod = input("Ingrese el código del videojuego a buscar: ")
    mensaje = f"El videojuego con el código {buscar_cod} no existe. \n"
    for cod,juego in videojuegos.items():
        if buscar_cod == cod:
            precio = float(input("Ingrese el precio actualizado: "))
            while precio <= 0:
                precio = float(input("Error! El precio debe ser mayor que cero, ingreselo de nuevo: "))
            juego['precio'] = precio
            mensaje = f"El videojuego con código '{cod}' quedó con un precio de ${juego['precio']} \n"
    print(mensaje)
        

def registrar_venta(videojuegos):
    buscar_cod = input("Ingrese el código del videojuego: ")
    cant = int(input("Ingrese la cantidad de videojuegos a vender: "))
    mensaje = f"El videojuego con el código {buscar_cod} no existe. \n"
    for cod,juego in videojuegos.items():
        if buscar_cod == cod:
            if cant <= juego['cantidad']:
                juego['cantidad'] = juego['cantidad'] - cant
                total = cant * juego['precio']
                mensaje = f"""Factura de Venta:\n----------------------------------\nJuego: {juego['nombre']}\nPrecio unitario: ${juego['precio']}\nCantidad: {cant}\n----------------------------------\nTotal a Pagar: ${total} \n"""
            else:
                mensaje = f"La cantidad solicitada excede la cantidad de videojuegos disponibles ({juego['cantidad']}). \n"
    print(mensaje)


def mostrar_estadisticas(videojuegos):
    cant_juegos = 0
    total_inventario = 0
    precio_costoso = 0
    vg_costoso = ""
    mayor_cant = 0
    vg_mayor_cantidad = ""
    promedio = 0
    for cod,juego in videojuegos.items():
        cant_juegos += 1
        total_inventario += juego['cantidad']*juego['precio']
        if juego['precio']> precio_costoso:
            precio_costoso = juego['precio']
            vg_costoso = juego['nombre']
        if juego['cantidad'] > mayor_cant:
            mayor_cant = juego['cantidad']
            vg_mayor_cantidad = juego['nombre']
    promedio = total_inventario/cant_juegos

    print(f"Total de videojuegos registrados: {cant_juegos}")
    print(f"Valor total inventario: ${total_inventario}")
    print(f"El videojuego más costoso es {vg_costoso} con un precio de ${precio_costoso}")
    print(f"El videojuego con más unidades disponibles es {vg_mayor_cantidad} con {mayor_cant}")
    print(f"El promedio de precios es: ${promedio}")
    print("\n")
        
def eliminar_videojuego(videojuegos):
    codigo = input("Ingrese el código del videojuego: ")
    eliminado = videojuegos.pop(codigo, None)

    if eliminado is not None:
        print(f"El videojuego con código {codigo} fue eliminado correctamente.")
    else:
        print("Error: Código no encontrado. \n")
            



def menu():
    opciones = """===== TIENDA DE VIDEOJUEGOS =====
    1. Agregar videojuego
    2. Mostrar inventario
    3. Buscar videojuego por código
    4. Actualizar precio
    5. Registrar venta
    6. Mostrar estadísticas
    7. Eliminar videojuego
    8. Salir"""
    opcion = 0
    while opcion != 8:
        print(opciones)
        opcion = int(input("Seleccione una opción: "))
        print("\n")

        if opcion == 1:
            agregar_videojuego(videojuegos)
        elif opcion == 2:
            mostrar_inventario(videojuegos)
        elif opcion == 3:
            buscar_videojuego(videojuegos)
        elif opcion == 4:
            actualizar_precio(videojuegos)
        elif opcion == 5:
            registrar_venta(videojuegos)
        elif opcion == 6:
            mostrar_estadisticas(videojuegos)
        elif opcion == 7:
            eliminar_videojuego(videojuegos)
        elif opcion == 8:
            break
        elif opcion < 1 or opcion > 8 :
            print("Por favor elija una opción correcta.\n")

menu()

