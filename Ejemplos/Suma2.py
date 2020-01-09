import math
# Algoritmo de descomposición de un número en sus dígitos, del más significativo al menos significativo
# Declaración de Variables
num = potencia = digito = suma = temporal = contDigitos = 0
# Entrada de datos
print("-"*30)
print("       Descomposición 2")
print("-"*30)
num = int(input("Ingrese un número entero: "))
print("-"*30)
print("Del más al menos significativo")
# Ciclo que descompone el número y suma sus dígitos
temporal = num
while (temporal != 0): # El ciclo se ejecuta hasta temporal = 0
    contDigitos += 1
    temporal //= 10 # Eliminamos el dígito obtenido de temporal
potencia = pow(10,contDigitos-1)    
temporal = num
while (temporal != 0):
    digito = (temporal // potencia)
    temporal %= potencia
    potencia //= 10
    suma += digito
    print(digito, end="  ")
print("")
print("-"*30)
print("Para el número:",num)
print("La suma de sus dígitos es:",suma)