'''
list1 = [2,3,1,4,5]
list2 = ["A","B","C","D"]
list3 = ["Matematicas", "Historia", 1999,1998]
list4 = [list1,list2,list3]

print (list1)
print (list2)
print (list3)
print (list4)

for i in list3:
    print (type(i))
'''
list1 = [2,3,1,4,5]
frutas = ['naranja','manzana','pera','fresa','banana','manzana','kiwi']
print (frutas)

frutas.append('uva') #sumar uno mas
print ("APPEND")
print (frutas)

#frutas.extend(list1) #Suma de listas
#print  (frutas)

frutas.insert(0,'melon') #suma especifica
print ("INSTER1")
print (frutas)

frutas.pop(3) #Método de eliminación
print ("POP")
print (frutas)

frutas.remove("manzana") #Método de eliminación
print ("REMOVE")
print (frutas)

frutas.reverse() #Método de inversión de la lista
print ("REVERSE")
print (frutas)

frutas.sort() #ordena en str por alfabeto y numeros en orden
print ("SORT") #primero van las letras Mayusculas
print (frutas)

print ("COUNT")
print (frutas.count("manzana"))#Cuenta los numero de elemoentos de una pila

print ("INDEX")#Devuelve la posicion de donde se encuentra un elemento
print (frutas.index("manzana", 2)) #Con el segundo le dices desde donde quieres buscarlo, respeta la posicion de la lista
