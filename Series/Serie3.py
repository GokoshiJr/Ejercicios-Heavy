import math
# Ejercicio de Series 3
"""
Crear un programa que desarrolle la siguiente serie
S = AX/2 + B/Y**2 + AX**2/4 + (B+1)/Y**3 + AX**3/6 + (B+2)/Y**4 + ...
El programa tendrá como datos de entrada A y B como valores enteros
X e Y como valores reales. La serie será desarrollada para N términos
por consola se debe mostrar cada término acumulado y la sumatoria de la serie
"""
# Declaración de Variables
cociente = x = y = 0.0
contA = 4
contB = 0
a = b = 0
exponente = 2
terminoB = True
print("-"*30)
print("\t   Serie 3")
print("-"*30)
# Entrada de Datos
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
x = float(input("Ingrese el valor de X: "))
y = float(input("Ingrese el valor de Y: "))
n = int(input("Cuántos términos tendrá la Serie: "))
# Proceso
print("-"*30)
print("Términos de la Serie")
s = (a * x) / 2
print(s)
for i in range (2,n+1): # Ciclo For
    if terminoB:
        cociente = ((b + contB) / pow(y,exponente))
        contB += 1
        terminoB = False
    else:
        cociente = (pow(a*x,exponente) / (contA))
        contA += 2
        exponente += 1
        terminoB = True
    print(cociente)
    s += cociente
print("-"*30)
print("La sumatoria es:",s)