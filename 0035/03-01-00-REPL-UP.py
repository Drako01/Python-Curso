class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, id: {hex(id(self)).upper()}'

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez')
    print(persona1)

def mostrar_mensaje(mensaje):
    print(mensaje)