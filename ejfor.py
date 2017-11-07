print ("CONTADOR DE PARES E IMPARES")

x = int(input("Cuantos valores va a introducir"))

if x <= 0:
  print ("¡Imposible!")

elif x > 0:
    pares = 0
    for i in range (1,x + 1):
        y = int(input("Escriba el valor " + str (i) + ": "))

        if y % 2 == 0:
            pares += 1

    print ("Ha escrito " + str(pares) + " numeros pares y " + str(x - pares) + " numeros impares")
