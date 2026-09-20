matriz = [
 
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]

#se usa cuando fila y columa es la misma para 1 es [0,0], para 5 es [1,1] para 9 es [3,3]
sumadiagonalprincipal = 0

for pf in range(len(matriz)):
    sumadiagonalprincipal += matriz[pf][pf]

print(sumadiagonalprincipal)

#se usa cuando el uno sube y el otro baja   