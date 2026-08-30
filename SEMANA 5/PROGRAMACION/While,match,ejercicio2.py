while True:
    calificacion = int(input("ingrese una calificacion del 1 al 5:"))

    match calificacion:
        case 1:
            print("Insuficiente")
        case 2:
            print("Regular")
        case 3:
            print("Bueno")
        case 4:
            print("Muy bueno")
        case 5:
            print("Excelente")
        case _:
            print ("calificacion no valida")
            break
