from models.Informe import Informe

class InformeEmpleados(Informe):
    def __init__(self, formato='', fecha_creacion='', empleados = None):
        super().__init__(formato, fecha_creacion)
        self.__empleados = empleados if empleados is not None else []
        
    def empleados(self):
        return self.__empleados
        
    def generarInforme(self):
        if not self.__empleados:
            print('\nNo hay empleados registrados\n')
            return
        pass
    
#Ejemplo de uso
#informe = InformeEmpleados(
#    formato='PDF',
#    fecha_creacion=str(date.today()),
#    empleados=[empleado1, empleado2]
#)