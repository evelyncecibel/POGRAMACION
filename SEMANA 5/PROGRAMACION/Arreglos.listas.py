#Arreglo unidimensional (una sola fila)
#listas ()
#.append=agregar
#.pop=eliminar
#                 1        2          3           4         5
Dias_semana = ["Lunes", "Martes", "Mercoles", "Jueves", "Viernes"]

print("Impresion del arreglo Inicial")

print(Dias_semana)

print("Agregar el sabado")
Dias_semana.append ("sabado")
print(Dias_semana)

print("Agregar el domingo")
Dias_semana.append ("domingo")
print(Dias_semana)

print("Modificar el error del miercoles")
Dias_semana [2] = "Miercoles"
print(Dias_semana)

print("eliminar")
print(Dias_semana.pop(2))
print(Dias_semana)