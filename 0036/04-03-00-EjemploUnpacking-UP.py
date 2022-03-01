# Unpacking - desempaquetado
valores = 1,2,3
print(valores)
print(type(valores))

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

valor1, _, valor3 = 1, 2, 3
print(valor1, valor3)

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))

valor1, valor2, *valor3, valor4, valor5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(valor1, valor2, valor3, valor4, valor5)
print(type(valor3))

def regresa_varios_datos():
    return (1, 2, 3)

valor1, valor2, valor3 = regresa_varios_datos()
print(valor1, valor2, valor3)

valor1, *valores_restantes = regresa_varios_datos()
print(valor1, valores_restantes)

# help(str.partition)
hora, _, minutos = '17:20'.partition(':')
# print(type(variable))
print(hora, minutos)

