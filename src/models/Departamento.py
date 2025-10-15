class Departamento:
    def __init__(self, nombre, empleados = None, gerente = ''):
        self.__nombre = nombre
        if empleados == None:
            self.__empleados = []
        self.__empleados = empleados
        self.__gerente = gerente
    
    #IMPLEMENTAR GETTER Y SETTER
    
    def crearDepartamento(self,nombre, gerente):
        nombre_departamento = input('Ingrese el nombre del departamento: ')
        empleados = [] #Aplicar logica mas adelante
        departamento_final = Departamento(nombre_departamento, empleados, gerente)
        return departamento_final
    
    def editarDepartamento(self, id):
        #Mostrar listado de departamentos con su respectivo ID
        id_editar = input('Ingrese el ID del departamento que desee editar: ')
        #Menú para editar nombre o gerente
        #No retornar nada
    
    def buscarDepartamento(self, id):
        #Mostrar listado de departamentos con su respectivo ID
        id_buscar = input('Ingrese el ID del departamento que desee buscar: ')
        #Mostrar si existe el departamento, y cual es el nombre del departamento junto a sus empleados y gerente
        #No retornar nada
    
    def eliminarDepartamento(self, id):
        #Mostrar listado de departamentos con su respectivo ID
        id_eliminar = input('Ingrese el ID del departamento que desee eliminar: ')
        #Pedir confirmacion para eliminar
        #No retornar nada
    
    def asignarEmpleado(self, empleado):
        if empleado.departamento is not None:
            print(f'\nEl empleado ya pertenece al departamento: {empleado.departamento.nombre}')
            return False
        self.__empleados.append(empleado)
        empleado.asignarDepartamento(self)
        return True
    
    def desasignarEmpleado(self, empleado):
        if empleado not in self.__empleados:
            print(f'\nEl empleado {empleado.nombre} no pertenece a este departamento\n')
            return
        self.__empleados.remove(empleado)
        empleado.asignarDepartamento(None)
        print(f'\nEl empleado {empleado.nombre} ha sido designado del departamento {self.nombre}\n')