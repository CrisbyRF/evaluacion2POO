class RegistroHorario:
    def __init__(self, horas_trabajadas = 0, fecha= '', descripcion_tareas = ''):
        self.__horas_trabajadas = horas_trabajadas
        self.__fecha = fecha
        self.__descripcion_tareas = descripcion_tareas
        
    def get_horas_trabajadas (self):
        return self.__horas_trabajadas
    
    def set_horas_trabajadas (self, horas_trabajadas):
        self.__horas_trabajadas = horas_trabajadas
        
    def get_fecha (self):
        return self.__fecha
    
    def set_fecha (self, fecha):
        self.__fecha = fecha
        
    def get_descripcion_tareas (self):
        return self.__descripcion_tareas
    
    def set_descripcion_tareas (self, descripcion):
        self.__descripcion_tareas = descripcion