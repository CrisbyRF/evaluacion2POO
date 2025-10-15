class EmpleadoProyecto:
    def __init__(self, empleado = None, proyecto = None, rol = '', fecha_inicio = None, fecha_fin = Date):
        self.__empleado = empleado
        self.__proyecto = proyecto
        self.__rol = rol
        self.__fecha_asignacion = fecha_inicio

    @property
    def empleado(self):
        return self.__empleado
    
    @property
    def proyecto(self):
        return self.__proyecto
    
    @property
    def rol (self):
        return self.__rol
    
    @rol.setter
    def rol (self, nuevo_rol):
        if nuevo_rol:
            self.__rol = nuevo_rol
        
    @property
    def fecha_asignacion (self):
        return self.__fecha_asignacion
    
def actualizarFechas(self, fecha_incio):
    pass

def cambiarRol(self, nuevo_rol):
    pass

def mostrarDetalle(self, db_conexion):
    pass