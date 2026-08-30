matriz = [
    [8,6,5],
    [1,2,3],
    [2,4,6]
]

lista= []
listamayoramenor = []
for fila in matriz:
    for columna in fila:
        lista.append (columna)
        listamayoramenor.append (columna)

print("valor inicial")
print (matriz)
print ("lista")
print (lista)
print ("-"*20)


for pf in range(len(lista)):
    for pc in range(pf+1, len(lista)):
        if lista [pf] > lista [pc]:
            aux=lista [pf]
            lista [pf] = lista [pc]
            lista [pc] = aux

print ("mayor a menor")
for pf in range(len(listamayoramenor)):
    for pc in range(pf+1, len(listamayoramenor)):
        if listamayoramenor [pf] < listamayoramenor [pc]:
            aux=listamayoramenor [pf]
            listamayoramenor [pf] = listamayoramenor [pc]
            listamayoramenor [pc] = aux

print ("lista menor a mayor")
print (lista)
print ("-"*20)

print ("lista mayor a menor")
print (listamayoramenor)
print ("-"*20)

posicion =0
for pf in range (3):
    for pc in range (3):
        matriz[pf][pc] = lista[posicion]
        posicion +=1

print("matriz ordenada")
print (matriz)
print ("lista")
print (lista)
print ("-"*20)




