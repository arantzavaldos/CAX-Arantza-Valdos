while True:
  
  print("Menu de inicio")
  input()
  print("r = Reportes de fallas")
  print("o = Opcion a pago")
  print("p = Promociones")

  c = input("En que le podemos ayudar?")

  if (c=="r"):
    print("Reportes de falla")
    print("T= fallas de television")
    print("F= fallas de red")
    c = input ("Cual es su falla?")


    if (c=="T"):
      print("Fallas de television")
      print("6493")

    elif (c=="F"):
      print ("Fallas de red ")
      print("9265")

  elif (c=="o"):
    print ("opciones de pago")
    print ("pago con tarjeta de credito ")
    tarjeta = int(input("ingrese su numero de tarjeta:"))
    print ("Pago recibido! ")

  elif (c=="p"):
    print("Promociones del mes")
    print("Compra dos teles pequeñas a 5k! ")
    print("Le ponemos internet gratis si compra una television!")
    print("Si compra un telefono, te damos  unos audifonos!")


  

