from clases.modelos.Informe import Informe

class InformeProyectos(Informe):
    def __init__(self, formato='', fecha_creacion='', proyectos = None):
        super().__init__(formato, fecha_creacion)
        if proyectos == None:
            self.__proyectos = []
        self.__proyectos = proyectos
        
        #IMPLEMENTAR GETTER
        
    def generarInforme(self):
        if not self.__proyectos:
            print('\nNo hay proyectos registrados\n')
            return
        pass
    
#Ejemplo de uso
#informe = InformeProyectos(
#    formato='PDF',
#    fecha_creacion=str(date.today()),
#    proyectos = [proyecto1, proyecto2]
#)