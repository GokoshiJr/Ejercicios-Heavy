import math
# Ejercicio de Series 2
""" 
Crear un programa que desarrolle la siguiente serie:
S = 1/x - 1/x**2 + 1/x**3 - 1/x**4 + .....
Donde x es un valor real, desarrollare la serie mientras el cociente
1/X**n sea mayor que un epsilon dado, en la salida mostrar cada
termino de la serie, cuantos terminos se acumularon y la sumatoria
"""
# Inicialización de Variables
sumatoria = 0.0
cont = 0
exp = 1
signo = True
print("-"*30)
print("\t   Serie 2")
print("-"*30)
# Entrada de Datos
x = float(input("Ingrese el valor de X: "))
epsilon = float(input("Ingrese el valor de Epsilon: "))
print("-"*30)
print("Términos de la serie")
cociente = 1/x
while cociente > epsilon: # Ciclo while
    print(cociente)
    if signo:
        sumatoria += cociente
        signo = False
    else:
        sumatoria -= cociente
        signo = True
    cont += 1
    exp += 1
    cociente = 1/pow(x,exp)
print("-"*30)
print("La sumatoria es:",sumatoria)
print("Se acumularon",cont,"términos en la serie")