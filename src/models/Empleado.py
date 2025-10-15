from .Persona import Persona
from models.RegistroHorario import RegistroHorario
import mysql.connector
from datetime import date

class Empleado(Persona):
    def __init__(self, nombre='', direccion='', telefono='', email='', inicio_contrato = None, salario = 0, departamento = None):
        #CAMBIAR EL TIPO DE DATO DE PROYECTOS PARA CUANDO HAYA UNO
        super().__init__(nombre, direccion, telefono, email)
        self.__inicio_contrato = inicio_contrato or date.today()
        self.__salario = salario
        self.__departamento = departamento
        self.__asignaciones = []
        
    def __str__(self):
        return
    
    @property
    def asignaciones(self):
        return self.__asignaciones
    
    def agregar_asignacion(self, asignacion):
        self.__asignaciones.append(asignacion)
    
    @property
    def inicio_contrato(self):
        return self.__inicio_contrato
    
    @property
    def salario (self):
        return self.__salario
    
    @property
    def departamento(self):
        return self.__departamento
    
    @salario.setter
    def salario(self, salario):
        if salario < 0:
            raise ValueError('\nEl salario no puede ser negativo\n')
        self.__salario = salario
                     
            
    def crearRegistro(self, horas_trabajadas, fecha, descripcion):
        pass
        #Debe retornar el registro como objeto
    
    def asignarDepartamento(self, departamento):
        pass
        #Debe retornar el
        
    def actualizarDatos(self, empleado):
        pass
        #Debe retornar True o False