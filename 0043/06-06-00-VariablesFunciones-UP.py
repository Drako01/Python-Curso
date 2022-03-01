# Las funciones en python son ciudadanas de primera clase
# First class citizens

# Definimos la función
def sumar(a, b):
    return a + b

# 1. Asignar una función a una variable (no se usan paréntesis)
mi_funcion = sumar

# Verificar el tipo de variable
print(type(mi_funcion))

# Llamamos la función a través de la variable
resultado = mi_funcion(5, 8)
print(f'Resultado: {resultado}')