from validaciones.funciones import validar_fecha, validar_dato
class RegistroHorario:
    def __init__(self, horas_trabajadas = 0, fecha= None, descripcion_tareas = ''):
        self.horas_trabajadas = horas_trabajadas
        self.fecha = fecha
        self.descripcion_tareas = descripcion_tareas #maximo 250 caracteres
        
    @property
    def horas_trabajadas (self):
        return self.__horas_trabajadas
    
    @horas_trabajadas.setter
    def horas_trabajadas(self, horas_trabajadas):
        if horas_trabajadas <= 0:
            raise ValueError('\nLa cantidad de horas debe ser mayor a 0\n')
        self.__horas_trabajadas = horas_trabajadas
        
    @property
    def fecha (self):
        return self.__fecha
    
    @fecha.setter
    def fecha (self, fecha):
        validar_fecha(fecha)
        self.__fecha = fecha
        
    @property
    def descripcion_tareas (self):
        return self.__descripcion_tareas
    
    @descripcion_tareas.setter
    def descripcion_tareas (self, descripcion):
        validar_dato(descripcion)
        if len(descripcion) > 250:
            raise ValueError('\n¡200 caracteres permitidos como máximo!\n')
        self.__descripcion_tareas = descripcion