# Programa: Reserva de Asientos de Cine (Matriz 3x4)
# Nombre del estudiante: Evelyn Cecibel Jácome Pillajo
# Objetivo: Permitir la reserva de un asiento específico e imprimir el estado actualizado de la sala.

# 1. Crear matriz de 3x4 inicializada en 0 (asientos libres)

asientos =[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],

]

# 2. Solicitar al usuario la fila y columna
print("--- Sistema de Reserva de Cine ---")
f = int(input("Ingrese fila (0 a 2):"))
c = int(input("Ingrese columna (0 a 3):"))

# 3. Marcar el asiento como reservado (1)
asientos[f][c] = 1

# 4. Imprimir el estado actual de la sala
print("\nEstado de la sala:")
for i in range(3):
    for j in range(4):

# 'end=" "' evita el salto de línea entre elementos de la misma fila
        print(asientos[i][j], end=" ")
        
# Imprime un salto de línea al terminar cada fila
    print()
