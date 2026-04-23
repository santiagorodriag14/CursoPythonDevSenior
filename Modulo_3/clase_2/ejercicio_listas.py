a = ["fresa","manzana","pera","manzana","naranja","manzana","sandia"]
"""caracteres = 0
for elemento in a:
    caracteres += len(elemento)
    print(f"{elemento} tiene {len(elemento)} caracteres")

print(f"La cantidad total de caracteres en la lista es {caracteres}")
"""
#Imprimiendo cada elemento de la lista con un ciclo while
"""cant_elementos = len(a)
while cant_elementos > 0:
    print(a[-cant_elementos])
    cant_elementos -=1"""

#otro modo
"""pos =0
while pos < len(a):
    print(a[pos])
    pos += 1"""

#Encontrar con index la cantidad de manzanas
"""for i in range(len(a)):
    i -= 1
    if a[i] == "manzana":
        print(f"Manzana encontrada en la posición {i}")
"""
#otro modo
"""i = 0
while i < len(a):
    if a[i] == "manzana":
        print(f"Manzana encontrada en la posición {i}")
    i += 1"""
