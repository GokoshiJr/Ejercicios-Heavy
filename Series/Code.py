import math
""" 
Una empresa de productos masivos quiere por motivos de seguridad asignarles un código personalizado
a cada uno de sus empleados. la aplicación tendrá como entrada la edad del empleado (todos mayores de edad) 
y la cédula de identidad del mismo. El código de acceso se construirá de la siguiente manera: Los dos primeros 
dígitos del código será la edad del empleado, los siguientes 4 dígitos del código serán los primeros 4
dígitos pares de la cédula, procediendo del digito menos significativo al más 
significativo, en caso de faltar digitos pares se completarán con ceros, considere el 0 como par. 
"""
# Declaración de Variables
edad = cedula = codigo = digito = temporal = contPares = pares = 0
print("-"*30)
print("       Código Personal")
print("-"*30)
# Entrada de Datos
edad = int(input("Edad del empleado: "))
cedula = int(input("Cédula del empleado: "))
# Proceso
codigo = edad
temporal = cedula
while (temporal != 0) and (contPares < 4):
    digito = (temporal % 10)
    if (digito % 2 == 0):
        pares = ((pares * 10) + digito)
        contPares += 1
    temporal //= 10
codigo = (codigo * pow(10,4)) + (pares * pow(10,(4 - contPares)))
print("-"*30)
print("Para el empleado de edad:",edad)
print("Cédula:",cedula)
print("-"*30)
print("El código asignado será:",codigo)