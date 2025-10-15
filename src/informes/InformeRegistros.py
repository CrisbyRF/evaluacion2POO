from clases.modelos.Informe import Informe

class InformeRegistros(Informe):
    def __init__(self, formato='', fecha_creacion='', registros = None):
        super().__init__(formato, fecha_creacion)
        if registros == None:
            self.__registros = []
        self.__registros = registros
        
        #IMPLEMENTAR GETTER
        
    def generarInforme(self):
        if not self.__registros:
            print('\nNo hay registros registrados\n')
            return
        pass
    
#Ejemplo de uso
#informe = InformeRegistros(
#    formato='PDF',
#    fecha_creacion=str(date.today()),
#    registros = [registro1, registro2]
#)