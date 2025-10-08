from Informe import Informe

class InformeEmpleados(Informe):
    def __init__(self, formato='', fecha_creacion='', empleados = None):
        super().__init__(formato, fecha_creacion)
        if empleados == None:
            self.empleados = []
        self.empleados = empleados
        
    def generarInforme(self):
        if not self.empleados:
            print('\nNo hay empleados registrados\n')
            return
        pass
    
#Ejemplo de uso
#informe = InformeEmpleados(
#    formato='PDF',
#    fecha_creacion=str(date.today()),
#    empleados=[empleado1, empleado2]
#)