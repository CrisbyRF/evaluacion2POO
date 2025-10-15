import re
import datetime

def validar_dato (dato):
    while True:
        if not dato:
            print('\n¡El campo no puede quedar vacío!\n')
            continue
        if any(char in dato for char in ['<', '>', ';', '--', '/*', '*/']):
            print('\nCaracteres no permitidos\n')
            continue
        return dato
    
def validar_entrada(prompt):
    while True:
        entrada = input(prompt).strip()
        
        if not entrada:
            print('\n¡El campo no puede quedar vacío!\n')
            continue
        if any(char in entrada for char in ['<', '>', ';', '--', '/*', '*/']):
            print('\nCaracteres no permitidos\n')
            continue
        
        return entrada
        
def validar_email(email_recibido):
    if not email_recibido:
        return False, "El email no puede estar vacío"
    
    email_recibido = email_recibido.strip()
    
    patron = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9][a-zA-Z0-9.-]*\.[a-zA-Z]{2,}$'
    
    if not re.match(patron, email_recibido):
        print('\nEmail inválido\n')
        return False

    try:
        dominio = email_recibido('@')[1]
        if dominio.startswith('-') or dominio.endswith('-'):
            return False, "\nEl dominio no puede empezar o terminar con guión\n"
    except IndexError:
        return False, "\nFormato de email inválido\n"
    
    return True, "\nEmail válido\n"

def validar_fecha(prompt):
    while True:
        fecha = input(prompt).strip()
        
        if not fecha:
            print('\n¡El campo no puede quedar vacío!\n')
            return None
        try:
            datetime.strptime(fecha, '%d-%m-%Y')
            return fecha
        except ValueError:
            print('\nFormato de fecha inválido, utilice el formato DD-MM-YYYY\n')