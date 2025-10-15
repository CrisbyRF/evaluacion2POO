from datetime import datetime
import mysql.connector
from ...validaciones.funciones import validar_dato, validar_fecha, validar_entrada
#EN LA INTERFAZ MOSTRAR UNA OPCIÓN PARA VOLVER ATRÁS EN CASO DE QUE EL USUARIO SE HAYA EQUIVOCADO EN CADA SELECCION
class Proyecto:
    def __init__(self, nombre = '', descripcion = '', fecha_inicio = None, estado = False):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__estado = estado
        self.__asignaciones = [] #Lista de empleados

    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nuevo_nombre):
        validar_dato(nuevo_nombre)
        self.__nombre = nuevo_nombre
        
    def crearProyecto(self, db_conexion, nombre, descripcion, fecha_inicio):
        try:
            cursor = db_conexion.cursor()
            consulta = """
                INSERT INTO proyecto (nombre, descripcion, fecha_inicio)
                VALUES  (%s,%s,%s)
            """
            valores= (nombre, descripcion, fecha_inicio)
            cursor.execute(consulta, valores)
            db_conexion.commit()
            print('\n¡Proyecto creado de manera exitosa!\n')
            return True
        except mysql.connector.IntegrityError as err:
            print('\n¡El proyecto ya existe o email duplicado!\n')
            db_conexion.rollback()
            return False
        except mysql.connector.Error as err:
            print(f'\nError al crear el proyecto: {err}\n')
            db_conexion.rollback()
            return False
        finally:
            cursor.close()
        
    def editarProyecto(self, db_conexion):
        campos_para_actualizar = []
        valores = []
        id_editar = None
        try:
            cursor = db_conexion.cursor()
            cursor.execute ('SELECT id_proyecto, nombre FROM proyecto')
            proyectos = cursor.fetchall()
            
            if not proyectos:
                print('\n¡No hay proyectos disponibles!\n')
                return
            
            print('\n=== PROYECTOS DISPONIBLES ===')
            for id_p, nombre_p in proyectos:
                print(f'ID: {id_p} | Nombre: {nombre_p}')
                print('=====================================')
                
            id_editar = int(input('Ingrese el ID del proyecto que desee editar: '))
            
            while True:
                print('\n=== ¿Qué desea modificar? ===')
                print('1. Nombre')
                print('2. Descripción')
                print('3. Fecha de inicio')
                print('4. Guardar datos y salir')
                print('5. Cancelar')
                
                seleccion = input('Seleccione un opción: ').strip()
                
                if seleccion == '4':
                    break
                
                if seleccion == '5':
                    print('\nEdición cancelada\n')
                    return
                
                if seleccion not in ('1', '2', '3'):
                    print('\n¡Opción inválida! Intente de nuevo.\n')
                    continue
                
                match seleccion:
                    case '1':
                        nuevo_nombre = validar_entrada('Ingrese el nuevo nombre: ')
                        if nuevo_nombre:
                            if "nombre = %s" not in campos_para_actualizar:
                                campos_para_actualizar.append("nombre = %s")
                                valores.append(nuevo_nombre)  
                            else:
                                print('\nYa modificaste el nombre. Finaliza la edición para guardar\n')
                            print('\nEl nombre está listo para ser actualizado\n')
                    case '2':
                        nueva_descripcion = validar_entrada('Ingrese la nueva descripción: ')
                        if nueva_descripcion:
                            if 'descripcion = %s' not in campos_para_actualizar:
                                campos_para_actualizar.append('descripcion = %s')
                                valores.append(nueva_descripcion)
                            else:
                                print('\nYa modificaste la descripcion. Finaliza la edición para guardar\n')   
                        print('\nEl nombre está listo para ser actualizado\n')
                    case '3':
                        nueva_fecha = validar_fecha('Ingrese la nueva fecha de inicio [DD-MM-YYYY]: ')
                        if nueva_fecha:
                            if 'fecha_inicio = %s' not in campos_para_actualizar:
                                campos_para_actualizar.append('fecha_inicio = %s')
                                valores.append(nueva_fecha)
                            else:
                                print('\nYa modificaste la fecha. Finaliza la edición para guardar\n')
                            print('\nLa fecha está lista para ser actualizada\n')
            if seleccion not in ('1', '2', '3', '4', '5'):
                print('\nOpción inválida\n')
                return
            if not campos_para_actualizar:
                print('\nNo se seleccionó ningún campo para actualizar\n')
                return
            valores.append(id_editar)
            clausula = ", ".join(campos_para_actualizar)
            consulta = f"UPDATE proyecto SET {clausula} WHERE id_proyecto = %s"
                    
            cursor.execute(consulta, tuple(valores))
            if cursor.rowcount == 0:
                print(f'\n¡No se encontró el proyecto con el ID seleccionado\n')
                db_conexion.rollback()
            else:
                db_conexion.commit()
                print(f'\n¡El proyecto con el ID {id_editar} se ha editado de manera exitosa!, se actualizaron {len(campos_para_actualizar)} campos\n')
        except mysql.connector.Error as err:
            print('\nError al editar el proyecto\n')
            db_conexion.rollback()
        finally:
            cursor.close()
    
    def eliminarProyecto(self, id):
        #Mostrar interfaz de todos los proyectos creados
        id_eliminar = int(input('Ingrese el ID del proyecto que desee eliminar: '))
        #Aplicar lógica
        #Preguntar para confirmación de eliminación de proyecto
        #No retornar nada
        
    def listarProyectos(self):
        pass
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