import math
""" Desarrolle la siguiente serie:
S = 2X/2! - 3X^2/3! 4X^3/4! - 5X^4/5! + ... 
En esta serie, se leera el valor de x y epsilon, la misma se desarrollará hasta que el modulo 
de la diferencia entre el termino anterior y el siguiente sea menor que un epsilon sado osea: 
|termino anterior - termino siguiente| < epsilon
"""
# Declaración de Variables
sumatoria = x = factorial = 0.0
print("-"*30)
print("        Serie Heavy 3")
print("-"*30)
# Entrada de Datos
x = float(input("Valor de X: "))
epsilon = float(input("Valor de épsilon: "))
print("-"*30)
# Ciclo, obtención de término, acumulación término
terminoAnt = 0
terminoSig = 2*x/2          
i = 1
while abs(terminoAnt - terminoSig) > epsilon:
    print("Término",i,"=",round(terminoSig,2))
    sumatoria += terminoSig
    i = i + 1
    terminoAnt = terminoSig
    factorial = 1
    for j in range(1,i+2):
        factorial *=j
    terminoSig = (-1)**(i+1)*((i+1)*x**i)/factorial
# Salida de resultado
print("-"*30)
print("Sumatoria:",round(sumatoria,2))