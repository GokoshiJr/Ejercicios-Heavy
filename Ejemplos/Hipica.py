"""El club hípico esta organizando la competencia de salto anual del estado
Carabobo, desarrolle un programa que ayude a determinar el tiempo final del competidor"""
# Declaración de Variables
jinete = caballo = ""
minutos = segundos = tiempoRealizado = tiempoPermitido = 0
obstaculos = penaTiempo = penaDerribo = ponderacionFalta = tiempoFinal = 0
tiempoPermitido = 90
# Entrada de datos
print("-"*30)
print("\t    Datos")
print("-"*30)
jinete = input("Nombre del jinete: ")
caballo = input("Nombre del caballo: ")
minutos = int(input("Minutos del recorrido: "))
segundos = int(input("Segundos del recorrido: "))
obstaculos = int(input("Obstáculos derribados: "))
print("-"*30)
print("\t Resultados")
print("-"*30)
# Proceso
tiempoRealizado = ((minutos * 60) + segundos)
if obstaculos <= 10:
    if tiempoRealizado > tiempoPermitido:
        penaTiempo = tiempoRealizado - tiempoPermitido
    if obstaculos > 0:
        if obstaculos <= 5:
            ponderacionFalta = 4
        else:
            ponderacionFalta = 6
        penaDerribo = obstaculos * ponderacionFalta
    tiempoFinal = tiempoRealizado + penaTiempo + penaDerribo
    print(jinete,"montando a", caballo)
    print("Realizó el recorrido en",tiempoFinal,"segundos")
else:
    print("Descalificado por derribar más de 10 obstáculos")