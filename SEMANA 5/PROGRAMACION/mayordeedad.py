edad= int (input("ingrese la edad:"))
tiene_entrada = bool (input ("tiene la entrada (true/false):"))
permiso_especial = bool (input ("tiene la entrada (true/false):"))
#                 false
#     true               false                      false 
if (edad>=18 and tiene_entrada==True) or permiso_especial==True:
    print ("puede entrar")
else:
    print ("no puede entrar")


