# La manera de crear conjunto de datos en python

set_paises =  {"venezuela", "colombia", "chile", "hondura"}
print("ESto es un set en python -> ", set_paises)

set_numeros = {2, 4, 6, 8, 10}
print("ESto es un set en python -> ", set_numeros)

set_difetentes_datos = {"Hola", 1, False, 1.1}
print("ESto es un set en python -> ", set_difetentes_datos)

# Conversion de un tipo de datos a un set

valor_string = set("Hola Mundo")
print("Esta es una conversion de string a set -> ", valor_string)

# Conversion de un tipo de dato numerico a un set
set_tupla = set((2, 3, 4, 5, 6, 7))
print("Esta es una conversion de numero a set -> ", set_tupla)

# Conversion de un tipo de dato numerico a un set
set_lista = set([2, 3, 4, 5, 6, 7])
print("Esta es una conversion de lista a set -> ", set_lista)

# Que pasaria si tenemos elementos duplicados
set_lista_duplicado = set([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 10, 10])
print("Esta es una conversion de numero de lista duplicado a set -> ", set_lista_duplicado)

# Reto: Quiero que elimines los valores de una lista repetidos y quiero que el tipo de dato no sea modificado y que sea una lista
lista_duplicado = [1,1,1,1,1,1, 2, 3,3,3, 4,4, 5,5,5,5, 6, 7, 8, 9,9,9, 10, 10]
#lista_modificada = list(set(lista_duplicado))
#print(lista_modificada)
#print(type(lista_modificada))

#lista_modificada = set(lista_duplicado)
#lista_modificada = list(lista_modificada)
#print(lista_modificada)
#print(type(lista_modificada))

# Resumen:
# 1.- SET no tiene una jerarquia de los datos = No tiene un orden en especifico.
# 2.- SET no acepta valores repetidos = Si hay valores repetidos los elimina y deja un solo valor.