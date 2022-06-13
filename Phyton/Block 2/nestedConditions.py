#nested conditions

mensaje=input("escribe hola:   ")
#!= es diferente
if(mensaje!="hola"):

  if(mensaje=="HOLA"):
    print("no sabe leer, es hola")
    mensaje=input("intentelo nuevamente")

    if(mensaje=="HOLA"):
       print("y con todo y eso no aprende a leer")
    
  elif(mensaje=="Hola"):
    print("se agradece una persona muy letrada, pero aprenda a leer, dije hola")

  elif(mensaje=="hOLA"):
    print("desactive el bloq mayus")
          
  else:
      print("enserio....?")      
          
  
elif(mensaje=="hola"):                   print("que agradable sujeto")
