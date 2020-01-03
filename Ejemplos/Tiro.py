# Programa de tiro al blanco
import math
""" En una competencia de tiro al blanco se desea determinar la puntuación obtenida por
    el competidor en el caso de dar en la diana o si no acertó en la diana indicarlo 
    con el mensaje correspondiente.
"""
# Declaración de Variables
x = y = radio = 0.0
puntos = 0 
# Captura de Datos
print("-"*30)
print("\tTiro al Blanco")
print("-"*30)
x = float(input("Abcisa del disparo (x): "))
y = float(input("Ordenada del disparo (y): "))
radio = pow(x,2) + pow(y,2)
# Proceso
if (radio <= 16):
    if (radio <= 1):
        puntos = 100
    elif (radio <= 4):
        puntos = 50
    elif (radio <= 6):
        puntos = 25
    else:
        puntos = 10
    print("-"*30)
    print("Dió en la diana ")
    print("Puntuación",puntos,"pts")
else:
    print("-"*30)
    print(" No dió en la diana")
print("-"*30)
print("Fin del programa")