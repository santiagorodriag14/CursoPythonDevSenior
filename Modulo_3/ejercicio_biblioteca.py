
biblioteca ={
    "autores"   :   {},
    "libros"    :   {},
    "usuarios"  :   {},
    "prestamos" :   {}
}

opcion = ""

while opcion != 8:
    print("Opciones")
    opcion = int(input("Seleccione una opción:"))
    
    #Agregar autor
    if opcion == 1:
        titulo = input("Ingrese el título del libro: ")
        isbn = input("Ingrese el ISBN del libro:")
        ano_publicacion = input("Ingrese el año de publicación en el formato dd/mm/aaaa: ")
        
        autores = []
        num_autores = int(input("Ingrese el número de autores del libro"))
        for i in range(num_autores):
            autor = input(f"Ingrese el nombre del autor número {i+1}: ")
            for id, info in biblioteca["autores"].items():
                if info["nombre"] == autor:
                    print(f"El autor {autor} ya existe en la biblioteca con ID {id}.")
                    break
            autores.append(autor)
        
        categorias = set()
        num_categorias = int(input("Ingrese el número de categorías del libro"))
        for i in range(num_categorias):
            categoria = input(f"Ingrese la categoría número {i+1}: ")
            categorias.add(categoria)
        
        num_total_copias = int(input("Ingrese el número total de copias: "))
        num_copias_disponibles = int(input("Ingrese el número de copias disponibles: "))

        biblioteca["libros"][isbn] = {
            "titulo"    :   titulo,
            "isbn"      :   isbn,
            "año_publicacion"   : ano_publicacion,
            "autores"   : autores,
            "categorias" : categorias,
            "numero_total_copias" : num_total_copias,
            "numero_copias_disponibles" : num_copias_disponibles
        }


    elif opcion == 2:
        autor = input("Ingrese el nombre del autor: ")
        id = input("Ingrese la identificaión única del autor:")
        nacionalidad = input("Ingrese la nacionalidad del autor:")
        ano_nacimiento = input("Ingrese el año de nacimiento en el formato dd/mm/aaaa: ")
        biblioteca["autores"][id] = {
            "nombre"        :   autor,
            "id"            :   id,
            "nacionalidad"  :   nacionalidad,
            "año_nacimiento":   ano_nacimiento
        }

    elif opcion == 3:
        nombre = input("Ingrese el nombre completo del usuario")
        id = input("Ingrese la identificación única del usuario")
        correo = input("Ingrese el correo electrónico del usuario")
        telefono = input("Ingrese el número de teléfono del usuario")
        biblioteca["usuarios"][id] = {
            "nombre"    :   nombre,
            "id"        :   id,
            "correo"    :   correo,
            "telefono"  :   telefono
        }
    elif opcion == 4:
        id_prestamo = input("Ingrese la identificación única del préstamo")
        id_usuario = input("Ingrese la identificación del usuario que realiza el préstamo")
        isbn_libro = input("Ingrese el ISBN del libro que se va a prestar")
        fecha_prestamo = input("Ingrese la fecha del préstamo en el formato dd/mm/aaaa: ")
        fecha_devolucion = input("Ingrese la fecha de devolución en el formato dd/mm/aaaa: ")
        estado = input("Ingrese el estado del préstamo (activo, devuelto, atrasado): ")
        if id_usuario not in biblioteca["usuarios"] or isbn_libro not in biblioteca["libros"]:
            print("El usuario o el libro no existen en la biblioteca.")
        else:
            biblioteca["prestamos"][id_prestamo] = {
                "id_usuario"   :   id_usuario,
                "isbn_libro"   :   isbn_libro,
                "fecha_prestamo" : fecha_prestamo,
                "fecha_devolucion" : fecha_devolucion,
                "estado"       : estado
            }



