#se crea un diccionario con '{}', se divide mediante
#comas, se pueden agregar diccionarios en diccionarios y todo tipo

diccionario = { 'nombre': 'Carlos', 'edad' : 22, 'cursos':
['Python', 'Django']}
'''
print (diccionario)
print (diccionario['nombre']) #mandar llamar un elemento de la lista
print (diccionario['edad'])
#mandar llamar un elemento de la lista que esta dentro de un diccionario
print (diccionario['cursos'][0])
'''

#Otra forma de hacer diccionarios
dic = dict (nombre = 'Jorge', apellido = 'Sanchez', edad = 22)
print (dic)
print (dic['nombre'])


#Iterar en un diccionario
for key, value in diccionario.items():
    print  (key + ':' + str(value))

lista_cursos = diccionario ['cursos']
lista_cursos.append('Java')
print (lista_cursos)
print (diccionario)

#Número de elementos que tiene el diccionario
print (len(diccionario))

#Imprimir las llaves
print (diccionario.keys())

#Imoprimir valores
print (diccionario.values())


#Si no existe un valor, dame un valor por Default, que seria el que esta despues
#de la coma en este caso Juanito
print (diccionario.get("nombree", "Juanito"))

#Agregar elemento al diccionario con su clave : valor
diccionario['key']= 'value'
print (diccionario)

#eliminar un elemento, pero aqui no hay orden, por lo tanto se necesita poner cual quieres
#borrar
diccionario.pop('key')
print (diccionario)

#Duplicar diccionario
diccionario2 = diccionario.copy()
print (diccionario2)

#Añade elementos de un diccionario a otro
diccionario.update(dic)
print (diccionario)
