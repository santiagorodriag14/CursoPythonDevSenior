# Archivos de texto plano – Escritura y lectura segura

# r para leer
# w para escribir
# a para agregar
# r+ para leer y escribir
# x pra crear un nuevo archivo

"""archivo =  open("saludo.txt", "w")
archivo.write("Hola mundo!")
archivo.close() """

"""archivo = open("tareas.txt", "r")
linea = archivo.readline()
print(linea)
archivo.close()"""

"""archivo = open("tareas.txt", "r")
lineas = archivo.readlines()
print(lineas)
archivo.close()

for linea in lineas:
    linea = linea.rstrip("\n")
    print(linea)"""

#Para no usar .close(), se utiliza:

"""with open("tareas.txt", "w", encoding= "utf-8") as archivo:
    archivo.write("Saludos para todos")

with open("tareas.txt", "r", encoding= "utf-8") as archivo:
    linea = archivo.readline()
    print(linea)

with open("tareas.txt", "a", encoding= "utf-8") as archivo:
    archivo.write("\nHola manito")

with open("tareas.txt", "r", encoding= "utf-8") as archivo:
    lineas = archivo.readlines()
    print(lineas)"""

#Creando función que guarde texto
def guardar_texto(nombre_archivo, texto):
    with open(nombre_archivo, "w", encoding= "utf-8") as archivo:
        archivo.write(texto)

def cargar_texto(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding= "utf-8") as archivo:
            texto = archivo.read()
            return texto
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return None

def guardar_tareas(tareas):
    with open("tareas.txt", 'w', encoding= "utf-8") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

def cargar_tareas():
    try:
        with open("tareas.txt", 'r', encoding= "utf-8") as archivo:
            return [linea.strip() for linea in archivo.readlines()]
    except:
        return ("El archivo no existe")
    
tareas = ["Hacer la cama", "Sacar el perro", "Ir al gimnasio"]
guardar_tareas(tareas)
tareas_cargadas = cargar_tareas()
print(tareas_cargadas)