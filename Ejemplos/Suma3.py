import math
# Algoritmo de descomposición de un número en sus dígitos, armando un número nuevo solo con los pares del anterior
# Declaración de Variables
cedula = potencia = digito = armaPares = suma = temporal = contDigitos = 0
# Entrada de datos
print("-"*30)
print("       Descomposición 3")
print("-"*30)
cedula = int(input("Ingrese su cédula: "))
print("-"*30)
print("Dígitos capturados:")
# Ciclo que descompone el número y suma sus dígitos
temporal = cedula
while (temporal != 0): # El ciclo se ejecuta hasta temporal = 0
    contDigitos += 1
    temporal //= 10 # Eliminamos el dígito obtenido de temporal
potencia = pow(10,(contDigitos - 1))    
temporal = cedula
while (temporal != 0):
    digito = (temporal // potencia)
    temporal %= potencia
    potencia //= 10    
    print(digito, end="  ")
    if (digito % 2 == 0):
        armaPares = ((armaPares * 10) + digito)
print("")
print("-"*30)
print("Para cedula:",cedula)
print("El armado de los pares es:",armaPares)