# Profundizando en el tipo str

# help(str.join)

tupla_str = ('Hola','Mundo','Universidad','Python')
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(f'mensaje: {mensaje}')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre':'Juan', 'apellido': 'Perez', 'edad':'18'}
llaves = ' '.join(diccionario.keys())
valores = ' '.join(diccionario.values())
print(f'llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, type: {type(valores)}')