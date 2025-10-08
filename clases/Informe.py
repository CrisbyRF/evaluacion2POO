from abc import ABC, abstractmethod

class Informe (ABC):
    def __init__(self, formato = '', fecha_creacion = ''):
        self.formato = formato
        self.fecha_creacion = fecha_creacion
        
    @abstractmethod
    def generarInforme(self):
        #aplicar lógica
        pass
        
    def exportar(self):
        #Aplicar lógica de exportación
        pass
        