from abc import ABC, abstractmethod

class Informe (ABC):
    def __init__(self, formato = '', fecha_creacion = None):
        self.__formato = formato
        self.__fecha_creacion = fecha_creacion
        
    #IMPLEMENTAR GETTER
        
    @abstractmethod
    def generarInforme(self):
        #aplicar lógica
        pass
        
    def exportar(self):
        #Aplicar lógica de exportación
        pass
        