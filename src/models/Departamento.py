from validaciones.funciones import validar_dato, validar_entrada

class Departamento:
    def __init__(self, nombre, gerente = None):
        self.__nombre = nombre # maximo de 150 caracteres
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
    
    def crearDepartamento(self, nombre, nombre_gerente, db_conexion):
        validar_dato(nombre)
        validar_dato(nombre_gerente)

        if len(nombre) > 150:
            print('\n¡El nombre del departamento no puede superar los 150 caracteres!\n')
            input('\nPresione ENTER para continuar\n')
            return None

        try:
            cursor = db_conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM empleado WHERE cargo = 'Gerente'")
            if cursor.fetchone()[0] == 0:
                print('\nNo hay gerentes registrados en el sistema.\n')
                input('\nPresione ENTER para continuar\n')
                return None

            cursor.execute("""
                SELECT id_empleado FROM empleado 
                WHERE nombre = %s AND cargo = 'Gerente'
            """, (nombre_gerente,))
            resultado = cursor.fetchone()

            if not resultado:
                print('\nEl nombre ingresado no corresponde a un gerente registrado.\n')
                input('\nPresione ENTER para continuar\n')
                return None

            id_gerente = resultado[0]

            query = """
                INSERT INTO departamento (nombre, id_gerente)
                VALUES (%s, %s)
            """
            cursor.execute(query, (nombre, id_gerente))
            db_conexion.commit()

            self.__nombre = nombre
            self.__gerente = id_gerente

            print('\nDepartamento creado exitosamente.\n')
            return self

        except Exception as err:
            print(f'\nError al crear el departamento: {err}\n')
            db_conexion.rollback()
            input('\nPresione ENTER para continuar\n')
            return None

        finally:
            cursor.close()
    
    def editarDepartamento(self, db_conexion):
        try:
            cursor = db_conexion.cursor()
            query = """SELECT id_departamento, nombre, id_gerente FROM departamento"""
            cursor.execute(query)
            departamentos = cursor.fetchall()
            
            for departamento in departamentos:
                print(f'\nID: {departamento[0]} | Nombre: {departamento[1]} | Gerente: {departamento[2]}')
            id_editar = input('\nIngrese el ID del departamento que desee editar: ')
            id_editar = int(id_editar)
            cursor.execute("SELECT COUNT(*) FROM departamento WHERE id_departamento = %s", (id_editar,))
            existe = cursor.fetchone()[0]
            if existe == 0:
                print('\nEl ID ingresado no existe\n')
                return
            print('\n¿Qué desea editar?\n\n1) Nombre\n2) Gerente\n3) Volver atrás')
            seleccion = input('Seleccione una opción: ')
            if seleccion not in ('1', '2', '3'):
                raise ValueError ('\nOpcion inválida\n')
            
            campos = []
            valores = []
                        
            match seleccion:
                case '1':
                    nuevo_nombre = validar_entrada('Ingrese el nuevo nombre: ')
                    if len(nuevo_nombre) > 150:
                        print('\n¡El nombre no puede superar los 150 caracters!\n')
                        return
                    campos.append('nombre = %s')
                    valores.append(nuevo_nombre)
                    
                case '2':
                    nuevo_gerente = validar_entrada('Ingrese el nuevo gerente: ')
                    cursor.execute("""
                        SELECT id_empleado FROM empleado 
                        WHERE nombre = %s AND cargo = 'Gerente'
                    """, (nuevo_gerente,))
                    resultado = cursor.fetchone()
                    if not resultado:
                        print('\nEl nombre ingresado no corresponde a un gerente registrado.\n')
                        return
                    id_gerente = resultado[0]
                    campos.append('id_gerente = %s')
                    valores.append(id_gerente)
                case '3':
                    print('\nOperación cancelada. Volviendo al menú anterior...\n')
                    return

            query = f"UPDATE departamento SET {', '.join(campos)} WHERE id_departamento = %s"
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
                SELECT id_departamento, nombre, id_gerente FROM departamento
                WHERE id_departamento = %s
            """
            cursor.execute(query, (id_buscar,))
            departamento = cursor.fetchone()
            
            if departamento:
                cursor.execute("SELECT nombre FROM empleado WHERE id_empleado = %s", (departamento[2],))
                nombre_gerente = cursor.fetchone()
                nombre_gerente = nombre_gerente[0] if nombre_gerente else 'No asignado'
                print('\n¡Departamento encontrado!\n')
                print(f'Departamento ID: {departamento[0]}\nNombre: {departamento[1]}\nGerente: {nombre_gerente}')
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
            cursor.execute("SELECT nombre FROM departamento WHERE id_departamento = %s", (id_eliminar, ))
            resultado = cursor.fetchone()
            
            if not resultado:
                print('\nNo se encontro ningun departamento con este ID\n')
                input('\nPresione ENTER para continuar\n')
                return None
            cursor.execute("""
                SELECT e.nombre FROM empleado e
                JOIN departamento d ON e.id_empleado = d.id_gerente
                WHERE d.id_departamento = %s
            """, (id_eliminar,))
            gerente = cursor.fetchone()
            nombre_gerente = gerente[0] if gerente else 'No asignado'
            print(f'\nDepartamento encontrado: {resultado[0]} | Gerente: {nombre_gerente}')
            print(f'\nDepartamento encontrado: {resultado[0]}')
            confirmar = input('\n¿Está seguro que desea eliminarlo? [s/n]: ').strip().lower()
            if confirmar == 's':
                cursor.execute("SELECT COUNT(*) FROM empleado WHERE id_departamento = %s", (id_eliminar,))
                empleados_asignados = cursor.fetchone()[0]

                if empleados_asignados > 0:
                    print('\nNo se puede eliminar el departamento porque tiene empleados asignados.\n')
                    input('\nPresione ENTER para continuar\n')
                    return
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
    
    def asignarEmpleado(self, empleado, db_conexion):
        if empleado.departamento is not None:
            print(f'\nEl empleado ya pertenece al departamento: {empleado.departamento.nombre}')
            return False

        cursor = db_conexion.cursor()
        query = "UPDATE empleado SET id_departamento = %s WHERE id_empleado = %s"
        cursor.execute(query, (self.id_departamento, empleado.id_empleado))
        db_conexion.commit()
        cursor.close()

        empleado.asignarDepartamento(self)
        print(f'\nEmpleado {empleado.nombre} asignado al departamento {self.nombre}\n')
        return True
    
    def desasignarEmpleado(self, empleado, db_conexion):
        if empleado.departamento != self:
            print(f'\nEl empleado {empleado.nombre} no pertenece a este departamento\n')
            return

        cursor = db_conexion.cursor()
        query = "UPDATE empleado SET id_departamento = NULL WHERE id_empleado = %s"
        cursor.execute(query, (empleado.id_empleado,))
        db_conexion.commit()
        cursor.close()

        empleado.asignarDepartamento(None)
        print(f'\nEl empleado {empleado.nombre} ha sido desasignado del departamento {self.nombre}\n')