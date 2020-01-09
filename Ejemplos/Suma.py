# Algoritmo de descomposición de un número en sus dígitos, del menos significativo al más significativo
# Declaración de Variables
num = digito = suma = temporal = 0
# Entrada de datos
print("-"*30)
print("       Descomposición 1")
print("-"*30)
num = int(input("Ingrese un número entero: "))
print("-"*30)
print("Del menos al más significativo")
# Ciclo que descompone el número y suma sus dígitos
temporal = num
while (temporal != 0): # El ciclo se ejecuta hasta temporal = 0
    digito = (temporal % 10) # Obtenemos digito menos significativo
    suma += digito # Acumulamos el digito en suma
    temporal //= 10 # Eliminamos el dígito obtenido de temporal
    print(digito, end="  ")
print("")
print("-"*30)
print("Para el número:",num)
print("La suma de sus dígitos es:",suma)
