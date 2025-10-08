from abc import ABC

class Persona(ABC):
    def __init__(self, nombre = '', direccion = '', telefono = '', email = ''):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email