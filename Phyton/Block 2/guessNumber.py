
while True:
  a=int(input("adivine el numero:"))
  numr=8-a
  nums=a-8
  if(a==8):
   print("ADIVINASTE")
  if (a<8):
    print("Te faltan:", numr)
  if(a>8) :
    print("Te sobran: ", nums)
  





