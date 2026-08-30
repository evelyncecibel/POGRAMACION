n1=int(input("Ingrese la calificaion 1:"))
n2 = int(input("Ingrese la calificaion 2:"))
n3 = int(input("Ingrese la calificaion 3:"))
promedio =(n1+ n2 + n3)/3

print ("Nota 1:", n1)
print ("Nota 3:", n3)

print("Promedio:",promedio)
      
       
if  n1>n2 and n1>n3:
    print("la calificacion 1 es mayor")
    print ("Nota final:", promedio + 1)
elif n2>n1 and n2>n3:
    print ("la calificacion 2 es mayor")
    print ("Nota final:",promedio + 0.5)
else:
    print ("la calificacion 3 es mayor")
    print ("Nota final:",promedio)

asistencia = input ("ingrese el numero de faltas:")
#        true           true
if promedio < 7 and asistencia>= 4:
    print("esta perdido en faltas y promedio")
#        true            false
elif promedio < 7 or asistencia>= 4:
    print("esta perdido en faltas o promedio")
else: ("paso el nivel")


