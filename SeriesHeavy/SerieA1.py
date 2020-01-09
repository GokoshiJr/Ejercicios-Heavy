import math
""" Desarrolle la siguiente serie:
S = - X^1/1! + X^4/1*3 - X^9/3! + X^16/1*3*5 - X^25/5! + ...
"""
# Declaración de Variables
sumatoria = termino = factorial = 0.0
n = factor = final = aux = aux2 = exp2 = 0
estatus = ""
signo = True
print("-"*30)
print("       Serie Heavy A1")
print("-"*30)
# Entrada de Datos
x = float(input("Valor de X: "))
n = int(input("Numero de terminos: "))
print("-"*30)
# Ciclo, obtención término, acumulación término
factor = aux2 = exp2 = 1
final = n
for i in range (1, final + 1):
    # Calculo del factorial de i
    factorial = 1
    aux += 1
    factor = (i * aux)      
    for j in range (1,i+1):
        factorial *= j    
    if signo:        
        termino = (pow(x,factor) / factorial)
        signo = False
        sumatoria -= termino
        estatus = "-"      
    else:        
        signo = True
        aux2 += 2
        exp2 *= aux2
        termino = (pow(x,factor) / exp2)
        sumatoria += termino
        estatus = "+"        
    print("Término",i,"=",estatus,round(termino,2))     
# Salida de resultados
print("-"*30)
print("Sumatoria:",round(sumatoria,2))