from holerite import gerar_holerite
from funcionarios import cadastrar_funcionario, listar_funcionarios,remover_funcionario, editar_funcionario, buscar_funcionario
import os

def limpar():
    os.system('cls')


def pausar():
        input("\nPressione ENTER para continuar...")

while True:
    limpar()
    print("\n1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Gerar holerite")
    print("4 - Remover funcionário")
    print("5 - Buscar funcionário")
    print("6 - Editar funcionário")
    print("7 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_funcionario()
        pausar()

    elif opcao == "2":
        listar_funcionarios()
        pausar()

    elif opcao == "3":
        gerar_holerite()
        pausar()
    
    elif opcao == "4":
        remover_funcionario()
        pausar()
    
    elif opcao == "5":
        buscar_funcionario()
        pausar()
    
    elif opcao == "6":
        editar_funcionario()
        pausar()

    elif opcao == "7":
        print('Programa encerrado.')
        break

    else:
        print("Opção inválida")