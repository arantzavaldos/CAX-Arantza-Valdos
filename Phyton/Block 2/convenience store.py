print("Bienvenido a la tiendita de AvaMax!")
print("Ingrese su nombre")
nom=input()
print("Hola", nom)
print("Articulos a comprar:")

Art1=(input('Ingrese articulo 1: '))
Precio1=int(input('Ingrese precio: '))

Art2=(input('Ingrese articulo 2: '))
Precio2=int(input('Ingrese precio: '))

Art3=(input('Ingrese articulo 3: '))
Precio3=int(input('Ingrese precio: '))

Art4=(input('Ingrese articulo 4: '))
Precio4=int(input('Ingrese precio: '))

Art5=(input('Ingrese articulo 5: '))
Precio5=int(input('Ingrese precio: '))

suma=Precio1+Precio2+Precio3+Precio4+Precio5

subtotal=suma
iva= .16
impuesto=subtotal*iva
total=impuesto+suma

print('El total es:', total)

print('Ticket:')
print('La tiendita de AvaMax')
print(Art1,"$",Precio1)
print(Art2,"$",Precio2)
print(Art3,"$",Precio3)
print(Art4,"$",Precio4)
print(Art5,"$",Precio5)
print('SUBTOTAL:', subtotal)
print("TOTAL:", total)
