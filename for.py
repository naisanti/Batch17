
'''
var = "HOLA"

for i in  var:
    print ("La letra que toma i es: " + i)

print ("ACABE")

for i in range (11):
    print (i)

print ("Multiplo de dos ")
cuenta = 0
for i in range (1,100):
    if i % 2 == 0:
        cuenta +=1     # cuenta = cuenta + 1

print (cuenta)


print ("Acumulador")
suma = 0
for i in range (1,10):
    print (i)
    suma = suma + i
    print ("Resultado: ", suma)



print ("Ejercicio 1:")
for i in range (1,10001):
    print (i)

print ("Ejercicio 2:")
for i in range (1,10001):
    if i % 2 == 0:
        print (i)


print ("Ejercicio 3:")
var = "ELEFANTE"
pal=0
for i in var:
    if i == "E":
        pal += 1
        print (pal)

print (pal)


print ("Ejercicio 3:")
var = "ELEFANTE"
pal=0
for i in var:
    if i == "E":
        pal += 1
        if pal == 3:
            print ("Esta es la tercera E: " + str(pal))

print (pal)
'''

p = int (input ("ingresa un precio"))
q = int (input("ingresa la cantidad"))

sin_descuento= p * q

cant = 0
if (q<=0 or p <= 0):  #dos condiciones
    print ("Vuelve a Intentarlo")

elif q > 5:
    descuento = (((q * 5)/100) * q)
    precio_real = ((p *q)-descuento)
    print ("Tu precio es: " + str(precio_real) + "y tu descuento fue de: " + str(descuento))
else:
    print ("no hay descuento, tu precio es: " + str (sin_descuento))
