#hola_Ernesto

#mundo = 30
#exponente =8
#resultado = mundo%exponente
#print ("el resultado es: "+ str(resultado))



#print ("""dd
#dd
#ddd
#""")

#nombre = 3 == 5
#print(nombre, type(nombre))


#palabra = input("introduce una palabra: ")
#num_int = int(input("introduce un numero entero: "))
#num_float = float(input("introduce un numero flotante: "))
#num_complex = complex(input("introduce un numero complejo: "))

#print ("string", palabra)
#print ("flotante", num_float)
#print ("complejo", num_complex)


#nombre = "eeeeEEE" 
#print(f"hola {nombre.capitalize()}")

#precio = 5.4566666
#print(f"el precio es: {precio: .3f}")

#nombre = (input("cual es tu nombre"))
#print (f"hola {nombre} vamos a realizar una suma")

#numerouno =int(input("escribir el primer valor: "))
#numerodos =int(input("escribir el segundo valor: "))

#resultado =numerouno + numerodos
#print (f"{nombre} eel resultado es: {resultado}")

#numero = 5
#if numero ==0:
#    print("el numero es 5")

#print("fin")



#numero = 0

#if numero == 5:
#    print ("el numero es 5")
#else:
#    print ("el numero no es 0")
#print ("fin")

#nombre = input ("cual es tu nombre: ")

#matematicas = int (input ((f"{nombre} cual es tu calificacion en matematicas: ")))
#quimica =int ( input ((f"{nombre} cual es tu calificacion en quimica: ")))
#biologia =int (input ((f"{nombre} cual es tu calificacion en biologia: ")))

#resultado = (matematicas + quimica + biologia)/3
#if resultado > 7:
#    print (f'felicidades {nombre} "aprobaste" con un promedio de: {resultado: .2f}')


#else:
#    print (f'lo sentimos {nombre} "no everaprobaste" con un promedio de: {round(resultado,2)}')
    
#    print("fin")




#------Sentencias condicionales múltiples en Python (elif)-------------------------------------------

#print ("Convertidos de numeros a letras")

#numero = int(input("cual es el numero que deseas convertir: "))

#if numero == 1:
#    print('el numero es "uno"')

#elif numero == 2:
#    print('el numero es "dos"')

#elif numero == 3:
#    print('el numero es "tres"')

#elif numero == 4:
#    print('el numero es "cuatro"')
#elif numero == 5:
#    print('el numero es "cinco"')

#else:
#    print("el numero se desconoce")

#print("fin")
    

#----------------Sentencias condicionales anidadas en Python----------------------------------    

#print("menu de opciones \n")
#print("preciona 1 para convertir de numero a palabra.")
#print("preciona 2 para convertir de palabras a numeros.\n")

#opciones =(int(input("Cual es tu opcion deseada: ")))

#if opciones ==1:
#    print("\nconversor de numeros a palabras\n")
#    opcion_1 =(int(input("Cual es el numero que desea convertir a palabra: ")))

#    if opcion_1 ==1:
#        print("el numero es 'uno'")
#    elif opcion_1 ==2:
#        print("el numero es 'dos'")
#    elif opcion_1 ==3:
#        print("el numero es 'tres'")
#    elif opcion_1 ==4:
#        print("el numero es 'cinco'")
#    elif opcion_1 ==5:
#        print("el numero es 'cinco'")
#    else:
#        print("el numero no esta registrado")


#elif opciones ==2:
#    print("\nconversor de palabras a numeros\n")

#    opcion_2 =(input("Cual es ella palabra que desea convertir a numero: "))
#    opcion_2 = opcion_2.lower ()
#    if opcion_2== "uno":
#          print("el numero es '1'")

#    elif opcion_2 == "dos":
#        print("el numero es '2'")
#    elif opcion_2 == "tres":
#        print("el numero es '3'")
#    elif opcion_2 == "cuatro":
#        print("el numero es '4'")
#    elif opcion_2 == "cinco":
#        print("el numero es '5'")
#    else:
#        print("el numero no esta registrasdo")
          
#else:
#     print("opcion no disponible")
#print("fin")


#-----------------------------Operadores relacionales en Python----------------------------------------
#print("introducir dos numeros a comparar")

#numero_uno =int(input("introduce el primer numero: "))
#numero_dos = int(input("introduce el segundo numero: "))

#print(f"los numeros comparados son {numero_uno} y {numero_dos}")
#if numero_uno == numero_dos:
#    print ("es igual")
#if numero_uno != numero_dos:
#    print("es diferente")
#if numero_uno > numero_dos:
#    print("es mayor")
#if numero_uno < numero_dos:
#    print("es menor")
#if numero_uno >= numero_dos:
#    print("es mayor o igual")
#if numero_uno <= numero_dos:
#    print("es maenor o igual")


#--------------------Operadores lógicos en Python---------------------------------------
#CONJUNCION (AND)
#print("conjuncion (and)")
#num_uno =int(input("escribir un numero mayor a 2 y menor a 5: "))
#if num_uno >5 and num_uno <5:
#    print(f"el numero {num_uno} cumple con la condicion./n")
#else:
#    print(f"el numero {num_uno} no cumple con la condicion./n")

#DISYUNCION OR
#palabra = input ("escribir la palabra yes o si")
#palabra = palabra.lower()
#if palabra == "yes" or palabra =="si":
#    print("la condicion se ha cumplido")
#else:
#    print("la condicion no se ha cumplido")

#NEGACION
#print ("negacion (not)")

#num_uno =int(input("introduce un numero igual a 5: "))
#if not num_uno== 5:
#    print("el numero es diferente a 5 y si se cumple la condicion")
#else:
#    print ("el numero es 5 y no cumple la condicion") 

#---------------------EJERCICIO PRACTICO 1------------------------------------
#print("Sistema de vacacion de RAPPIT")

#nombre = input("introducir su nombre: ")

#clave = int (input("introducir el numero de clave de su  departamento: "))

#antiguedad =int ( input("años de trabajo: "))
#if clave == 1:
#    if antiguedad == 1:
#        print(f"{nombre} recibe 6 dias de vacaciones")
#    elif antiguedad > 2 and antiguedad <= 6:
#        print(f"{nombre} recibe 15 dias de vacaciones")
#    elif antiguedad >= 7:
#            print(f"{nombre} recibe 22 dias de vacaciones")
#    else: 
#         print(f"{nombre} no cumple con los años solictados para las vacaciones")

#elif clave == 2:
#    if antiguedad == 1:
#        print(f"{nombre} recibe 7 dias de vacaciones")
#    elif antiguedad == 2 and antiguedad <= 6:
#        print(f"{nombre} recibe 15 dias de vacaciones")
#    elif antiguedad >= 7:
#            print(f"{nombre} recibe 22 dias de vacaciones")
#    else: 
#         print(f"{nombre} no cumple con los años solictados para las vacaciones")

#elif clave == 3:
#    if antiguedad == 1:
#        print(f"{nombre} recibe 10 dias de vacaciones")
#    elif antiguedad == 2 and antiguedad <= 6:
#        print(f"{nombre} recibe 20 dias de vacaciones")
#    elif antiguedad >= 7:
#            print(f"{nombre} recibe 30 dias de vacaciones")
#    else: 
#         print(f"{nombre} no cumple con los años solictados para las vacaciones")


#else:
#    print ("clave incorrecta")

#---------------------EJERCICIO PRACTICO 2------------------------------------
#print("el programa determina si un numero es par o impar")

#numero_uno = int(input("por favor introducir un numero entero: "))

#if numero_uno  % 2 == 0:
#    print("el numero es par")
#elif numero_uno  % 2 == 1:
#    print("el numero es impar")
#else:
#    print("opcion no correcta")

#---------------------EJERCICIO PRACTICO 3------------------------------------
#print("programa para determinar cual es el numero mas grande de los tres numeros")

#num_uno = int(input("introducir el primer numero: "))
#num_dos = int(input("introducir el segundo numero: "))
#num_tres = int(input("introducir el tercer numero: "))

#if num_uno > num_dos and num_uno > num_tres:
#    print (f"{num_uno} es mayor")
#if num_dos > num_uno and num_uno > num_tres:
#    print (f"{num_dos} es mayor")
#if num_tres > num_uno and num_uno >num_dos:
#    print (f"{num_tres} es mayor")



#---------------------Operadores de asignación------------------------------------
#nombre = "Hola "
#nombre += input("escribe tu nombre")

#print(nombre, "esto es el incremento y decremento de una variable")
#print("incremento o aumento")

#x=1
#print("el valor inicial de x es: ", x)

#x+= 1

#x+= 1

#x+= 1

#x+= 1
#print(f"el valor de x es: {x}")

#print("decremento o dismunucion")

#print(f"el valor inicial de x es: {x}" )

#x-=1
#x-=1
#x-=1
#x-=1

#print(f"el valor final de x es: {x}")

#---------------------Ejercicio práctico #4 ------------------------------------

#print ("-"*20)
#print ("Menu de opciones")
#print("-"*20)

#print("1. suma")
#print("2. resta")
#print("3. multiplicacion")
#print("4. division")
#print("5. division entera")
#print("6. exponente")
#print("7. modulo o resta")

#numero = (int(input(f"introduce la opcion deseada: ")))

#if numero == 1:
#    print("eleguste la suma")
#    numero= (int(input("introduce en primer numero: ")))
#    numero+= (int(input("introduce en segundo numero: ")))
#    print(f"el resultado es: {numero}")

#elif numero == 2:
#    print("eleguste la resta")
#    numero= (int(input("introduce en primer numero: ")))
#    numero-= (int(input("introduce en segundo numero: ")))
#    print(f"el resultado es: {numero}")

#elif numero == 3:
#    print("eleguste la multiplicacion")
#    numero= (int(input("introduce en primer numero: ")))
#    numero*= (int(input("introduce en segundo numero: ")))
#    print(f"el resultado es: {numero}")

#elif numero == 4:
#    print("eleguste la division")
#    numero= (float(input("introduce en primer numero: ")))
#    numero/= (float(input("introduce en segundo numero: ")))
#    print(f"el resultado es: {numero:.2f}")

#elif numero == 5:
#    print("eleguste la division entera")
#    numero= (int(input("introduce en primer numero: ")))
#    numero//= (int(input("introduce en segundo numero: ")))
#    print(f"el resultado es: {numero:.2f}")

#elif numero == 6:
#    print("eleguste la division entera")
#    numero= (int(input("introduce en primer numero: ")))
#    numero**= (int(input("introduce en segundo numero: ")))
#    print(f"el resultado es: {numero}")

#elif numero == 7:
#    print("eleguste modulo o resto")
#    numero= (int(input("introduce en primer numero: ")))
#    numero %= (int(input("introduce en segundo numero: ")))
#    print(f"el resultado es: {numero}")

#else:
#    print("opcion incorrecta")

#--------------------- Los parámetros end y sep ------------------------------------

print("1","2","3","4", sep=",")
#--------------------- Bucle o ciclo while ------------------------------------