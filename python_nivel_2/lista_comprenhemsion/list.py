# Una nueva forma para resumir un una linea una iteracion con una condicion

# Sin lista comprendida : [List compemhemsiom]
numeros = []
for item in range(1, 11):
    numeros.append(item)

print("Muestra lista de numeros del 1 al 10 ->", numeros)

print("*"*40)

numeros = []
for item in range(1, 11):
    numeros.append(item * 2)

print("Muestra lista de numeros del 1 al 10 multiplicado por 2 ->", numeros)

print("*"*40)
# Con lista comprendida (list comprehension)
# Estructura de la lista comprendida = [variable for almacenar in range(1, 11)]
'''
* variable: valores que va a almacenar
* for: El ciclo for.
* almacenar: es la variable que almacena los valores del ciclo.
* in: es el operador para el ciclo for
* range: rango de recorridos que va a hacer el ciclo.

'''

numeros_v2 = [item for item in range(1, 11)]

print("Lista comprendida ->", numeros_v2)

print("*"*40)
numeros_multiplicados = [item * 2 for item in range(1, 11)]

print("Lista comprendida con valores multiplicados por 2 ->", numeros_multiplicados)

print("*"*40)
# Ciclo sin lista comprendida (List comprenhension) con condicion
numeros = []
for item in range(1, 11):
    if item % 2 == 0:
        numeros.append(item) # => [2, 4, 6, 8, 10]
print("Lista normal con una condicion de numeros pares ->", numeros)

print("*"*40)

numeros = []
for item in range(1, 11):
    if item % 2 == 0:
        numeros.append(item * 2) # => [2, 4, 6, 8, 10]
print("Lista normal con una condicion de numeros pares multuplicados por 2 ->", numeros)

print("*"*40)

# Lista comprendida [Lint comprenhension]

numeros_comprendidos = [item for item in range(1, 11) if item % 2 ==0]
print("Lista normal con una condicion de numeros pares ->", numeros_comprendidos)

print("*"*40)

numeros_comprendidos = [item * 2 for item in range(1, 11) if item % 2 ==0]
print("Lista normal con una condicion de numeros pares multiplicados por 2 ->", numeros_comprendidos)

print("*"*40)

# Reto: hacer una lista comprendida (List comprehension) que muestre como resultado los paises que estan en la lista

lista_paises = ["portugal", "alemania", "italia", "francia"]
lista_pais = ["alemania", "italia"]

lista_normal_paises = []
for pais in lista_paises:
    if pais in lista_pais:
        lista_normal_paises.append(pais)
print("Reto ->", lista_normal_paises)

lista_comprendida_paises = [pais for pais in lista_paises if pais in lista_pais]
print("Reto comprendido ->", lista_comprendida_paises)

# Resumen
"""
1.- Las listas comprendidas (list comprehension) en Python son una forma concisa y legible de crear listas en una sola linea de codigo.
2.- La sintaxis basica seria: [variable ciclo for rango] = [item for item in range(1, 10)]
3.- La sintaxis compleja con operacion de multiplicacion seria: [variable * 2 ciclo for rango] = [item * 2 for item in range(1, 11)]
4.- La sintaxis con condicion seria: [variable ciclo for rango condicion] = [item for item in range(1, 11) if item % 2 == 0
"""
