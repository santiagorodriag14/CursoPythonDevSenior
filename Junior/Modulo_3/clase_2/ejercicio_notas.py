"""Pedir al usuario que ingrese notas entre 
0 y 10 hasta que ingrese -1 para finalizar.
Luego mostrar el promedio de las notas ingresadas"""

notas = []
valor_nota = 0
mensaje = "Ingrese su nota entre 1 y 10, ingrese -1 para dejar de ingresar valores"
promedio = 0

while valor_nota != -1:
    print(mensaje)
    valor_nota = float(input("Ingrese el valor:"))
    if valor_nota>=0 and valor_nota<=10:
        notas.append(valor_nota)
    elif valor_nota == -1:
        print("Ingreso de notas finalizado")
        break
    else:
        print("Ingresó mal los valores")

if len(notas)>0:
    for i in notas: 
        promedio += i

    promedio = promedio/len(notas)

    print(f"El promedio de las notas ingresadas es {promedio}")
else:
    print("No hay notas ingresadas")