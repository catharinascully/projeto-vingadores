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
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexão com o banco de dados realizada com sucesso\n")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print('Conexão com o banco de dados encerrada com sucesso')
        else:
            print("Nenhuma conexão para fechar.")

    def execute_query(self, query, values=None):
        if not self.connection:
            print("Database não estabelecida")
            return None
        
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            print('Query executada com sucesso')
            return self.cursor
        except Error as e:
            print(f'Erro ao executar a query: {e}')
            return None

    def select(self, query, values = None):
        if not self.connection:
            print("Não há conexão com o banco de dados")
            return None

        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Erro ao executar a query: {e}")
            return None
        

    def verificar_heroi_no_banco(self, nome_heroi):
        try:
            db = Database()
            db.connect()
            
            query = "SELECT heroi_id FROM heroi WHERE nome_heroi = %s"
            resultado = db.select(query, (nome_heroi,))
            
            db.disconnect()
            
            if resultado:
                return resultado[0][0]
            else:
                return None
        
        except Exception as e:
            print(f"Erro ao consultar herói no banco: {e}")
            return None