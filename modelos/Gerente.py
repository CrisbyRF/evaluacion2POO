from .Empleado import Empleado
import mysql.connector

#Un gerente es un tipo de empleado, por lo que hay herencia
class Gerente(Empleado):
    def __init__(self, nombre='', direccion='', telefono='', email='', inicio_contrato=None, salario=0, proyecto=None, administrador = False, cargo = '', empleados = None ):
        super().__init__(nombre, direccion, telefono, email, inicio_contrato, salario, proyecto)
        self.administrador = administrador
        self.cargo = cargo
        self.empleados = empleados if empleados is not None else []
        
    def generarInforme(self):
        #Aplicar lógica
        pass
    
    @classmethod
    def registrarEmpleado(cls, nombre, direccion, telefono, email, inicio_contrato, salario, proyecto, db_conection):
        try:
            cursor = db_conection.cursor()
            query = """
                INSERT INTO empleado
                (nombre, direccion, telefono, email, fecha_inicio, salario, proyectos)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (nombre, direccion, telefono, email, inicio_contrato, salario, proyecto)
            cursor.execute(query, valores)
            db_conection.commit()
            print(f'\nEmpleado {nombre} creado exitosamente\n')
            return True
        except mysql.connector.IntegrityError as err:
            print('\n¡El empleado ya existe o email duplicado!\n')
            db_conection.rollback()
            return False
        except mysql.connector.Error as err:
            print(f'\nError al crear empleado: {err}\n')
            db_conection.rollback()
            return False
        finally:
            cursor.close()
    
    @staticmethod 
    def listarEmpleados(db_conection):
        try:
            cursor = db_conection.cursor(dictionary = True)
            query = """
                SELECT * FROM empleados
            """ 
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            if not resultados:
                print('\nNo se encontraron empleados\n')
                return []

            for fila in resultados:
                print(f"Nombre: {fila['nombre']}")
                print(f"Email: {fila['email']}")
                print(f"Salario: {fila['salario']}")
                print(f"Proyecto: {fila['proyectos']}")
                print("-" * 40)
               
        except mysql.connector.Error as err:
            print(f'\nError al listar empleados: {err}\n')
            return []
        finally:
            if cursor:
                cursor.close()