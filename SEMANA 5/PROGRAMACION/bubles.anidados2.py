lista_estudiantes = [
    ["Alejandro Morales", 18, "Qhari"],
    ["Ana Lucía Gómez", 19, "Warmi"],
    ["Carlos Eduardo Paredes", 18, "Qhari"],
    ["Daniela Sofía Castro", 20, "Warmi"],
    ["Diego Fernando Torres", 19, "Qhari"],
    ["Gabriel Alejandro Silva", 18, "Qhari"],
    ["Isabella Martínez", 21, "Warmi"],
    ["Javier Enrique López", 19, "Qhari"],
    ["José Luis Rodríguez", 20, "Qhari"],
    ["Juan David Benítez", 18, "Qhari"],
    ["Laura Camila Romero", 19, "Warmi"],
    ["Luis Alberto Mendoza", 22, "Qhari"],
    ["María Fernanda Delgado", 18, "Warmi"],
    ["Mateo Sebastián Aguirre", 19, "Qhari"],
    ["Natalia Isabel Ruiz", 20, "Warmi"],
    ["Paula Andrea Vargas", 18, "Warmi"],
    ["Ricardo Antonio Flores", 21, "Qhari"],
    ["Santiago Esteban Ortiz", 19, "Qhari"],
    ["Sofia Alejandra Navarro", 18, "Warmi"],
    ["Valeria Beatriz Salazar", 20, "Warmi"],
]
while True:
    print("-----Lista de Alumnos de primero B")
    print("---------Menu de opciones------")
    print("1.-listar todos los alumnos")
    print("2.-listar solo el nombre")
    print("3.-listar solo la edad")
    print("4.-Listar solo la edad")
    print("5-listar nombre y el sexo")
    print("6.Salir")
    op=int(input("Ingrese el numero de la opcion:"))

    if op==1:
        for estudiante in lista_estudiantes:
            print(estudiante)
    elif op==2:
        for estudiante in lista_estudiantes:
            print(estudiante[0])
    elif op==3:
        for estudiante in lista_estudiantes:
            print(estudiante[1])
    elif op==4:
        for estudiante in lista_estudiantes:
            print(f"Nombre: {estudiante[0]}\n" +
                  f"Edad: {estudiante[1]}")

    elif op==5:
            for estudiante in lista_estudiantes:
                print(f"Nombre: {estudiante[0]}\n" +
                      f"Sexo: {estudiante[2]}")

    elif op==6:
        print("muchas gracias por su visita")
        break
    else:
        print("la opcion ingresada no es la correcta")