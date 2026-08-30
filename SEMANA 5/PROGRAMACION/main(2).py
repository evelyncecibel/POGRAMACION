def main():
 sistema_activo = True
 tiene_permiso = False

 if sistema_activo == True:
    if tiene_permiso == True:
      print("Acción ejecutada")
    else:
      print("Permiso denegado")
 else:
  print("Sistema inactivo")
 
main()  
