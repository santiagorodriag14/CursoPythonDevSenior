frutas = ["papaya","naranja","pera","fresa"]
print(len(frutas))

print("naranja" in frutas) #Verifica si hay un elemento "naranja" en frutas

frutas.append("mandarina") #Agrega elemento al final de la lista
print(frutas)

frutas.insert(2, "kiwi") #Agrega elemento en una posición especifica de la lista
print(frutas)

frutas[2] = "aguacate"  #sobreescribe aguacate en el elemento 2 de la lista
print(frutas)

print(frutas[2])

frutas.reverse() #Invierte la lista
print(frutas)

"""frutas.clear() #Vacía la lista, pero no borra la lista
print(frutas)

del frutas #borra la lista, del = delete"""

copia = frutas.copy() #Guarda una copia de la lista en la variable copia
print(copia)

print(frutas.count("mango")) #Cuenta las veces que está un elemento dado en la lista

#frutas.extend(("platano","banano")) #Extiende la lista con los elementos de la lista que se le entrega
verduras = ["Cebolla","tomate","zanahoria"]
frutas.extend(verduras)
print(frutas)

#frutas.append(verduras) #No expande, mete la lista verduras como elemento de la lista frutas
print(frutas)

a = frutas.pop(1)      #pop elimina el elemento de la posición dada y lo retorna
print(a)
frutas.remove("naranja")
print(frutas)

frutas.sort()       #Organiza de forma alfabetica o de menor a mayor
print(frutas)