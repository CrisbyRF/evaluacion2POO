from validaciones.funciones import validar_dato, validar_entrada

class Departamento:
    def __init__(self, nombre, empleados = None, gerente = ''):
        self.__nombre = nombre
        if empleados == None:
            self.__empleados = []
        self.__empleados = empleados
        self.__gerente = gerente
    
    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nuevo_nombre):
        validar_dato(nuevo_nombre)
        self.__nombre = nuevo_nombre
        
    @property
    def gerente(self):
        return self.__gerente
    
    @gerente.setter
    def gerente (self, nuevo_gerente):
        validar_dato(nuevo_gerente)
        self.__gerente = nuevo_gerente
        
    @property
    def empleados (self):
        return self.__empleados
    
    @empleados.setter
    def empleados (self, lista_empleados):
        if isinstance(lista_empleados, list):
            self.__empleados = lista_empleados
    
    def crearDepartamento(self,nombre, gerente, db_conexion):
        validar_dato(nombre)
        validar_dato(gerente)
        try:
            cursor = db_conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM empleado WHERE cargo = 'Gerente'")
            cantidad_gerentes = cursor.fetchone()[0]
            
            if cantidad_gerentes == 0:
                print('\nNo se puede crear un departamento porque no hay gerentes registrados en el sistema.\n')
                input('\nPresione ENTER para continuar\n')
                return
            cursor.execute("SELECT COUNT(*) FROM empleado WHERE nombre_empleado = %s AND cargo = 'Gerente'", (gerente,))
            existe_gerente = cursor.fetchone()[0]
            if existe_gerente == 0:
                print('\nEl nombre ingresado no corresponde a un gerente registrado.\n')
                input('\nPresione ENTER para continuar\n')
                return
            query = """
                INSERT INTO departamento (nombre, gerente)
                VALUES (%s,%s)
            """
            valores = (nombre, gerente)
            cursor.execute(query, valores)
            db_conexion.commit()
            self.__nombre = nombre
            self.__gerente = gerente
            print('\nDepartamento creado exitosamente\n')
            return self
            
        except Exception as err:
            print(f'\nError al crear el departamento: {err}\n')
            input('\nPresione ENTER para continuar\n').strip()
            return None
        finally:
            cursor.close()
    
    def editarDepartamento(self, db_conexion):
        try:
            cursor = db_conexion.cursor()
            query = """SELECT id, nombre_departamento, gerente FROM departamento"""
            cursor.execute(query)
            departamentos = cursor.fetchall()
            
            for departamento in departamentos:
                print(f'\nID: {departamento[0]} | Nombre: {departamento[1]} | Gerente: {departamento[2]}')
                id_editar = input('\nIngrese el ID del departamento que desee editar: ')
                cursor.execute("SELECT COUNT(*) FROM departamento WHERE id = %s", (id_editar,))
                existe = cursor.fetchone()[0]
                if existe == 0:
                    print('\nEl ID ingresado no existe\n')
                    return
            print('\n¿Qué desea editar?\n\n1)Nombre\n2)Gerente')
            seleccion = input('Seleccione una opción: ')
            if seleccion not in ('1', '2', '3'):
                raise ValueError ('\nOpcion inválida\n')
            
            campos = []
            valores = []
                        
            match seleccion:
                case '1':
                    nuevo_nombre = validar_entrada('Ingrese el nuevo nombre: ')
                    campos.append('nombre = %s')
                    valores.append(nuevo_nombre)
                    
                case '2':
                    nuevo_gerente = validar_entrada('Ingrese el nuevo gerente: ')
                    campos.append('gerente = %s')
                    valores.append(nuevo_gerente)
                case '3':
                    print('\nOperación cancelada. Volviendo al menú anterior...\n')
                    return

            query = f"UPDATE departamento SET {', '.join(campos)} WHERE id = %s"
            valores.append(id_editar)
            cursor.execute(query, tuple(valores))
            db_conexion.commit()
            print('\nDepartamento actualizado correctamente\n')
        except Exception as err:
            print(f'\nError: {err}\n')
            input('\nPresione ENTER para continuar\n').strip()
        finally:
            cursor.close()
    
    def buscarDepartamento(self, db_conexion):
        try:
            cursor = db_conexion.cursor()
            
            id_buscar = input('\nIngrese el ID del departamento que desee buscar: ')
            if not id_buscar.isdigit():
                print('\nEl ID debe ser un número entero\n')
                return
            id_buscar = int(id_buscar)
            
            query = """
                SELECT id_departamento, nombre_departamento, nombre_gerente FROM departamento
                WHERE id_departamento = %s
            """
            cursor.execute(query, (id_buscar,))
            departamento = cursor.fetchone()
            
            if departamento:
                print('\n¡Departamento encontrado!\n')
                print(f'Departamento ID: {departamento[0]}\nNombre: {departamento[1]}\nGerente: {departamento[2]}')
            else:
                print('\nNo se encontró ningún departamento con ese ID\n')
            
        except Exception as err:
            print(f'\nError: {err}\n')
            input('\nPresione ENTER para continuar\n').strip()
            return None
        finally:
            cursor.close()
    
    def eliminarDepartamento(self, db_conexion):
        try:
            cursor = db_conexion.cursor()
            id_eliminar = input('Ingrese el ID del departamento que desee eliminar: ')
            if not id_eliminar.isdigit():
                print('\nEl ID debe ser un número entero\n')
                return
            id_eliminar = int(id_eliminar)
            cursor.execute("SELECT nombre_departamento FROM departamento WHERE id_departamento = %s", (id_eliminar, ))
            resultado = cursor.fetchone()
            
            if not resultado:
                print('\nNo se encontro ningun departamento con este ID\n')
                input('\nPresione ENTER para continuar\n')
                return None
            print(f'\nDepartamento encontrado: {resultado[0]}')
            confirmar = input('\n¿Está seguro que desea eliminarlo? [s/n]: ').strip().lower()
            if confirmar == 's':
                query = """
                    DELETE FROM departamento WHERE id_departamento = %s
                    """
                cursor.execute(query, (id_eliminar,))
                db_conexion.commit()
                print('\nDepartamento eliminado correctamente\n')
            elif confirmar == 'n':
                print('\nOperación cancelada\n')
            else:
                print('\nOpción inválida. No se realizó ninguna acción.\n')        
            input('\nPresione ENTER para continuar\n')

        except Exception as err:
            print(f'\nError: {err}')
            db_conexion.rollback()
            input('\nPresione ENTER para continuar\n').strip()
            return None
        finally:
            cursor.close()
    
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