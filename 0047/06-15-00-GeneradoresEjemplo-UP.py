# Generador de números del 1 al 5
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print('Se reanuda la ejecución de la función')

# Utilizamos el generador
generador = generador_numeros()
print(f'Objeto generador: {generador}')
print(type(generador))

# Consumimos los valores del generador
for valor in generador:
    print(f'Número producido: {valor}')

# Consumir a demanda
generador = generador_numeros()
try:
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
    print(f'consumimos a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error al consumir generador {e}')

# Otra forma de consumir un generador
generador = generador_numeros()
while True:
    try:
        valor = next(generador)
        print(f'Impresión valor generado: {valor}')
    except StopIteration as e:
        print('Se terminó de iterar el generador')
        break