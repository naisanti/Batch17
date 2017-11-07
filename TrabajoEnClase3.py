print ("Ejercicio 1")
numeros = []
for i in range (1, 101):
    numeros.append(i)

print (numeros)



print ("Ejercicio 2")

num_pedido = int(input("Ingresa un número: "))
mult =[]

for i in range (1,11):
     mult = i * num_pedido

     print (mult)



print ("Ejercicio 3")

List1 = [4,76,3,12,65,3]
List2 = [234,222,523,65]

List1.extend(List2)

total = 0

for i in List1:
    total += i

print ("El resultado es: " + str(total))
