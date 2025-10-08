from Empleado import Empleado

#Un gerente es un tipo de empleado, por lo que hay herencia
class Gerente(Empleado):
    def __init__(self, nombre='', direccion='', telefono='', email='', inicio_contrato='', salario=0, proyectos=None, administrador = False, cargo = '', empleados = None ):
        super().__init__(nombre, direccion, telefono, email, inicio_contrato, salario, proyectos)
        self.administrador = administrador
        self.cargo = cargo
        if empleados == None:
            self.empleados = []
        self.empleados  = empleados
        
    def generarInforme():
        #Aplicar lógica
        pass
    
    def registrarEmpleado(self):
        nuevo_empleado = Empleado.crearEmpleado()
        self.empleados.append(nuevo_empleado)
        return nuevo_empleado