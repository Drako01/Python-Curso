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
