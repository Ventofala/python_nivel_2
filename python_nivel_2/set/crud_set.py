"""
CRUD = 
Create -> crear. 
Read -> leer. 
Update -> actualizar. 
Delete -> eliminar
"""

set_paises =  {"venezuela", "colombia", "chile", "hondura"}

# Metodos de los set

# Tamano de un conjunto o set
size_set = len(set_paises)
print("El metodo len me permite saber la longitud de un set -> ", size_set)

# Saber si hay o no un elemento dentro del conjunto o set
print("Brasil esta en nuestro set? ->", "brasil" in set_paises)
print("Chile esta en nuestro set? ->", "chile" in set_paises)

print("*"*40)

# Agregar un nuevo elemento a nestro conjunto o set -> CREATE
set_paises.add("venezuela") # -> Esto no va a afectar a nuestro conjunto o set
set_paises.add("brasil") # -> Esto si va a afectar a nuestro conjunto o set
set_paises.add("argentina") # -> Esto si va a afectar a nuestro conjunto o set
set_paises.add("colombia") # -> Esto no va a afectar a nuestro conjunto o set
print("Conjunto o set mutado, modificado su valor original ->", set_paises)

print("*"*40)

#Modificar los conjuntos o set -> UPDATE
set_paises.update({"uruguay", "bolivia"})
print("Conjunto o set mutado, actualizado su valor original ->", set_paises)
set_paises.update(["canada", "rusia"])
print("Conjunto o set mutado, modificado su valor original ->", set_paises)
"""
set_paises.update("canada", "rusia")
print("Conjunto o set mutado, modificado su valor original ->", set_paises)

"""
print("*"*40)

# Eliminar o descartar elementos que esten dentro de nuestro conjunto o set
set_paises.remove("rusia")
print("El metodo remove quita un elemento del conjunto o set ->", set_paises)

# El elemento a eliminar debe estar en el conjunto o set!!!

print("*"*40)

# Para evitar que la aplicacion se detenga por completo, vamos a utilizar un metodo que me permite descartar el error
set_paises.discard("rusia")
print("El metodo discard quita un elemento del conjunto o set y evita que se detenga la aplicacion por no encontrar el valor ->", set_paises)

print("*"*40)

# El metodo clear me permite limpiar todo un conjunto o set
set_paises.clear()
print("Conjunto o set vacio -> ", set_paises)
print("longitud actual de nuestro conjunto o set -> ", len(set_paises))

#Resumen
"""
1.- Los conjuntos o SET tienen longitud o un tamaño.
2.- Los conjuntos o SET pueden se iterados con el operador "in".
3.- Podemos agregar un nuevo valor a nuestro conjunto o SET "add".
4.- Podemos actualizar su tamaño original de un conjunto o SET "update".
5.- Podemos eliminar o remover elemento de un conjunto a SET "remove".
6.- Podemos descartar el error que ocurre cuando el elemento no existe en nuestro conjunto o SET "discard"
7.- Podemos dejar vacio o limpiar un conjunto o SET "clear". 
  
"""