asientos =[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],

]

f = int(input("Ingrese fila (0 a 2):"))
c = int(input("Ingrese columna (0 a 3):"))


asientos[f][c] = 1

print("\nEstado de la sala:")

for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
