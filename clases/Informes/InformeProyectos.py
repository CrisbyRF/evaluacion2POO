from Informe import Informe

class InformeProyectos(Informe):
    def __init__(self, formato='', fecha_creacion='', proyectos = None):
        super().__init__(formato, fecha_creacion)
        if proyectos == None:
            self.proyectos = []
        self.proyectos = proyectos
        
    def generarInforme(self):
        if not self.proyectos:
            print('\nNo hay proyectos registrados\n')
            return
        pass
    
#Ejemplo de uso
#informe = InformeProyectos(
#    formato='PDF',
#    fecha_creacion=str(date.today()),
#    proyectos = [proyecto1, proyecto2]
#)