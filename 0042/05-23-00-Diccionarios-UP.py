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
