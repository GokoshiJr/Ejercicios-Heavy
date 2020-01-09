import math
""" Desarrolle la siguiente serie:
S = 2X/2! - 3X^2/3! 4X^3/4! - 5X^4/5! + ... 
En esta serie, se leera el valor de x y épsilon, la misma se desarrollará hasta que el módulo 
del término siguiente sea menor que un épsilon sado osea: |termino| < épsilon
"""
# Declaración de Variables
sumatoria = termino = x = factorial = 0.0
exponente = 0
print("-"*30)
print("        Serie Heavy 2")
print("-"*30)
# Entrada de Datos
x = float(input("Valor de X: "))
epsilon = float(input("Valor de épsilon: "))
print("-"*30)
# Ciclo, obtención de término, acumulación término
termino = 2*x/2           
i = 1
while abs(termino) > epsilon:
    print("Término",i,"=",round(termino,2))
    sumatoria += termino
    i = i + 1
    factorial = 1
    for j in range(1,i+2):
        factorial *=j
    termino = (-1)**(i+1)*((i+1)*x**i)/factorial
# Salida de resultado
print("-"*30)
print("Sumatoria:",round(sumatoria,2))