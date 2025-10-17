from .Empleado import Empleado
import mysql.connector
from datetime import date
from informes.InformeEmpleados import InformeEmpleados
from informes.InformeDepartamentos import InformeDepartamentos
from informes.InformeProyectos import InformeProyectos
from informes.InformeRegistros import InformeRegistros

class Gerente(Empleado):
    def __init__(self, nombre='', direccion='', telefono='', email='', inicio_contrato=None, salario=0, administrador=True, proyecto=None, id_empleado=None, departamento=None):
        super().__init__(nombre, direccion, telefono, email, inicio_contrato, salario, cargo='Gerente', departamento= departamento, id_empleado= id_empleado)
        self.__administrador = administrador
        self.__proyecto = proyecto
        
    @property
    def administrador(self):
        return self.__administrador

    @administrador.setter
    def administrador(self, nuevo_valor):
        if isinstance(nuevo_valor, bool):
            self.__administrador = nuevo_valor
        else:
            raise ValueError("El valor debe ser booleano (True o False)")
        
    @property
    def proyecto(self):
        return self.__proyecto

    @proyecto.setter
    def proyecto(self, nuevo_proyecto):
        self.__proyecto = nuevo_proyecto
           
    def generarInforme(self, db_conexion):
        print('\n¿Qué tipo de informe desea generar?\n')
        print('1) Informe de empleados')
        print('2) Informe de departamentos')
        print('3) Informe de proyectos')
        print('4) Informe de registro de horarios ')
        print('5) Volver atrás')
        
        opcion = input('\nSELECCIONE OPCIÓN: ').strip()
        formato = input('\nIngrese el formato deseado [pdf / excel] : ').lower()
        if formato not in ['pdf', 'excel']:
            print('\nFormato inválido. Debe ser PDF o EXCEL.\n')
            return
        fecha_actual = str(date.today())
        informe = None
        
        match opcion:
            case '1':
                empleados = self.listarEmpleados(db_conexion)
                informe = InformeEmpleados(
                    formato = formato,
                    fecha_creacion = fecha_actual,
                    empleados = empleados
                )
                
            case '2':
                cursor = db_conexion.cursor(dictionary = True)
                cursor.execute('SELECT id_departamento, nombre FROM departamento')
                departamentos = cursor.fetchall()
                cursor.close()
                informe = InformeDepartamentos(
                    formato = formato,
                    fecha_creacion = fecha_actual,
                    departamentos=departamentos
                )
            
            case '3':
                cursor = db_conexion.cursor(dictionary = True)
                cursor.execute ('SELECT id_proyecto , nombre, descripcion, fecha_inicio, fecha_termino, estado FROM proyecto')
                proyectos = cursor.fetchall()
                cursor.close()
                informe = InformeProyectos(
                    formato = formato,
                    fecha_creacion= fecha_actual,
                    proyectos = proyectos
                )
                
            case '4':
                cursor = db_conexion.cursor(dictionary = True)
                cursor.execute('SELECT id_registro_horario, horas_trabajadas, fecha, descripcion_tarea FROM registroHorario')
                registros = cursor.fetchall()
                cursor.close()
                informe = InformeRegistros(
                    formato = formato,
                    fecha_creacion= fecha_actual,
                    registros = registros
                )
            case '5':
                print('\nPresione ENTER para volver\n')
                return
            case _:
                print('\nOpción inválida, intente nuevamente\n')
        if informe:
            informe.generarInforme()
            informe.exportar()
    
    @classmethod
    def registrarEmpleado(cls, nombre, cargo, direccion, telefono, email, inicio_contrato, salario, db_conexion):
        try:
            cursor = db_conexion.cursor()
            query = """
                INSERT INTO empleado
                (nombre, cargo, direccion, telefono, email, fecha_inicio, salario)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cargo = cargo.strip().capitalize()
            
            if cargo not in ('Empleado', 'Gerente'):
                print('\nCargo inválido. Solo se permite "Empleado" o "Gerente".\n')
                return
            valores = (nombre, cargo, direccion, telefono, email, inicio_contrato, salario)
            cursor.execute(query, valores)
            db_conexion.commit()
            print(f'\nEmpleado {nombre} creado exitosamente\n')
            return True
        except mysql.connector.IntegrityError as err:
            print('\n¡El empleado ya existe o email duplicado!\n')
            db_conexion.rollback()
            return False
        except mysql.connector.Error as err:
            print(f'\nError al crear empleado: {err}\n')
            db_conexion.rollback()
            return False
        finally:
            cursor.close()
    
    @staticmethod 
    def listarEmpleados(db_conexion):
        try:
            cursor = db_conexion.cursor(dictionary = True)
            query = """
                SELECT id_empleado, nombre, email, salario, proyecto FROM empleado
            """ 
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            if not resultados:
                print('\nNo se encontraron empleados\n')
                return []

            empleados = []
            
            for fila in resultados:
                proyecto = fila['proyecto'] if fila['proyecto'] else 'No asignado a ningún proyecto'
                print(f"ID: {fila['id_empleado']}")
                print(f"Nombre: {fila['nombre']}")
                print(f"Email: {fila['email']}")
                print(f"Salario: ${fila['salario']}")
                print(f"Proyecto: {proyecto}")
                print("-" * 40)
                
                empleados.append(fila)
            return empleados
                       
        except mysql.connector.Error as err:
            print(f'\nError al listar empleados: {err}\n')
            return []
        finally:
            if cursor:
                cursor.close()
    def eliminar_empleado(self, db_conexion):
        try:
            cursor = db_conexion.cursor()
            id_empleado = input('\nIngrese el ID del empleado a eliminar: ')
            if not id_empleado.isdigit():
                print('El numero debe ser una numero entero para el ID')
                return
            cursor.execute('SELECT nombre from empleado WHERE id_empleado = %s', (id_empleado,))
            empleado = cursor.fetchone()
            if not empleado:
                print('No se encontro un empleado con la ID ingresada')
                return
            nombre_empleado = empleado[0]
            cursor.execute('SELECT COUNT(*) FROM EmpleadoProyecto WHERE id_empleado = %s', (id_empleado,))
            asignaciones = cursor.fetchone()[0]
            if asignaciones > 0:
                print(f'\nEl empleado tiene {asignaciones} asignación(es) activa(s) en proyectos.')
                print('Debe desasignarlo antes de eliminarlo.\n')
                return
            while True:
                confirmacion = input('¿Desea eliminarlo? [s/n]: ').strip().lower()
                if confirmacion == 's':
                    cursor.execute('DELETE FROM empleado WHERE id_empleado = %s', (id_empleado,))
                    db_conexion.commit()
                    if cursor.rowcount > 0:
                        print(f'\nEl empleado "{nombre_empleado}" fue eliminado con éxito.\n')
                    else:
                        print('\nNo se pudo eliminar el empleado.\n')
                    break
                elif confirmacion == 'n':
                    print('\nOperación cancelada. El empleado no fue eliminado.\n')
                    break
                else:
                    print('\nRespuesta no válida. Seleccione "s" para confirmar o "n" para cancelar.\n')
        except Exception as e:
            print(f'\nError al eliminar el empleado: {e}\n')
            input('\nPresione ENTER para continuar\n')
            db_conexion.rollback()
        finally:
            cursor.close()
            input('\nPresione ENTER para continuar\n')
            
    def buscarEmpleado(self, db_conexion):
        try:
            cursor = db_conexion.cursor()
            id_buscar = input('Ingrese el ID del empleado que desee buscar: ')
            if not id_buscar.isdigit():
                print('\nEl ID debe ser un número entero.\n')
                return
            id_buscar = int(id_buscar)
            cursor.execute ('SELECT nombre FROM empleado WHERE id_empleado = %s', (id_buscar, ))
            empleado = cursor.fetchone()
            if not empleado:
                print(f'\n¡No se encontro al empleado con el id {id_buscar}!\n')
                return
            print(f'\n¡Empleado "{empleado[0]}" encontrado con ID: {id_buscar}!\n')
            input('\nPresione ENTER para continuar')
            
        except Exception as err:
            print(f'\nNo se ha encontrado el empleado: {err}\n')
            input('\nPresione ENTER para continuar\n')