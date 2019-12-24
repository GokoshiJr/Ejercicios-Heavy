# Declaración de Variables
jinete = caballo = ""
minutos = segundos = 0
tiempoRealizado = obstaculos = segPenalizados1 = segPenalizados2 = ponderacionFalta = tiempoFinal = 0
tiempoMaxPermitido = 90
# Captura de Datos
jinete = input(" Nombre del jinete: ")
caballo = input(" Nombre del caballo: ")
minutos = int(input(" Minutos realizó el recorrido: "))
segundos = int(input(" Segundos realizó el recorrido: "))
obstaculos = int(input(" Obstaculos derribados: "))
print("-"*30)
print(" Resultados")
print("-"*30)
tiempoRealizado = (minutos * 60 + segundos)
# Proceso
if (obstaculos <= 10):
    if (tiempoRealizado > tiempoMaxPermitido):
        segPenalizados1 = (tiempoRealizado - tiempoMaxPermitido)
    if (obstaculos > 0):
        if (obstaculos <= 5):
            ponderacionFalta = 4
        else:
            ponderacionFalta = 6
        segPenalizados2 = (obstaculos * ponderacionFalta)
    tiempoFinal = (tiempoRealizado + segPenalizados1 + segPenalizados2)
    print("",jinete,"montado a",caballo)
    print(" Realizó el recorrido en",tiempoFinal,"Segundos")
else:
    print(jinete,"Quedó fuera de la competencia derribo más de 10 obstaculos")
print("-"*30)   
print(" Fin del programa")
