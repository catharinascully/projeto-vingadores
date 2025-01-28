from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/ola")
def hello_world():
    return "<p>Olá, mundo!</p>"


# from model/codigo import Interface

# def main():

#     while True:
#         opcao = Interface.menu()
#         if opcao == "1":
#             Interface.cadastrar_vingador()
#         elif opcao == "2":
#             Interface.listar_vingadores()
#         elif opcao == "3":
#             Interface.detalhes_vingador()
#         elif opcao == "4":
#             Interface.convocar()
#         elif opcao == "5":
#             Interface.aplicar_tornozeleira()
#         elif opcao == "6":
#             Interface.aplicar_chip_gps()
#         elif opcao == "7":
#             Interface.mandado_de_prisao()
#         elif opcao == "0":
#             print("Encerrando o sistema...")
#             break
#         input("\nPressione Enter para continuar...")

# if __name__ == "__main__":
#     main()