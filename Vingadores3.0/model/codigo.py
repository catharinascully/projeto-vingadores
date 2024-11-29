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

            db.execute_query(query, values)
        except Exception as e:
            print(f"Erro ao salvar vingador no banco de dados: {e}")
        finally:
            db.disconnect()

        print(f"\nVingador {nome_heroi} cadastrado com sucesso!")
 
    @staticmethod
    def listar_vingadores():
        Interface.limpar_tela()
        print("=== Lista de Vingadores ===")
        if not Vingador.lista_vingadores:
            print("Nenhum vingador cadastrado.")
        else:
            print(f'{"Nome do Herói".ljust(20)} | {"Nome Real".ljust(20)} | {"Categoria".ljust(15)} | '
                  f'{"Tornozeleira".ljust(15)} | {"Chip GPS"}')
            print("-" * 80)
            for vingador in Vingador.lista_vingadores:
                print(vingador)
 
    @staticmethod
    def detalhes_vingador():
        nome = input("Digite o Nome do Herói ou Nome Real: ")
        vingador = next((v for v in Vingador.lista_vingadores if v.nome_heroi == nome or v.nome_real == nome), None)
        if vingador:
            print("\n=== Detalhes do Vingador ===")
            print(vingador.detalhes())
        else:
            print("Vingador não encontrado.")
 
    @staticmethod
    def acao_em_vingador(acao):
        nome = input("Digite o Nome do Herói ou Nome Real: ")
        vingador = next((v for v in Vingador.lista_vingadores if v.nome_heroi == nome or v.nome_real == nome), None)
        if vingador:
            resultado = acao(vingador)
            print(resultado)
        else:
            print("Vingador não encontrado.")

        try: 
            db = Database
            db.connect()
            
            motivo = input("Motivo da convocacao: ")
            data_convocacao = datetime.now()
            data_comparecimento = ("Data de comparecimento (DD/MM/AAAA): ")
            status = input("Status (Presente, ausente ou comparecido): ")

            query = "INSERT INTO (motivo, data_convocacao, data_comparecimento, status) values (%s, %s, %s, %s)"
            values = (motivo, data_convocacao, data_comparecimento, status)

            data_comparecimento = datetime.strptime(data_comparecimento, "%d/%m/%Y")

            db.execute_query(query, values)
        except Exception as e:
            print(f"Erro ao salvar vingador no banco de dados: {e}")
        finally:
            db.disconnect()