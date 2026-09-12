def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

if __name__ == "__main__":
    precio_producto = 10
    cantidad_producto = 3
    resultado = calcular_total(precio_producto, cantidad_producto)
 
    print(f"El total a pagar es: ${resultado:.2f}")