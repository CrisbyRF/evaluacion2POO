class Departamento:
    def __init__(self, nombre, empleados = None, gerente = ''):
        self.nombre = nombre
        if empleados == None:
            self.empleados = []
        self.empleados = empleados
        self.gerente = gerente
    
    def crearDepartamento(self, gerente):
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
    
    def asignarEmpleado(self, id_empleado):
        #Mostrar listado de empleados
        empleado_seleccion = int(input('Ingrese el ID del empleado que desee asignar: ')) #Solo mostrar empleados que no esten asignados a un depa
        #Mostrar listado de departamentos
        departamento_seleccion = int(input('Ingrese el ID del departamento al que desee asignar el empleado: '))
        #Pedir confirmación
    
    def desasignarEmpleado(self, id_empleado):
        #Mostrar listado de empleados con su respectivo ID y departamentos asignados
        empleado_seleccion = input('Ingrese el ID del empleado que desee desasignar de su departamento: ')
        #Pedir confirmacion al usuario de la desasignacion
        #No retornar nada