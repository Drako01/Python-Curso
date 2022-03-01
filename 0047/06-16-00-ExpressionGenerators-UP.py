# Expresión generadora (es un generador anónimo)
multiplicacion = (valor*valor for valor in range(4))
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
# print(next(multiplicacion))

# También se puede pasar una expresión generadora a una función (sin paréntesis)
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')