from clases.modelos.Informe import Informe

class InformeDeparamentos(Informe):
    def __init__(self, formato='', fecha_creacion='', departamentos = None):
        super().__init__(formato, fecha_creacion)
        if departamentos == None:
            self.departamentos = []
        self.departamentos = departamentos
        
    def generarInforme(self):
        if not self.departamentos:
            print('\nNo hay departamentos registrados\n')
            return
        pass
    
#Ejemplo de uso
#informe = InformeDepartamentos(
#    formato='PDF',
#    fecha_creacion=str(date.today()),
#    departamentos = [departamento1, departamento2]
#)