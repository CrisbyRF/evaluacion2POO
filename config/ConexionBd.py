import mysql.connector
from mysql.connector import Error

import time

class ConexionBd:
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database
        self.__cnx = None
        
    def conectar(self):
        try:
            if self.__cnx is None or not self.__cnx.is_connected():
                self.__cnx = mysql.connector.connect(
                    host=self.__host,
                    user=self.__user,
                    password=self.__password,
                    database=self.__database
                )
            return self.__cnx
        except Error as err:
            print(f'\nError al conectar: {err}\n')
            raise
    
    def desconectar(self):
        try:
            if self.__cnx is None or not self.__cnx.is_connected():
                self.__cnx.close()
                time.sleep(1)
                print('\nConexión cerrada\n')
        except Error as e:
            print(f'\nError al cerrar la conexión: {e}\n')
    
    def get_conectar(self):
        if self.__cnx is None or not self.__cnx.is_connected():
            return self.conectar()
        return self.__cnx