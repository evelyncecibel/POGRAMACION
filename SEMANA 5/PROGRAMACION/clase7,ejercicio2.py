nombre = input("Ingrese el nombre del estudiante: ")
nota= input ("ingrese la nota: ")
faltas = input (int("Ingrese las faltas de estudiante: "))
 
if nota >= 7 and faltas <=8:
    print ("pasa el nivel")
else:
    print ("pierde el nivel")


if nota >= 7:
    if faltas <= 8:
        print ("paso el nivel")
    else: 
        ("pierde por faltas")
else:
    ("pierde por calificaciones")
#Puede ser de las dos formas usando and primer casp o segundo caso if y else