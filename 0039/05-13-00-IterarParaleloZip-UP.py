# print(dir(__builtins__))
# help(zip)
numeros = (1,2,3)
letras = ['a','b','c','d']
indentificadores = 321, 322, 323, 324, 325
conjunto = {6,4,0,9,8,15,10}
mezcla = zip(numeros, letras, indentificadores, conjunto)
# print(mezcla)
print(list(mezcla))
# print(tuple(zip(numeros, letras)))
# print(type(mezcla))

# iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros, letras, indentificadores, conjunto):
    print(f'Número: {numero}, Letra: {letra}, Id: {id}, Aleatorio: {aleatorio}')

nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros, letras, indentificadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)