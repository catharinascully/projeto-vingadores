import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv
 
class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('BD_HOST')
        self.user = getenv('BD_USER')
        self.password = getenv('BD_PSWD')
        self.database = getenv('BD_DATABASE')
 
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexão com o banco de dados realizada com sucesso")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
    
    def disconnect(self):
        self.connection.close()
        print('Conexão com o banco de dados encerrada com sucesso')

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print('Query executada com sucesso')
            return self.cursor
        except Error as e:
            print(f'Erro: {e}')
            return None
        
    #código