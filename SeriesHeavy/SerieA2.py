import math
""" Desarrolle la siguiente serie:
S = N!/2X - 4X^2/(N-1) + (N-2)!/6X^3 - 8X^4/(N-3)! + (N-4)!/8X^5 - ...
"""
# Declaración de Variables
sumatoria = termino = factorial = 0.0
n = factor = final = 0
estatus = ""
signo = True
print("-"*30)
print("       Serie Heavy A2")
print("-"*30)
# Entrada de Datos
x = float(input("Valor de X:"))
n = int(input("Número de términos:"))
# Ciclo, obtención término, acumulación término
factor = 2
final = n
print("Términos de la serie")
print("-"*30)
for i in range (1, final + 1):
    # Calculo del factorial de i
    factorial = 1
    for j in range (1,n+1):
        factorial *=j
    if signo:
        termino = factorial / (factor * pow(x,i))
        sumatoria += termino
        estatus = "+"
    else:
        termino = (factor * pow(x,i)) / factorial
        sumatoria -= termino
        estatus = "-"
    print("Término",i,"=",estatus,round(termino,2))
    n -= 1
    factor += 2
    signo = not(signo)
# Salida de resultados
print("-"*30)
print("Sumatoria:",round(sumatoria,2))