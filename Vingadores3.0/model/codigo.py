import os
from vingador import Vingador
from database import Database
from datetime import datetime


class Interface:
    @staticmethod
    def limpar_tela():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def menu():
        Interface.limpar_tela()
        print("=== Sistema dos Vingadores ===")
        print("1. Cadastrar Vingador")
        print("2. Listar Vingadores")
        print("3. Detalhar Vingador")
        print("4. Convocar Vingador")
        print("5. Aplicar Tornozeleira")
        print("6. Aplicar Chip GPS")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        return opcao

    @staticmethod
    def cadastrar_vingador():
        Interface.limpar_tela()
        print("=== Cadastro de Vingador ===")
        nome_heroi = input("Nome do Herói: ")
        nome_real = input("Nome Real: ")

        while True:
            categoria = input("Categoria (Humano, Meta-humano, Alienígena, Deidade): ")
            if categoria in Vingador.CategoriaVingadores.CATEGORIAS_VALIDAS:
                break
            print("Categoria inválida! Tente novamente.")

        poderes = input("Poderes (separe por vírgulas): ").split(", ")
        poder_principal = input("Poder Principal: ")
        fraquezas = input("Fraquezas (separe por vírgulas): ").split(", ")

        while True:
            try:
                nivel_forca = int(input("Nível de Força (0 a 10000): "))
                if 0 <= nivel_forca <= 10000:
                    break
                print("Nível de força inválido! Deve estar entre 0 e 10000.")
            except ValueError:
                print("Por favor, insira um número válido.")

        novo_vingador = Vingador(nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca)
        Vingador.lista_vingadores.append(novo_vingador)

        try:
            db = Database()
            db.connect()

            query = "INSERT INTO heroi (nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (nome_heroi, nome_real, categoria, ', '.join(poderes), poder_principal, ', '.join(fraquezas), nivel_forca)

            cursor = db.connection.cursor()
            cursor.execute(query, values)

            db.connection.commit()

            Vingador(nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca)

        except Exception as e:
            print(f"Erro ao salvar vingador no banco de dados: {e}")
        finally:
            db.disconnect()

        print(f"Vingador(a) '{nome_heroi}' cadastrado com sucesso.")

    @staticmethod
    def listar_vingadores():
        Interface.limpar_tela()
        print("=== Lista de Vingadores ===")
        try:
            db = Database()
            db.connect()

            query = 'SELECT heroi_id, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca FROM heroi'
            herois = db.select(query)
            if not herois:
                print("Nenhum vingador cadastrado.")
            else:
                print(f'{"Nome do Herói".ljust(20)} | {"Nome Real".ljust(20)} | {"Categoria".ljust(15)} | '
                    f'{"Tornozeleira".ljust(15)} | {"Chip GPS"}')
                print("-" * 95)
                for heroi in herois:
                    vingador = Vingador(*heroi[1:])
                    print(vingador)
        except Exception as e:
            print(f'Erro: {e}')
        finally:
            db.disconnect()

    @staticmethod
    def detalhes_vingador():
        try:
            nome = input("Digite o Nome do Herói ou Nome Real: ")

            db = Database()
            db.connect()

            query = "SELECT nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca FROM heroi WHERE nome_heroi = %s OR nome_real = %s"

            heroi_result = db.select(query, (nome, nome))

            if heroi_result:
                vingador = Vingador(
                    heroi_result[0][0], heroi_result[0][1], heroi_result[0][2], heroi_result[0][3], heroi_result[0][4], 
                    heroi_result[0][5], heroi_result[0][6]
                )

                print("\n=== Detalhes do Vingador ===")
                print(vingador.detalhes())
            else:
                print("Vingador não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            db.disconnect()
    
    @staticmethod
    def convocar():
        try:
            db = Database()
            db.connect()

            nome_heroi = input("Nome do herói que você deseja convocar: ")
            query_heroi = "SELECT heroi_id FROM heroi WHERE nome_heroi = %s"
            heroi_id_resultado = db.select(query_heroi, (nome_heroi,))

            if not heroi_id_resultado:
                print("Herói não encontrado")
                return
                
            heroi_id = heroi_id_resultado[0][0]

            motivo = input("Motivo da convocação: ")
            data_convocacao = datetime.now()
                
            data_comparecimento_str = input("Data do comparecimento (dd/mm/aaaa) ou aperte Enter para deixar em branco: ")
            if data_comparecimento_str:
                data_comparecimento = datetime.strptime(data_comparecimento_str, "%d/%m/%Y")
            else:
                data_comparecimento = None
                
            status = input("Status (pendente, ausente ou comparecido): ")

            query = "INSERT INTO convocacao (heroi_id, motivo, data_convocacao, data_comparecimento, status) VALUES (%s, %s, %s, %s, %s)"
            values = (heroi_id, motivo, data_convocacao, data_comparecimento, status)
            db.execute_query(query, values)

            print("Convocação realizada com sucesso!")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            db.disconnect()

