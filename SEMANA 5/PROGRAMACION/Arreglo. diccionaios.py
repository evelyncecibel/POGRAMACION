#diccionarios
lista_estudiantes =[{
    "nombre": "Luis",
    "apellido": "Llerena",
    "edad": "29",
    "estatura": "1.75",
     "estado": "soltero"
}]

otro_estudiante ={
    "nombre": "Luis",
    "apellido": "Llerena",
    "edad": "29",
    "estatura": "1.75",
     "estado": "soltero"
}
lista_estudiantes.append (otro_estudiante)
for estudiante in lista_estudiantes:
    print (estudiante)


# se usa esto si quiero solo un dato:
# print (lista_estudiantes ["nombre"])

#se imprime con la palabra clave:
#clave: nombre y el valor Luis
#clave: apellido y el valor Llerena
#clave: edad y el valor 29
#clave: estatura y el valor 1.75
#clave: estado y el valor soltero

#for clave, valor in lista_estudiantes.items():
    #print (f"clave: {clave} y el valor {valor}")

#sacar solo el valor:
#Luis
#Llerena
#29
#1.75
#soltero

#for valor in lista_estudiantes.values():
#    print(valor)

#sacar las claves

#for valor in lista_estudiantes:
 #   print(valor)