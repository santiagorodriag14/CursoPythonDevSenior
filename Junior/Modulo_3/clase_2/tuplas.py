frutas = ("manzana", "banano", "naranja")
#Otra forma de crear una tupla
#frutas2 = tuple(("pera","uva","kiwi"))

print(frutas[1:]) #para mostrar una parte especifica de la tupla, también sirve en listas

print(frutas.count("banano")) #Dice la cantidad de veces que está un elemento
print(frutas.index("banano")) #Dice la posición en la que está un elemento

#Puedo crear una copia como lista
copia = list(frutas)
print(copia)
copia.remove("naranja")
frutas = tuple(copia)
print(frutas)