import csv

"""with open("productos.csv", "r", encoding= "utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)"""

#Editar el archivo e insertar filas, es necesario poner newline para que no haga saltos de linea dentro del archivo

"""datos = [
    ["Monitor", 2500000], 
    ["Mouse", 300000]
    ]
with open("productos.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "precio"])
    
    for fila in datos:
        escritor.writerow(fila)"""

#Hacer diccionarios tomando los encabezados
"""with open("productos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    print(lector.fieldnames) #Muestra los encabezados que toma como llaves para crear el diccionario
    print(type(lector))

    for fila in lector:
        print(fila)
        print(fila["nombre"],fila["precio"])"""

#Convertir diccionario en archivo
"""with open("productos.csv", "w", encoding= "utf-8", newline="") as archivo:
    campos = ["nombre","precio"]

    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()

    escritor.writerow({
        "nombre" : "Mousepad",
        "precio" : 50000
    })

    escritor.writerow({
        "nombre" : "torre",
        "precio" : 2000000
    })"""

with open("archivo_comas.csv","r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo,delimiter=";")

    for fila in lector:
        print(fila)