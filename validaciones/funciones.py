import re
import datetime

def validar_dato (prompt):
    while True:
        if not prompt:
            print('\n¡El campo no puede quedar vacío!\n')
            continue
        if any(char in prompt for char in ['<', '>', ';', '--', '/*', '*/']):
            print('\nCaracteres no permitidos\n')
            continue
        return prompt
    
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
        
def validar_email(prompt):
    email = input(prompt.strip())
    
    if not email:
        return False, 'El email no puede estar vacío'
    
    patron = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9][a-zA-Z0-9.-]*\.[a-zA-Z]{2,}$'
    
    if not re.match(patron, email):
        print('\nEmail inválido\n')
        return False

    try:
        dominio = email.split('@')[1]
        if dominio.startswith('-') or dominio.endswith('-'):
            return False, "\nEl dominio no puede empezar o terminar con guión\n"
    except IndexError:
        return False, "\nFormato de email inválido\n"
    
    return email

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

def validar_telefono(prompt):
    import re
    patron = r'^(\+56)?(9\d{8})$'
    while True:
        telefono = input(prompt).strip()
        if not telefono:
            print('\n¡El campo no puede quedar vacío!\n')
            continue
        if any(char in telefono for char in ['<', '>', ';', '--', '/*', '*/']):
            print('\nCaracteres no permitidos\n')
            continue
        if not re.match(patron, telefono):
            print('\nNúmero inválido. Debe tener formato +569XXXXXXXX o 9XXXXXXXX\n')
            continue
        return telefono
    