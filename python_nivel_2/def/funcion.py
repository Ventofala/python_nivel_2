# Funciones en python
# las funciones son habitantes de primera clase
# Las fuciones estan conformadas por parametros y argumentos.

# Ejercicio sin funcion

nombre = "Cesar"
nombre2 = "Carlos"
nombre3 = "Jennifer"
nombre4 = "Pablo"
nombre5 = "Ramon"

print(f"hola, {nombre}")
print(f"hola, {nombre2}")
print(f"hola, {nombre3}")
print(f"hola, {nombre4}")
print(f"hola, {nombre5}")

print("*"*40)
# Palabra reservada (def) identificacion unica (parametro):

def saludo(name: str):
    print(f"hola, {name}")

# Invocar a la funcion = saludo("cesar") = invocar("argumentos")

saludo("Cesar")
saludo("Jennifer")
saludo("Carlos")
saludo("Pablo")

print("*"*40)

# Funcion sin parametros ni argumentos

def funcion_sin_parametros_ni_argumentos():
    print("Funcion sin parametros ni argumentos")

# Invocar o llamar

funcion_sin_parametros_ni_argumentos()

"""
Reto
1.- Crear una funcion que me permita sumar dos valores. Quiero que seas estricto con el tipado = el tipo de dato que debe recibir la funcion.
2.- Crear una fiesta tematica donde tienen que mostrar o imprimir el nombre del invitado y el personaje que esta disfrazado.
"""
print("*"*40)

def suma(num: int, num2: int):
    print(f"Primera suma, {num + num2}")

suma(2, 3)
suma(5, 7)

print("*"*40)

def invitado(invitado: str, disfraz: str):
    print(f"hola, {invitado} como {disfraz}")

invitado("Cesar", "Batman")

