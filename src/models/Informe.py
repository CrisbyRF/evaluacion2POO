from abc import ABC, abstractmethod
from datetime import date

class Informe (ABC):
    def __init__(self, formato = '', fecha_creacion = None):
        self.__formato = formato
        self.__fecha_creacion = fecha_creacion or str(date.today())

    @property
    def formato(self):
        return self.__formato

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion
        
    @abstractmethod
    def generarInforme(self):
        #aplicar lógica
        pass
    
    @abstractmethod
    def exportar(self):
        print(f'\nExportando informe en formato {self.formato}...')