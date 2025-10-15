from abc import ABC
from validaciones.funciones import validar_dato, validar_email

class Persona(ABC):
    def __init__(self, nombre = '', direccion = '', telefono = '', email = ''):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        validar_dato(nombre)
        self.__nombre = nombre.strip()
        
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, direccion):
        validar_dato(direccion)
        self.__direccion = direccion.strip()
        
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, telefono):
        if not telefono or len(telefono.strip()) == 0:
            raise ValueError('\n¡Este campo no puede quedar vacío!\n')
        self.__telefono = telefono.strip()
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if not email or len(email.strip()) == 0:
            raise ValueError('\n¡Este campo no puede quedar vacío!\n')
        self.__email = email