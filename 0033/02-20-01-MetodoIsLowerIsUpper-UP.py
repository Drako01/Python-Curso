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

mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())