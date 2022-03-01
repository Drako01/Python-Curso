# * desempaquetar
numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

# Desempaquetando al momento de pasar un parámetro a una función
def sumar(a, b, c):
    print(f'Resultado suma: {a + b + c}')

sumar(*numeros)
