Matriz = [
   [2, 4, 6],
   [1, 3, 5],
   [7, 8, 9]
]

#que sea manual (cuando cambias el numero manual y en no automatico)

#print ("valor inicial")
#print (Matriz[1][1])

#print ("valor final")
#Matriz[1][1]=55
#print (Matriz[1][1])

#DE FORMA DINAMICA
#solo de lectura
#for fila in Matriz:
#   for columna in fila:
#        if columna == 5:
#            columna = "cinco"
#print (Matriz)


#DE FORMA DINAMICA
#pf es posicion de filas
#pc es posicion de columnas
#for pf in range (len(Matriz)):
#    for pc in range (len(Matriz[pf])):
#        if Matriz [pf] [pc] ==5:
#            Matriz[pf] [pc] = "cinco"
#print (Matriz)


for fila in Matriz:
    print (fila)
