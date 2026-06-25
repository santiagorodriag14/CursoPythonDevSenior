"""a = 10
b = 3


##### OPERADORES ARITMETICOS #####
print("##### OPERADORES ARITMETICOS ##### \n")
#Suma +
suma = a + b
print(suma)

#resta - 
resta = a - b
print("La resta es:", resta)

#Multiplicación *
multiplicacion = a*b
print("La multiplicación es:", multiplicacion)

#División /
division = a/b
print("La división es:", division)

#Potencia **
potencia = a**b
print("La pontencia es:", potencia)

#Modulo // -> es el residuo de una division
modulo = a%b
print("El módulo es:", modulo)

#División entera // -> solo entrega la parte entera de la división
divisionEntera = a//b
print("La división entera es:", divisionEntera, "\n")


##### OPERADORES DE ASIGNACIÓN #####
# +=    -> adicion a la variable por el numero a la izquierda
# -=    -> resta a la variable por el numero a la izquierda
# *=    -> multiplica a la variable por el numero a la izquierda
# /=    -> División a la variable por el numero a la izquierda
# **=   -> potencia por el numero a la izquierda
# %=    -> Hace el modulo de la variable por el numero a la izquierda
# //=   -> Hace la división entera entre la variable y el numero a la izquierda


##### OPERADORES DE COMPARACIÓN #####
print("##### OPERADORES DE COMPARACIÓN ##### \n")
#Estos devuelven un valor de lógico (de verdad) (TRUE O FALSE)

#Mayor que >
print("a es mayor que b?", a>b)

#Mayor o igual que >=
print("a es mayor o igual que b?", a>=b)

#Menor que <
print("a es menor que b?", a<b)

#Menor o igual que <=
print("a es menor o igual que b?", a<=b)

#Diferente de !=
print("a es diferente que b?", a != b)

#Igual a ==
print("a es igual que b?", a == b, "\n")

##### OPERADORES LÓGICOS #####
print("##### OPERADORES LÓGICOS #####")
c = 5

#or, and, not
print(a>=b or b>c)
print(a>=b and b>c)"""

### CALCULADORA ###
"""a = float(input("Ingrese el número a: "))
b = float(input("ingrese el número b: "))
operacion = input("ingrese el nú mero de la operación que desea hacer: \n "
                    "1. suma \n"
                    "2. resta \n"
                    "3. multiplicacion \n"
                    "4. division \n"
                    "5. potencia \n"
                    "6. modulo \n"
                    "7. division entera \n")

if operacion == "1":
    print(f"{a} + {b} = {a + b}")
elif operacion == "2":
    print(f"{a} - {b} = {a - b}")
elif operacion == "3":
    print(f"{a} * {b} = {a * b}")
elif operacion == "4":
    print(f"{a} / {b} = {a / b}")
elif operacion == "5":
    print(f"{a} ** {b} = {a ** b}")
elif operacion == "6":
    print(f"{a} % {b} = {a % b}")
elif operacion == "7":
    print(f"{a} // {b} = {a // b}")
else:
    print("El dato digitado es incorrecto")"""

#EJERCICIO

"""nombre = input("Ingrese su nombre: ")

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

print(f"Hola {nombre} la suma de los numeros es: {numero1 + numero2}")
print(f"La resta de los numeros es: {numero1 - numero2}")
print(f"La multiplicación de los numeros es: {numero1 * numero2}")
print(f"La división de los numeros es: {numero1 / numero2}")
print(f"La división entera de los numeros es: {numero1 // numero2}")
print(f"El módulo de la división de los numeros es: {numero1 % numero2}")
print(f"La potencia de los numeros es: {numero1 ** numero2}")"""

"""#EJERCIO: Hacer un programa que calcule el área de un circulo
radio = float(input("Ingrese el radio del circulo en cm:"))
PI = 3.1416
area = PI*(radio**2)
print(f"El área de un circulo con radio de {radio} cm es de {area} cm^2")"""

#EJERCIO: Hacer un programa que calcule el área de un triangulo
"""lado1 = float(input("Ingrese el lado 1 del triangulo en cm:"))
lado2 = float(input("Ingrese el lado 2 del triangulo en cm:"))
area = (lado1*lado2)/2
print(f"El área de un triángulo con una lado de {lado1} cm y otro de {lado2} es de {area} cm^2")"""

"""EJERCICIO: Calcular el valor a pagar a un empleado por su trabajo de la semana
se pregunta cuantas horas trabajó el empleadao y cuanto gana por hora y al final
se muestra el valor a pagar al empleado"""

horas_semana = int(input("Ingrese las horas trabajadas del empleado: "))
precio_hora = int(input("Valor por hora de trabajo: "))
print(f"El valor a pagar al empleado por {horas_semana} horas trabajadas a un precio de {precio_hora} la hora es: $ {horas_semana*precio_hora} pesos")