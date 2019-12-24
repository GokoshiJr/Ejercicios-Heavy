# Ejercicio de los vuelos

# Declaración de Variables
numero = estatus = ""
hora = minuto = horaSalida = minutoSalida = acum = cont = 0
bandera = False

archivo = open("Vuelos.txt") # Abrimos el archivo.txt
print("{0:4}""{1:>15}""{2:>12}""{3:>15}".format("Numero","Hora Prog","Demora","Estatus"))
# Proceso
for linea in archivo: # con el for leemos las lineas del archivo

    columna = linea.split(",") # el .split lo que hace es tomar como columna lo que este separado por ","
    numero = columna[0] # columna en la posición 0 y asi sucesivamente
    hora = int(columna[1])
    minuto = int(columna[2])
    horaSalida = int(columna[3])
    minutoSalida = int(columna[4])

    aux1 = (hora * 60) + minuto
    aux2 = (horaSalida * 60) + minutoSalida
    demora = aux2 - aux1
    
    if  (demora == 0):
        estatus = "Salió a tiempo"
    elif (demora > 0):            
        estatus = "Salió tarde"
        acum += demora
        cont += 1
        if (bandera == False): # switch para capturar una sola vez y comparar el vuelo que salió más tarde
            bandera = True
            demoraTarde = demora
        elif (demora > demoraTarde):
            demoraTarde = demora
            numTarde = numero
            horaProgra = hora
            minutoProgra = minuto
    else:
        estatus = "Salió antes"
    print(" {0:4}""{1:>10}"":{2:>2}""{3:>13}""{4:<8}""{5:<10}".format(numero,hora,minuto,demora,"",estatus))
    
horaTarde=(acum/60)/cont
minutosTarde=(horaTarde*60)/cont
# Salida de datos
print("")
print(" Resultados")
print(" Tiempo promedio vuelos retardados:",round(horaTarde,2),"horas",round(minutosTarde,2),"Minutos")
print(" El vuelo con mayor retardo fue el:",numTarde,"con salida programada")
print(" a las",horaProgra,":",minutoProgra,"con",demoraTarde ,"minutos de retraso")
