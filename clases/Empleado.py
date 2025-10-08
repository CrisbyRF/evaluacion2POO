from clases.modelos.Persona import Persona
from RegistroHorario import RegistroHorario
from datetime import datetime

fecha_actual = datetime.now().strftime("%d-%m-%Y")

class Empleado(Persona):
    def __init__(self, nombre='', direccion='', telefono='', email='', inicio_contrato = None, salario = 0, proyectos = None ):
        #CAMBIAR EL TIPO DE DATO DE PROYECTOS PARA CUANDO HAYA UNO
        super().__init__(nombre, direccion, telefono, email)
        self.inicio_contrato = inicio_contrato
        self.salario = salario
        if proyectos == None:
            self.proyectos = []
        self.proyectos = proyectos
    
    @classmethod
    def crearEmpleado(cls):
        nombre = input('Ingrese el nombre del empleado: ')
        direccion = input('Ingrese direccion del empleado: ')
        telefono = input('Ingrese telefono del empleado: ')
        email = input('Ingrese el email del empleado: ')
        inicio_contrato = fecha_actual
        salario = int(input('Ingrese el salario del empleado: '))
        proyectos = '' #implementar mas adelante
        return cls(nombre, direccion, telefono, email, inicio_contrato, salario, proyectos)
    
    def crearRegistro(self):
        horas_trabajadas = int(input('Ingrese sus horas trabajadas: '))
        fecha = fecha_actual
        descripcion_tarea = input('Ingrese la descripción de la tarea [200 caracteres máximo]: ')
        registro_final = RegistroHorario(horas_trabajadas, fecha, descripcion_tarea)
        
        return registro_final