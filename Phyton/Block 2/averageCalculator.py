print("3 calificaciones:")
calificacion1=int (input('1 calificación:'))
calificacion2=int (input('2 calificación:'))
calificacion3=int (input('3 calificación:'))

promedio=calificacion1+calificacion2+calificacion3/3

print("el promedio es: ", promedio)

if (promedio>=9):
  print("Conseguiste una medalla!")
if (promedio>=6):
  print("Aprobaste!")
if (promedio<6):
  print("Reprobaste!")
  