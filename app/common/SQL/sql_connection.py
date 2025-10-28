from .config_SQL import NAME_DB
import mysql.connector

class ConnectionMySQL:

    def __init__(self ,name_SQL_DB = NAME_DB ):
        self.mydb = mysql.connector.connect(
            host="localhost",   
            user="root",         
            password="",          
            database=name_SQL_DB 
            )
        
    def connection_to_MySQL(self):
        pass
        
