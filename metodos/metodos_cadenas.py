cadena1 = "Hola como estas"
cadena2 = "Bienvenido"

#print(dir(cadena1)) #dir --> es una función, devuelve la lisat de atributos válidos del objeto pasado por parámetro

resultado = cadena1.upper()
#print(resultado)


#estructura --> dato.metodo()

#upper --> convierte un dato a mayúscula

#lower --> convierte todo a minúscula

#capitalize --> convierte la primer letra a mayúscula

#find --> nos permite buscar un valor dentro de una cadena, puede ser una palabra o un caracter
#devuelve la posición del valor buscado, o -1 si el mismo no se encuentra en la cadena.

#index --> funciona igual que find, pero si no encuentra en valor buscado, devuelve un error (excepción).

#dato.isNumeric() --> devueleve true si el dato es numérico

busqueda = cadena1.find("Hola")
print(busqueda)

#dato.isAlpha() --> devuelve true si es alfanumerico, devuleve true si y solo si la cadena tiene solamente
# letras, con que haya un caracter especial, un espacio, etc, ya devuelve false.

#dato.count() --> nos dice cuantas veces hay una coincidencia dentro de una cadena. Si no encuentra nada, devuelve 0

#dato.len() --> devuelve la cantidad de caracteres que tiene una cadena.

#cadena.startswith("parametro") --> devuelve true si la cadena inicia con el valor pasado por parámetro.

#cadena.endswith("parametro") --> devuelve true si la cadena termina con el valor pasado por parámetro.

#cadena_nueva = cadena.replace("lo_q_quiero_reemplazar", "valor_nuevo") --> reemplaza un pedazo de la cadena dada, por otra.
# ambas cadenas son pasadas por parámetro.

#cadena.split("parametro") --> separa una cadena utilizando la cadena pasada como parametro
cadena = "hola,como,estas"
cadena.split(",") #resultado => ["hola","como","estas"]
