# Ejercicio Conversión de Coordenadas
import math
""" Escribir una aplicación en python que permita convertir Coordenadas Cartesianas en Polares
y Polares en Cartesianas. Y determinar en que cuadrante se encuentran las coordenadas"""
# Declaración de Variables
x = y = r = angulo = 0.0
rad = grados = 0.0
cuadrante = ""
# Menú
print("-"*30)
print("  Convertidor de Coordenadas")
print("-"*30)
print("1) Cartesianas a Polares")
print("2) Polares a Cartesianas")
print("-"*30)
opc = int(input("Ingrese una opción: "))
print("-"*30)
if (opc == 1):
    x = float(input("Ingrese el valor de X: "))
    y = float(input("Ingrese el valor de Y: "))
    r = (math.sqrt(pow(x,2) + pow(y,2)))
    rad = (math.atan(y/x))
    grados = (math.degrees(rad))
else:
    r = float(input("Ingrese el valor de R: "))
    grados = float(input("Ingrese el Ángulo: "))
    rad = (math.radians(grados))
    x = (r * math.cos(rad))
    y = (r * math.sin(rad))
# Determinamos el cuadrante
if (x >= 0) and (y >= 0):
    cuadrante = "I"
elif (x < 0) and (y >= 0):
    cuadrante = "II"
    if (opc == 1):
        grados += 180
elif (x < 0) and (y < 0):
    cuadrante = "III"
    if (opc == 1):
        grados += 180
elif (x >= 0) and (y < 0):
    cuadrante = "IV"
    if (opc == 1):
        grados += 360
print("-"*30)
print("\t Resultados")
print("-"*30)
print("Está en el cuadrante",cuadrante)
if (opc == 1):
    print("R =",round(r,2))
    print("Ángulo =",round(grados,2))
else:
    print("X =",round(x,2))
    print("Y =",round(y,2))