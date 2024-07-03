# Funciones con return (Retornar) solamente se ejecutan una unica vez.
# La funcion con return no devuelve un valor especifico

# Funcion sin return (Sin retornar)

def sumar_valores_sin_return(a: int, b: int):
    print(a + b)

sumar_valores_sin_return(1, 2)
sumar_valores_sin_return(5, 7)

resultado_obtenido_en_la_suma = sumar_valores_sin_return(2, 3)

print("*"*40)

print("Mostrar valor obtenido mediante la funcion sin return", resultado_obtenido_en_la_suma)

print("*"*40)

def sumar_valores_con_return(a: int, b: int):
    return a + b

# Invocando o llamando a la funcion con return y asignando el valor a una variable

resultado_obtenido_en_la_suma_con_return = sumar_valores_con_return(2, 3)

print("Mostrar valor obtenido mediante la funcion con return", resultado_obtenido_en_la_suma_con_return)