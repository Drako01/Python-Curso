# Alcance de Variables (scope)

var_global = 'Variable global'

def imprimir():
    # Acceder a una variable global
    print(f'Variable global desde función: {var_global}')
    # Definición de variable local
    var_local = 'Variables local'
    print(f'Variable local desde función: {var_local}')

    def funcion_anidada():
        print(f'Variable local dentro función anidada: {var_local}')

    funcion_anidada()

imprimir()
print(f'Var global fuera función: {var_global}')
# No es posible acceder a variables locales fuera
# del bloque donde se definieron
# print(f'Var local fuera función: {var_local}')