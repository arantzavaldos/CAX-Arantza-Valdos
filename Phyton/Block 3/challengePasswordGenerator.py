import random
#agregar el resto del abecedario

#volver el codigo infinito usandoun while True
base="abcdefghijklmnopqrstuvwxyz"





#permite que el usuario seleccione la longitud de su 
#password
while True:
  l=int(input('escoga la longitud:'))
  passw=""
  for i in range (l):
    passw=passw+random.choice(base)

  print("password ", passw)
  
  input()
  
#punto extra al que logre ademas que el usuario decida cuantas contraseñas desea generar