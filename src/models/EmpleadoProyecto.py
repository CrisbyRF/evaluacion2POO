from validaciones.funciones import validar_fecha, validar_dato
class EmpleadoProyecto:
    def __init__(self, empleado = None, proyecto = None, rol = '', fecha_inicio = None, fecha_fin = None, fecha_termino = None):
        self.__empleado = empleado
        self.__proyecto = proyecto
        self.__rol = rol #50 caracteres máximo
        self.__fecha_asignacion = fecha_inicio
        self.__fecha_termino = fecha_termino

    @property
    def empleado(self):
        return self.__empleado
    
    @property
    def proyecto(self):
        return self.__proyecto
    
    @property
    def rol (self):
        return self.__rol
    
    @rol.setter
    def rol (self, nuevo_rol):
        if nuevo_rol:
            self.__rol = nuevo_rol
        
    @property
    def fecha_asignacion (self):
        return self.__fecha_asignacion
    
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    def actualizarFechas(self, fecha_incio, fecha_termino = None):
        validar_fecha(fecha_incio)
        self.__fecha_asignacion = fecha_incio
        if fecha_termino:
            validar_fecha(fecha_termino)
            self.__fecha_termino = fecha_termino

    def cambiarRol(self, nuevo_rol, db_conexion = None):
        validar_dato(nuevo_rol)
        if len(nuevo_rol) > 50:
            print('\nPermite un máximo de 50 caracteres\n')
            input('Presione ENTER para continuar\n')
            return False
        self.__rol= nuevo_rol
        if db_conexion and self.__empleado and self.__proyecto:
            if self.__empleado.id_empleado is None:
                print('\nEl empleado no tiene un ID válido\n')
                return False

            if self.__proyecto.id_proyecto is None:
                print('\nEl proyecto no tiene un ID válido\n')
                return False
            try:
                cursor = db_conexion.cursor()
                query = """ 
                        UPDATE empleadoProyecto SET rol = %s
                        WHERE id_empleado = %s AND id_proyecto = %s
                """
                valores = (nuevo_rol, self.__empleado.id_empleado, self.__proyecto.id_proyecto)
                cursor.execute(query, valores)
                db_conexion.commit()
                print(f"\nRol actualizado correctamente a '{nuevo_rol}'\n")
                return True
            except Exception as err:
                print(f"\nError al actualizar el rol: {err}\n")
                input('\nPresione ENTER para continuar\nm')
                return False
            finally:
                cursor.close()
        else:
            print('\nRol actualizado de manera local, sin cambios en la base de datos\n')
            input('\nPresione ENTER para continuar\nm')
            return True

    def mostrarDetalle(self, db_conexion):
        try:
            cursor = db_conexion.cursor(dictionary=True)
            cursor.execute("""
                SELECT e.nombre, p.nombre, ep.rol, ep.fecha_inicio, ep.fecha_termino
                FROM EmpleadoProyecto ep
                JOIN empleado e ON ep.id_empleado = e.id_empleado
                JOIN proyecto p ON ep.id_proyecto = p.id_proyecto
                WHERE e.nombre = %s AND p.nombre = %s
            """, (self.__empleado, self.__proyecto))
            resultado = cursor.fetchone()
            if resultado:
                print(f"\nDetalle de asignación:")
                print(f"- Empleado: {resultado['nombre_empleado']}")
                print(f"- Proyecto: {resultado['nombre_proyecto']}")
                print(f"- Rol: {resultado['rol']}")
                print(f"- Inicio: {resultado['fecha_inicio']}")
                print(f"- Término: {resultado['fecha_fin']}")
            else:
                print("\nNo se encontró la asignación en la base de datos.\n")
        except Exception as e:
            print(f"\nError al mostrar detalle: {e}\n")
        finally:
            cursor.close()