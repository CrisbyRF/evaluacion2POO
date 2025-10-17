from .Persona import Persona
from models.RegistroHorario import RegistroHorario
from validaciones.funciones import validar_entrada, validar_fecha, validar_dato
from datetime import date

class Empleado(Persona):
    def __init__(self, nombre='', direccion='', telefono='', email='', inicio_contrato = None, salario = 0, cargo = 'Empleado',departamento = None):
        super().__init__(nombre, direccion, telefono, email)
        self.__inicio_contrato = inicio_contrato or date.today()
        self.__salario = salario
        self.__cargo = cargo
        self.__departamento = departamento
        self.__asignaciones = []
        
    def __str__(self):
        return (
        super().__str__() + "\n"
        f"Inicio de contrato: {self.inicio_contrato}\n"
        f"Salario: ${self.salario}\n"
        f"Departamento: {self.departamento.nombre if self.departamento else 'No asignado'}"
        )
    
    @property
    def asignaciones(self):
        return self.__asignaciones
    
    def agregar_asignacion(self, asignacion):
        self.__asignaciones.append(asignacion)
    
    @property
    def inicio_contrato(self):
        return self.__inicio_contrato
    
    @property
    def cargo (self):
        return self.__cargo
    
    @cargo.setter
    def cargo (self, nuevo_cargo):
        validar_dato(nuevo_cargo)
        if nuevo_cargo not in ('Empleado', 'Gerente'):
            print('\nCargo inválido. Solo se permite "empleado" o "gerente".\n')
            return
        self.__cargo = nuevo_cargo
    
    @property
    def salario (self):
        return self.__salario
    
    @property
    def departamento(self):
        return self.__departamento
    
    @salario.setter
    def salario(self, salario):
        if salario < 0:
            raise ValueError('\nEl salario no puede ser negativo\n')
        self.__salario = salario
                     
            
    def crearRegistro(self, horas_trabajadas, fecha, descripcion, db_conexion):
        try:
            if not horas_trabajadas or horas_trabajadas <= 0:
                print('\nLa cantidad de horas debe ser mayor a 0\n')
                return None
            
            fecha_validada = validar_fecha(fecha)
            descripcion_validada = validar_entrada(descripcion)
            
            cursor = db_conexion.cursor()
            query = """
            INSERT INTO registroHorario (horas_trabajadas, fecha, descripcion)
            VALUES (%s, %s, %s)
            """
            valores = (horas_trabajadas, fecha_validada, descripcion_validada)
            cursor.execute(query, valores)
            db_conexion.commit()
            
            print('\n¡Registro creado exitosamente!\n')
            return RegistroHorario(horas_trabajadas, fecha_validada, descripcion_validada)
        except Exception as err:
            print(f'\nError al crear el registro: {err}\n')
            db_conexion.rollback()
            return None
        finally:
            cursor.close()
    
    def asignarDepartamento(self, departamento):
        if not departamento:
            print('\n¡Debe proporcionar un departamento válido!\n')
            return self
        self.__departamento = departamento
        departamento.asignarEmpleado(self)
        return self
        
    def actualizarDatos(self, db_conexion):
        opciones = {
            "1": "nombre",
            "2": "direccion",
            "3": "telefono",
            "4": "email",
            "5": "salario"
        }
        print('\nSeleccione una opción que desee modificar\n')
        for clave, valor in opciones.items():
            print(f'{clave}: {valor.capitalize()}')
            
        seleccion = input('\nIngrese su opción: ')
        
        if seleccion not in opciones:
            print('\nOpción inválida\n')
            return False
        
        nuevo_valor = validar_entrada(f'Ingrese el valor para {opciones[seleccion]}: ')
        
        try:
            cursor = db_conexion.cursor()
            campo = opciones[seleccion]
            
            if campo == "salario":
                nuevo_valor = int(nuevo_valor)
                self.salario = nuevo_valor
            else:
                setattr(self, campo, nuevo_valor)
            
            query = f"""UPDATE empleados SET {campo} = %s
            WHERE email = %s
            """
            valores = (nuevo_valor, self.email)
            cursor.execute(query, valores)
            db_conexion.commit()
            
            print(f"\n{opciones[seleccion].capitalize()} actualizado correctamente.\n")
            return True
        except Exception as err:
            print(f'\nError al actualizar: {err}\n')
            return False
        finally:
            cursor.close()