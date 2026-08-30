# en pyton no se usa switch sino el match
while True:
    print ("-----Menu principal-----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    op= (input("Ingrese el numero de la operacion a realizar: "))
    op = op.lower()
    # para minusculas lower y para mayusculas op = op.upper()
    match op:
        case "suma":
            n1= int(input("Ingrese un numero: "))
            n2= int(input("Ingrese otro numero: "))
            print(f"la suma es {n1+n2}")

        case "resta":
            n1= int(input("Ingrese un numero: "))
            n2= int(input("Ingrese otro numero: "))
            print(f"la resta es {n1-n2}")

        case "multiplicacion":
            n1= int(input("Ingrese un numero: "))
            n2= int(input("Ingrese otro numero: "))
            print(f"la multiplicacion es {n1*n2}")
        case "division":
            n1= int(input("Ingrese un numero: "))
            n2= int(input("Ingrese otro numero: "))
            print(f"la division es {n1/n2}")
        case "salir":
            print("has salido del programa")
            break
            
            
        case _:
            print ("opcion incorrecta")



