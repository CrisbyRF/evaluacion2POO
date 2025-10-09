from .Persona import Persona
from modelos.RegistroHorario import RegistroHorario
import mysql.connector
from datetime import date

class Empleado(Persona):
    def __init__(self, nombre='', direccion='', telefono='', email='', inicio_contrato = None, salario = 0, proyectos = None ):
        #CAMBIAR EL TIPO DE DATO DE PROYECTOS PARA CUANDO HAYA UNO
        super().__init__(nombre, direccion, telefono, email)
        self.__inicio_contrato = inicio_contrato or date.today()
        self.__salario = salario
        if proyectos == None:
            self.__proyectos = []
        self.__proyectos = proyectos
    
    @property
    def inicio_contrato(self):
        return self.__inicio_contrato
    
    @property
    def salario (self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        if salario < 0:
            raise ValueError('\nEl salario no puede ser negativo\n')
        self.__salario = salario
                     
            
    def crearRegistro(self):
        horas_trabajadas = int(input('Ingrese sus horas trabajadas: '))
        fecha = ''
        descripcion_tarea = input('Ingrese la descripción de la tarea [200 caracteres máximo]: ')
        registro_final = RegistroHorario(horas_trabajadas, fecha, descripcion_tarea)
        
        return registro_final