"""for x in range(1,11):   #Siempre cuenta hasta uno menos range(a, b) va hasta b-1
    print(x)

for x in range(5):      #Si solo se pone un parametro va desde 0 a 5-1
    print(x)

for x in range(2,10,2): #Va de 2 a 10 pero saltando de dos en dos
    print(x)

texto = "Hola a todos"
for letra in texto:
    print(letra)
    """

#Hacer una tabla de multiplicar con for
"""numero = int(input("Escriba el número de la tabla que desea: "))
for i in range(11):
    resultado = i*numero
    print(f"{i} * {numero} = {resultado}")"""

nota1 = 5
nota2 = 3
nota3 = 2
if nota1 <= 5 and nota2 <= 5 and nota3 <= 5 and nota1>= 0 and nota2>= 0 and nota3>= 0 :
    print("Hola")