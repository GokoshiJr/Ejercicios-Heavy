import math
# Ejercicio de Series 2
""" 
Crear un programa que desarrolle la siguiente serie:
S = 1/x - 1/x**2 + 1/x**3 - 1/x**4 + .....
Donde x es un valor real, desarrollare la serie mientras el cociente
1/X**n sea mayor que un epsilon dado, en la salida mostrar cada
termino de la serie, cuantos terminos se acumularon y la sumatoria
"""
s = 0.0
cont = 0
exp = 1
signo = True
x = float(input("Ingrese el valor de X: "))
epsilon = float(input("Ingrese el valor de Epsilon: "))

print("")
print("Terminos de la serie")
cociente = 1/x
while cociente > epsilon:
    print(cociente)
    if signo:
        s += cociente
        signo = False
    else:
        s -= cociente
        signo = True
    cont += 1
    exp += 1
    cociente = 1/pow(x,exp)
print("")
print("La sumatoria es: ",s)
print("Se acumularon ",cont," terminos en la serie")
print("Fin del programa")

