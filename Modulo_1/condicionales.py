"""Hacer un programa que diga el sueldo a recibir de un
empleado, si gana menos de 2.000.000 se le da auxilio de
transporte de 200000"""

"""sueldo = int(input("Ingrese el sueldo del empleado: "))

if sueldo < 2000000:
    sueldo += 200000
    
print(f"El sueldo del empleado es: {sueldo}")"""

"""Escribir un programa que pida la edad del usuario y determine"
si es mayor de edad o no. Si la edad es mayor o igual a 18 años,
imprime "Eres mayor de edad" en caso contrario "Eres menor de edad". """

"""edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")"""

"""Escribir un programa que imprima los dias de la semana
ingresando un numero, si el numero es igual a 1, imprima lunes,
si es 2, martes, ..., si es 7, domingo"""

"""numero = int(input("Ingrese el número: "))

if numero == 1:
    print("lunes")
elif numero ==2:
    print("marttes")
elif numero ==3:
    print("miercoles")
elif numero ==4:
    print("jueves")
elif numero ==5:
    print("viernes")
elif numero ==6:
    print("sabado")
elif numero ==7:
    print("domingo")
else:
    print("Dato no válido.")"""

#Otra forma de hacerlo

"""day = int(input("Ingrese el número: "))

match day:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Viernes")
    case _:
        print("Número no válido.")"""
    
#Ejercicio uso del case
    
"""Preguntar al usuario un anima (perro, gato, pez)
    si es perro imprimir "guau"
    si es gato imprimir miau
    si es gato imprimir blup """

"""animal = input("Ingrese un animal (perro, gato, pez): ")

match animal:
    case "perro":
        print("Guau")
    case "gato":
        print("Miau")
    case "pez":
        print("Blup")
    case _:
        print("Dato invalido.")"""

#Ciclo While
"""i = 1

while i <= 5:
    print(i)
    i += 1

print("ya terminó")"""

"""EJERCICIO: Hacer código que pregunte al usuario que tabla de multiplicar quiere"""
tabla = int(input("Ingrese la tabla de multiplicaar que desea: "))
i = 0
while i<= 10:
    resultado = tabla*i
    print(f"{tabla} x {i} = {resultado}")
    i+=1

print("Ya terminó el ciclo")

