#while es para crear un ciclo y termina con el break 
while True:

    print ("-----Menu principal-----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    op= int(input("Ingrese el numero de la operacion a realizar: "))
#if y elif si uso solo if se va ejecitar todo, cuando uso elif se va ejecutar uno por uno
    if op== 1:
        n1= int(input("Ingrese un numero: "))
        n2= int(input("Ingrese otro numero: "))
        print(f"la suma es {n1+n2}")

    elif op== 2:
        n1= int(input("Ingrese un numero: "))
        n2= int(input("Ingrese otro numero: "))
        print(f"la resta es {n1-n2}")

    elif op== 3:
        n1= int(input("Ingrese un numero: "))
        n2= int(input("Ingrese otro numero: "))
        print(f"la multiplicacion es {n1*n2}")

    elif op== 4:
        n1= int(input("Ingrese un numero: "))
        n2= int(input("Ingrese otro numero: "))
        print(f"la division es {n1/n2}")
# las llaves se usa para hacer calculos matematicos en pyr
# f es para que no solo lea la cadena de texto, sino tambien para que haga la operacion matematica
    elif op== 5:
        print("Estas saliendo del programa")
        break
    else: 
        print("opcion incorrecta")