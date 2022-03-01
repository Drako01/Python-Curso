# Produndizando en diccionarios

# Los dic guardan un orden (a diferencia de un set)
diccionario = {'Nombre':'Juan','Apellido':'Perez','Edad':28}
print(diccionario)

# Los dic son mutables, pero las llaves deben ser inmutables
# diccionario = {[1,2]:'Valor1'}
# diccionario = {(1,2):'Valor1'}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario (si ya existe se reemplaza)
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario['Nombre'])
# Si no encuentra la llave lanza una excepcion
# print(diccionario['nombre'])

# Método get recupera una llave, y si no existe NO lanza excepción
# además podemos regresar un valor en caso de que no exista la llave
print(diccionario.get('Nombres','No se encontró la llave'))
print(diccionario)

# setdefault sí modifica el diccionario, además se agregar un valor por default
nombre = diccionario.setdefault('Nombres','Valor por default')
print(nombre)
print(diccionario)

# Imprimir con pprint
from pprint import pprint as pp
# help(pp)
pp(diccionario, sort_dicts=False)