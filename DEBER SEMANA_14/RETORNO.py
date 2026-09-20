
#Problema de la vida real:
#Calcular el precio total de una compra a partir del precio unitario
#de un producto y la cantidad comprada.


def calcular_precio_total(precio_unitario, cantidad):
     total = precio_unitario * cantidad
     return total
producto = "Cuaderno"
precio_unitario = 1.75
cantidad = 6

total_a_pagar = calcular_precio_total(precio_unitario, cantidad)
print("----- Resumen de compra -----")
print("Producto:", producto)
print("Precio unitario: $", precio_unitario)
print("Cantidad:", cantidad)
print("Total a pagar: $", total_a_pagar)

