# Profundizar en set
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables
# conjunto = {[1,2],[3,4]}
conjunto = {'Juan', True, 18.0}
print(conjunto)
# Set vacío
# conjunto = {} genera un dict vacío
# print(type(conjunto))
# set vacío correcto
conjunto = set()
print(conjunto)
print(type(conjunto))
# Mutable
conjunto.add('Juan')
print(conjunto)
# Contiene valores únicos
conjunto.add('Juan')
print(conjunto)
# Crear un set a partir de un iterable
conjunto = set([4,5,7,8,4])
print(conjunto)
