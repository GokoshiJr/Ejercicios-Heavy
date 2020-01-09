import math
""" Desarrolle la siguiente serie:
S = 2X/2! - 3X^2/3! + 4X^3/4! - 5X^4/5! + ...
"""
# Declaración de Variables
sumatoria = termino = x = factorial = 0.0
exponente = n = 0
print("-"*30)
print("        Serie Heavy 1")
print("-"*30)
# Entrada de Datos
x = float(input("Valor de X: "))
n = int(input("Número de términos: "))
print("-"*30)
# Ciclo, obtención de término, acumulación término
for i in range (1, n + 1):    
    factorial = 1
    for j in range(1,i+2):
        factorial *= j
    termino = (-1)**(i+1)*((i+1)*x**i)/factorial
    print("Término",i,"=",round(termino,2))
    sumatoria += termino
# Salida de resultado
print("-"*30)
print("Sumatoria:",round(sumatoria,2))