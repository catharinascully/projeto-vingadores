from codigo import Interface

def main():

    while True:
        opcao = Interface.menu()
        if opcao == "1":
            Interface.cadastrar_vingador()
        elif opcao == "2":
            Interface.listar_vingadores()
        elif opcao == "3":
            Interface.detalhes_vingador()
        elif opcao == "4":
            Interface.convocar()
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