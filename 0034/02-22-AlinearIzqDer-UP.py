# Leer contenido online
from urllib.request import urlopen

with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    contenido = mensaje.read().decode('utf-8')

# Contar ocurrencias de una cadena
print('No. veces Universidad: ', contenido.count('Universidad'))

# upper convierte a mayúsculas un str
print(contenido.upper())
print(contenido)

# lower convierte a minúsculas un str
print(contenido.lower())

# buscamos la cadena python en el contenido
print('Existe python?: ','python'.lower() in contenido.lower())
print('Existe Python?: ','Python'.upper() in contenido.upper())

# startswith - inicia con
print('Inicia con: ',contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - termina con
print('Termina con:', contenido.lower().endswith('globalmentoring.com.mx'.lower()))

# Alinear cadenas

# center - Centrar un str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
# print(len(titulo))
# print(titulo.center(10,'*'))
# print(len(titulo.center(50,'*')))
print(titulo.center(len(titulo)+10,'-'))

# ljust - alinea a la izquierda
# print(titulo.ljust(50,'*'))
print(titulo.ljust(len(titulo)+10,'-'))

# rjust - alinea a la derecha
# print(titulo.rjust(50,'*'))
print(titulo.rjust(len(titulo)+10,'-'))