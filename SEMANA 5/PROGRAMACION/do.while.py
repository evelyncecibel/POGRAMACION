print("Tablas de multiplicacion")
print("Ingrese un numero, para mostrar la informacion")

numero = int(input("Escriba un numero: "))
contador = 1
while True:
    print (f"{contador} * {numero} = {contador * numero} ")
    #contador +=1
    contador = contador + 1
    if contador > 12:
     break