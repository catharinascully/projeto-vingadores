from codigo import Interface
#from vingador import Vingador

def main():
    # Pré-cadastrados
    #Vingador.lista_vingadores = [
    #    Vingador("Thor", "Thor Odinson", "Deidade", ["Força", "Raio"], "Mjolnir", ["Arrogância"], 9000),
    #    Vingador("Hulk", "Bruce Banner", "Meta-humano", ["Força", "Regeneração"], "Transformação", ["Raiva"], 10000)
    #]

    while True:
        opcao = Interface.menu()
        if opcao == "1":
            Interface.cadastrar_vingador()
        elif opcao == "2":
            Interface.listar_vingadores()
        elif opcao == "3":
            Interface.detalhes_vingador()
        elif opcao == "4":
            Interface.acao_em_vingador(lambda v: v.convocar())
        elif opcao == "5":
            Interface.acao_em_vingador(lambda v: v.aplicar_tornozeleira())
        elif opcao == "6":
            Interface.acao_em_vingador(lambda v: v.aplicar_chip_gps())
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()

    #código também 12345