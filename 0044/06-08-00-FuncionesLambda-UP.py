# Funciones lambda
# Son funciones anónimas, y son pequeñas (una línea de código)

# No es posible asignar una función a una variable
# mi_funcion = def sumar(a, b): return a + b

# Con una función lambda( anónima, sin nombre, y una sola línea de código
# No se necesita agregar paréntesis para los parámetros
# No se necesita usar la palabra return, pero sí debe regresar una expresión
mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(4,6)
print(f'Resultado sumar con función lambda: {resultado}')