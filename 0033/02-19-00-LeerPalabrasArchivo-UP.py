# Leer contenido online
from urllib.request import urlopen

palabras = []
with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    for linea in mensaje:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)
print(palabras)
