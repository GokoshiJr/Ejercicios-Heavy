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
i = n = 0
signo = True
# Entrada de Datos
x = float(input("Ingrese el valor de X: "))
n = int(input("Cuantos terminos acumulara la serie: "))
# Proceso
print("")
print("Terminos de la Serie")
# Ciclo for
for i in range (1, n+1):
    acum = 1/pow(x,i)
    print(acum)
    if signo: 
        serie += acum
        signo = False
    else:
        serie -= acum
        signo = True
print("")
print("La sumatoria es: ", s)
print("Fin del programa")
        

 
