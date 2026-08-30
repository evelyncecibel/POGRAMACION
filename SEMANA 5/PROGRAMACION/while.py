print("Tablas de multiplicacion")
print("Ingrese un numero, para mostrar la informacion")

numero = int(input("Escriba un numero: "))
contador = 1
while contador < 12:
    print (f"{contador} * {numero} = {contador * numero} ")
    #contador +=1
    contador = contador + 1
    
    