#!/usr/bin/python
# -*- coding: utf-8 -*-

x = int (input ("ingresa un número entero X \n"))
y = int (input ("ingresa un número entero Y \n"))
n = int (input ("ingresa un número entero N \n"))
z = x % y
w = x - y



if z==0 :
    print ("Es entero")
else :
    print ("No es entero")  #ej 1

if x > y :
    print ("X es mayor")
elif x < y:
    print ("Y es mayor")
else:
    print ("Son iguales") #ej 2

if x > y :
    print ("Pasaron " + str (w) + "años")
elif x < y:
    print ("Faltan " + str (-w) + "años")
else:
    print ("Estas en el año actual") #ej 3

if x > y > n:
    print (str(x) + " es mayor que " + str (y) + " y mayor que " + str (n))
elif y > x > n:
    print (str(y) + " es mayor que " + str(x) + " y mayor que " + str (n))
elif x > n > y:
    print (str(x) + " es mayor que " + str (n) + " y mayor que " + str (y))
elif y > n > x:
    print (str(y) + " es mayor que " + str(n) + " y mayor que " + str (x))
elif n > x > y:

    print (str(n) + " es mayor que " + str(x) + " y mayor que " +str(y))
elif n > y > x:
    print (str(n) + " es mayor que " + str(y) + " y mayor que " + str(x))
elif x == y == n:
    print ("Son iguales")
else:
    print ("vuelve a intentarlo perro") # ej 4


if x > y > n:
    print (x)
elif y > x > n:
    print (y)
elif x > n > y:
    print (x)
elif y > n > x:
    print (y)          #agregar si son iguales en el ej 5 y el ejercicio extra
elif n > x > y:
    print (n)
elif n > y > x:
    print (n)  # igaules 2
elif x == y == n:
    print ("Son iguales")
else:
    print ("vuelve a intentarlo perro") # ej 5


if (x > y and x > n):
    print ("El numero mayor es " + str (x))
else:
    if (y > x and y > n):
        print ("El numero mayor es " + str (y))
    else:
        print ("El numero mayor es " + str (n))
