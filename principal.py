from config.ConexionBd import ConexionBd
from src.models.Departamento import Departamento
from validaciones.funciones import validar_email, validar_entrada, validar_telefono

database = None

def menu_gerente():
    try:
        database = ConexionBd('localhost', 'root', '', 'ecotech_solutions') #colocar datos de la base de datos
        conexion = database.conectar()
        
        
        
        while True:
            d = Departamento('', [], '')
            d.crearDepartamento('Recursos humanos', ' Cristóbal Rey', conexion)
            print('==========================================')
            print("SISTEMA DE GESTIÓN - ECHOTECH SOLUTIONS")
            print('==========================================')
            print("1. Crear empleado")
            print("2. Listar empleado")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("5. Buscar empleado")
            print("6. Salir")
            print('==========================================')
            
            try:
                
                seleccion = input('\nSelecciona una opción: ').strip()
                
                match seleccion:
                    case '1':
                        try:
                            cursor = conexion.cursor()
                            query = """
                            INSERT INTO empleado (nombre_empleado, direccion_empleado, telefono_empleado, email_empleado)
                            VALUES (%s, %s, %s, %s)
                            """
                            nombre_empleado = validar_entrada('Nombre completo: ')
                            direccion = validar_entrada("Dirección: ")  
                            telefono = validar_telefono("Teléfono: ")
                            email = validar_email("Email: ")
                            valores = (nombre_empleado, direccion, telefono, email)
                            cursor.execute(query, valores)
                            conexion.commit()
                            cursor.close()
                            print('\nEmpleado agregado con exito!')
                            input('\nPresione ENTER para continuar\n')
                        except ValueError as err:
                            print(f'\nError, intente nuevamente: {err}\n')
                            
            except ValueError as err:
                print('Error de validación: {e}')
        
    finally:
        if database:
            database.desconectar()
menu_gerente()