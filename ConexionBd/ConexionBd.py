import mysql.connector
import time

class ConexionBd:
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._cnx = None
        
    def conectar(self):
        try:
            if self._cnx is None or not self.__cnx.is_connected():
                self._cnx = mysql.connector.connect(
                    host=self._host,
                    user=self._user,
                    password=self._password,
                    database=self._database
                )
            return self._cnx
        except mysql.connector.Error as err:
            print(f'\nError al conectar: {err}\n')
            raise
    
    def desconectar(self):
        try:
            if self._cnx is None or not self._cnx.is_connected():
                self._cnx.close()
                time.sleep(1)
                print('\nConexión cerrada\n')
        except ValueError as e:
            print(f'\nError al cerrar la conexión: {e}\n')
    
    def get_conectar(self):
        if self._cnx is None or not self._cnx.is_connected():
            return self.conectar()
        return self._cnx