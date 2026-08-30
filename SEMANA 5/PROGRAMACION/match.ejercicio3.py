print ("-----Boleteria de cine----")
print ("1. Niño")
print ("2. Adulto")
print ("3. Adulto mayor")

tipo_cliente= int(input("ingrese el numero de la opcion:"))
match tipo_cliente:
    case 1:
        cliente = print("Niño")
        precio_base = 4
    case 2:
          cliente = print ("Adulto")
          precio_base = 7
    case 3:
        cliente = print ("Adulto mayor")
        precio_base = 5
    case _:
          print ("cliente no valido")


print ("ingrese el dia de la semana: ")
print ("1. lunes")
print ("2. martes")
print ("3. miercoles")
print ("4. jueves")
print ("5. viernes")
print ("6. sabado")
print ("7. domingo")

dia = int(input("Ingrese el numero de dia: "))
match dia:
     case 1:
          dia = "lunes"
          descripcion = "sin desceuntos"
     case 2:
          dia = "martes"
          descripcion = "sin desceuntos"
     case 3:
          dia = "miercoles"
          precio_base= precio_base -2
          descripcion = "desceunto de 1 USD"
     case 4:
          dia = "jueves"
          descripcion = "sin desceuntos"
     case 5:
          dia = "viernes"
          descripcion = "sin desceuntos"
     case 6:
          dia = "sabado"
          precio_base = precio_base + 1
          descripcion = "incremento de 1 USD"
     case 7:
          dia = "domingo"
          precio_base = precio_base + 1
          descripcion = "incremento de 1 USD"

print ("----detalle de la entrada---")
print(f"Tipo_cliente: {tipo_cliente}")
print (f"Dia:{dia}")
print(f"Precio: {precio_base}")
print(f"Descripcion: {descripcion}")
     
     






