# Más de funciones anidadas y alcance de variables

def funcion_externa():
    variable_local_externa = 'Variable local externa'

    def funcion_anidada():
        variable_local_anidada = 'Variable local anidada'

        nonlocal variable_local_externa
        variable_local_externa = 'Nuevo valor variable local externa'

    funcion_anidada()

    print(f'Valor variable local externa: {variable_local_externa}')
    # No es posible acceder a una variable local más interna
    # print(f'Valor variable local anidada: {variable_local_anidada}')

funcion_externa()