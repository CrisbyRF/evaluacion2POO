from models.Empleado import Empleado
from models.Departamento import Departamento
from src.models.Proyecto import Proyecto
from models.Gerente import Gerente
from models.RegistroHorario import RegistroHorario
from config import ConexionBd
from validaciones.funciones import validar_email, validar_entrada
import sys

database = None

try:
    database = ConexionBd() #colocar datos de la base de datos
    conexion = database.conectar()
    
    while True:
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
                        nombre_empleado = validar_entrada('Nombre completo: ')
                        direccion = validar_entrada("Dirección: ")  
                        telefono = validar_entrada("Teléfono: ")
                        email = validar_email("Email: ")
                    except ValueError as err:
                        print(f'\nError, intente nuevamente\n')
                        
        except ValueError as err:
            print('Error de validación: {e}')
    
finally:
    if database:
        database.desconectar()