#Están compuestos por más de un tipo de dato simple u otros datos compuestos

#LISTA --> pueden modificarse
list = ["Franco", "francogarcia", 1.68, False]
print(list)
print(list[1])

#TUPLA --> no pueden modificarse
tupla = ("Franco", "francogarcia", 1.68, False)
print(tupla)
print(tupla[2])

#Las tuplas no pueden ser modificadas
#tupla[1] = "Bernardo" --> no puede hacerse
#lista[1] = "Bernardo" --> puede hacerse

#creando un conjunto (set) --> los elementos están desordenados y pueden cambiar.
#No se puede modificar un elemento en particular, al igual que en las tuplas.
#El conjunto puede redefinirse completamente.
#No se puede acceder por el índice a un elemento del conjunto.
#No permite repetir valores
conjunto = {"Franco", "francogarcia", 1.68, False}#output --> {"Franco", "francogarcia", 1.68, False}
conjunto = {"Franco", "francogarcia", 1.68, False, "Franco"} #output --> {"Franco", "francogarcia", 1.68, False}
#print(conjunto[2]) --> no puede acceder al elemento, operación inválida

#DICCIONARIO (dict), es como un json en javascript
#Tienen una estructura key: value | clave: valor , separados con comas, debe haber n-1 comas, siendo n la cant de elementos
diccionario = {
    'nombre': 'Franco',
    'edad': 21,
    'carrera': 'Informatica',
    'dato_duplicado': 'Franco' 
}
#No se utiliza un indice, se utiliza la clave que se quiere mostrar
print('diccionario nombre: ' + diccionario['nombre']) 
