from datetime import datetime

#EN LA INTERFAZ MOSTRAR UNA OPCIÓN PARA VOLVER ATRÁS EN CASO DE QUE EL USUARIO SE HAYA EQUIVOCADO EN CADA SELECCION
class Proyecto:
    def __init__(self, nombre = '', descripcion = '', fecha_inicio = '', empleados = None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        if empleados == None:
            self.empleados = []
        self.empleados = empleados
        
    def crearProyecto(self):
        fecha_actual = datetime.now().strftime('%d-%m-%Y')
        
        nombre = input('Ingrese el nombre del proyecto: ')
        descripcion = input('Ingrese la descripción del proyecto: ')
        fecha_inicio = fecha_actual
        empleados = [] #Implementar mas adelante
        #Retornar un objeto con todos los datos ingresados
        proyecto_final = Proyecto(nombre, descripcion, fecha_inicio, empleados)
        return proyecto_final
        
    def editarProyecto(self, id):
        #Mostrar el ID de todos los proyectos + el nombre correspondiente
        id_editar = int(input('Ingrese el ID del proyecto que desee editar: '))
        #Aplicar lógica
        #No retornar nada
    
    def eliminarProyecto(self, id):
        #Mostrar interfaz de todos los proyectos creados
        id_eliminar = int(input('Ingrese el ID del proyecto que desee eliminar: '))
        #Aplicar lógica
        #Preguntar para confirmación de eliminación de proyecto
        #No retornar nada
        
    def asignarEmpleado(self, id_empleado):
        #Mostrar listado de empleados
        empleado_seleccion = int(input('Ingrese el ID del empleado que desee asignar: '))
        #Mostrar listado de proyectos
        proyecto_seleccion = int(input('Ingrese el proyecto al cual desee asignar al empleado: '))
        #Preguntar confirmacion
        #NO RETORNAR NADA
        
    def desasignarEmpleado(self, id_empleado):
        #Mostrar listado de proyectos
        proyecto_seleccion = int(input('Ingrese el ID del proyecto: '))
        #Mostrar listado de empleados dentro del proyecto seleccionado
        empleado_seleccion = int(input('Ingrese el empleado el cual desee desasignar al proyecto: '))
        #Preguntar confirmacion
        #NO RETORNAR NADA