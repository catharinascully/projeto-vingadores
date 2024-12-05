import os 
from vingador import Vingador
from database import Database
from datetime import datetime
from buscar_heroi import verificar_heroi_no_banco

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
        print("7. Mandato de prisão")
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

            db.disconnect()
    
    @staticmethod
    def convocar():
        try:
            db = Database()
            db.connect()

            nome_heroi = input("Nome do herói que você deseja convocar: ")
            heroi_id = verificar_heroi_no_banco(nome_heroi)

            if not heroi_id:
                print("Herói não encontrado")
                return
                
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

    @staticmethod
    def aplicar_tornozeleira():
        try: 
            db = Database()
            db.connect()

            nome_heroi = input("Nome do herói que você quer aplicar a tornozeleira: ")
            id_heroi = verificar_heroi_no_banco(nome_heroi)

            status = input("Status da tornozeleira (ativo ou inativo): ")

            data_ativacao = input("Data de ativação (dd/mm/aaaa) ou aperte Enter para deixar a data de hoje: ")
            if data_ativacao:
                data_ativacao = datetime.strptime(data_ativacao, "%d/%m/%Y")
            else:
                data_ativacao = datetime.now()
            
            data_desativacao = input("Data de desativação (dd/mm/aaaa) ou aperte Enter para deixar em branco: ")
            if data_desativacao:
                data_desativacao = datetime.strptime(data_desativacao, "%d/%m/%Y")
            else:
                data_desativacao = None

            query = "INSERT INTO tornozeleira (id_heroi, status, data_ativacao, data_desativacao) VALUES (%s, %s, %s, %s)"
            values = (id_heroi, status, data_ativacao, data_desativacao)
            db.execute_query(query, values)


            print("A tornozeleira foi aplicada")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            db.disconnect()

    @staticmethod
    def aplicar_chip_gps():
        try: 
            db = Database()
            db.connect()

            nome_heroi = input("Nome do herói que você deseja informar a localização: ")
            heroi_id_tornozeleira = verificar_heroi_no_banco(nome_heroi)

            query_tornozeleira = "SELECT id_tornozeleira FROM tornozeleira WHERE id_heroi = %s"
            resultado_tornozeleira = db.select(query_tornozeleira, (heroi_id_tornozeleira,))

            if not resultado_tornozeleira:
                print("Tornozeleira não encontrada para esse herói.")
            else:
                id_tornozeleira = resultado_tornozeleira[0][0]

            localizacao_atual = input("Localização atual do vingaodr: ")
            ultima_localizacao = input("Última localização do vingador: ")

            query = "INSERT INTO chip_gps (localizacao_atual, ultima_localizacao, id_tornozeleira) VALUES (%s, %s, %s)"
            values = (localizacao_atual, ultima_localizacao, id_tornozeleira)
            db.execute_query(query, values)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            db.disconnect()

    @staticmethod
    def mandato_de_prisao():
        try: 
            db = Database()
            db.connect()

            nome_heroi = input("Nome do herói que você quer prender: ")
            heroi_id_mandato = verificar_heroi_no_banco(nome_heroi)

            motivo_mandato = input("Motivo do mandato: ")
            status = input("Status do mandato (ativo, cumprido ou cancelado): ")
            data_emissao = input("Data de emissão (dd/mm/aaaa) ou aperte Enter para deixar a data de hoje: ")
            if data_emissao:
                data_emissao = datetime.strptime(data_emissao, "%d/%m/%Y")
            else:
                data_emissao = datetime.now()

            query = "INSERT INTO mandato_de_prisao (heroi_id_mandato, motivo_mandato, data_emissao, status) VALUES (%s, %s, %s, %s)"
            values = (heroi_id_mandato, motivo_mandato, data_emissao, status)
            db.execute_query(query, values)

            print("O mandato foi emitido")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        finally:
            db.disconnect()

            #