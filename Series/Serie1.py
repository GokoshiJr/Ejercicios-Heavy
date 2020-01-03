import math
# Ejercicio de series 1
""" 
Crear un programa que desarrolle la siguiente serie:
S = 1/x - 1/x**2 + 1/x**3 - 1/x**4 + .....
Donde x es un valor real, desarrollare la serie para N terminos
en la salida mostrar cada termino de la serie y la sumatoria
"""
# Inicialización de Variables
serie = acum = x = 0.0
i = n = cont = 0
signo = True
print("-"*30)
print("\t   Serie 1")
print("-"*30)
# Entrada de Datos
x = float(input("Ingrese el valor de X: "))
n = int(input("Cuantos términos acumulara la serie: "))
# Proceso
print("-"*30)
print("Términos de la Serie")
for i in range (1, n+1): # Ciclo for
    acum = 1/pow(x,i)
    print(acum)
    if signo: 
        serie += acum
        signo = False
    else:
        serie -= acum
        signo = True
    cont += 1
print("-"*30)
print("La sumatoria es: ", serie)
print("Se acumularon",cont,"términos en la serie")