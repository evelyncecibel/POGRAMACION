matriz = [
   [2, 4, 6],
   [1, 3, 5],
   [7, 8, 9]
]
vb=4
for fila in matriz:
    for columna in fila:
        if columna == vb:
            print (f"valor encontrado {vb}")

