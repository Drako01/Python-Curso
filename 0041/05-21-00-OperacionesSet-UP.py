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
# Podemos agregar más elementos on incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set (copia poco profunda, solo copia referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar igualdad
print(f'Es igual en contenido? {conjunto == conjunto_copia}')
print(f'Es la misma referencia? {conjunto is conjunto_copia}')

# Operaciones de conjuntos con set
# Personas con distintas características
pelo_negro = {'Juan','Karla','Pedro','María'}
pelo_rubio = {'Lorenzo','Laura','Marco'}
ojos_cafe = {'Karla','Laura'}
menores_30 = {'Juan','Karla','María'}
# Todos con ojos_cafe y pelo rubio (Union) (no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# (intersetion) Sólo las personas con ojos cafe y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

# (difference) Pelo negro sin ojos cafe (no es conmutativa)
# las personas que se encuentran en el primer set pero NO en el segundo
print(pelo_negro.difference(ojos_cafe))

# (diferencia simétrica) Pelo negro u ojos cafe, pero NO ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))