from models.Informe import Informe

class InformeDepartamentos(Informe):
    def __init__(self, formato='', fecha_creacion='', departamentos = None, db_conexion = None):
        super().__init__(formato, fecha_creacion)
        self.__departamentos = departamentos if departamentos is not None else []

        @property
        def departamentos(self):
            return self.__departamentos
        
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