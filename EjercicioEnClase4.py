print ("Ejercicio 1")
Palabras = int (input ("Cuantas palabras tiene la lista? \n"))

if Palabras < 1:
    print ("¡Imposible!")

else:

    List = []
    for i in range ( 1 , Palabras +1 ):
        Palabras1 = input("Ingresa la palabra " + str (i) + ": ")
        List.append(Palabras1)

    print (List)


print ("Ejercicio 2")

Palabras2 = input ("Que palabra quiere buscar? ")
popo = List.count(Palabras2)


print ("La palabra " + "''" + str(Palabras2)+ "''" + " aparece " + str(popo) + " veces en la lista.")


 #agregar todos a mayusculas y si la palabra no es la correcta, volver  A INTENTARLO

print ("Ejercicio 3")

Palabras4 = input ("Con que palabra quieres sustituirla? ")

for i in List:
    if i == Palabras2:
        posicion = List.index(i)
        List[posicion] = Palabras4

print ("La lista actual es: ", List )


print ("Ejercicio 4")

for i in range(len(List)):
    if List[i] == Palabras4:
        List[i] = None
print ("La lista actual es: ", List )

#para que no aparezca none, lo copiamos en una lista nueva
