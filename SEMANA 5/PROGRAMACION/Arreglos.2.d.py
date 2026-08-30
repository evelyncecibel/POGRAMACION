numero = [
#Posicion 0,1,2,3
    #columna, columna, columna, columna
    [1,2,3,4], #fila, posicion 0
    [5,6,7,8], #fila, posicion 1
    [9,10,11,12] #fila, posicion 2 
    
]
#Orden primero fila y despues columna
print(numero)
for fila in numero:
     for columna in fila:
      print(columna)
      print("-"*20)

