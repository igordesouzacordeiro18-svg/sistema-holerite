import sqlite3
from armazenamento import carregar_funcionarios , conectar


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT, 
        cargo TEXT,
        salario REAL
    )
    """)

    conexao.commit()
    conexao.close()

def obter_cargos():
    return {
        '1': {'nome': 'Aprendiz de TI', 'salario': 800},
        '2': {'nome': 'Estagiário de TI', 'salario': 2000},
        '3': {'nome': 'Developer Júnior', 'salario': 3500},
        '4': {'nome': 'Developer Pleno', 'salario': 6500},
        '5': {'nome': 'Developer Sênior', 'salario': 9000},
        '6': {'nome': 'Gestor de TI', 'salario': 12000},
        '7': {'nome': 'Diretor Geral', 'salario': 20000}
    }

def cadastrar_funcionario():

    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Nome: ")

    print('\nQual o seu cargo: \n')
    print('1 - Aprendiz de TI')
    print('2 - Estagiário de TI')
    print('3 - Developer Junior')
    print('4 - Developer Pleno')
    print('5 - Developer Sênior')
    print('6 - Gestor de TI')
    print('7 - Diretor Geral')

    opcao= input('Digite uma opção: ')

    cargos = obter_cargos()

    if opcao not in cargos:
        print('\nOpção inválida!Tente novamente.')
        conexao.close()
        return

    dados_cargo = cargos[opcao]

    cursor.execute("""
                   INSERT INTO funcionarios(nome, cargo, salario )
                   VALUES(?, ?, ?)
                   """,(nome, dados_cargo["nome"], dados_cargo["salario"]))
    
    conexao.commit()
    conexao.close()

    print('\nFuncionário cadastrado:')
    print(f'Nome: {nome}')
    print(f'Cargo: {dados_cargo["nome"]}')
    print(f'Salário: R$ {dados_cargo["salario"]:.2f}')


def listar_funcionarios():
    funcionarios = carregar_funcionarios()

    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    print("\n=== FUNCIONÁRIOS CADASTRADOS ===\n")

    for f in funcionarios:
        print(f"ID: {f['id']}")
        print(f"Nome: {f['nome']}")
        print(f"Cargo: {f['cargo']}")
        print(f"Salário: R$ {f['salario']:.2f}")
        print("-" * 30)

def remover_funcionario():
    funcionarios = carregar_funcionarios()
    
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    print('\n=== REMOVER FUNCIONÁRIO ===\n')

    for f in funcionarios:
        print(f"{f['id']} - {f['nome']} ({f['cargo']})")

    escolha = input('\nDigite o número do funcionário que deseja remover: ')

    if not escolha.isdigit():
        print('Entrada inválida.')
        conexao.close()
        return
    
    escolha = int(escolha)

    for f in funcionarios:
        if f["id"] == escolha:
            
            cursor.execute("DELETE FROM funcionarios WHERE id = ?",(escolha,))
            conexao.commit()

            print(f'\nFuncionário {f["nome"]} removido com sucesso! ')
            conexao.close()
            return
        
    print('\nFuncionário não encontrado. ')
    conexao.close()

def editar_funcionario():
    funcionarios = carregar_funcionarios()
    
    if not funcionarios:
        print('Nenhum funcionário para editar. ')
        return
    
    conexao = conectar()
    cursor = conexao.cursor()
    
    print('\n=== EDITAR  FUNCIONÁRIO ===')

    for f in funcionarios:
        print(f"{f['id']} - {f['nome']} ({f['cargo']})")

    escolha = input('\nDigite o número do funcionário que deseja editar: ')

    if not escolha.isdigit():
        print('Entrada inválida.')
        conexao.close()
        return
    
    escolha = int(escolha)

    for f in funcionarios:
        if f["id"] == escolha:
           
            novo_nome = f["nome"]
            novo_cargo= f["cargo"]
            novo_salario = f["salario"]
            
            print('\nO que deseja editar?\n')
            print('1 - Nome')
            print('2 - Cargo')
            print('3 - Salário')

            opcao = input('\nEscolha uma opção: ')

            if opcao == '1':
                novo_nome = input('Digite o novo nome: ')
            
            elif opcao == '2':

                cargos = obter_cargos()

                print("\nEscolha o novo cargo: \n")
                for k, v in cargos.items():
                    print(f"{k} - {v['nome']}")
                
                escolha_cargo = input('\nDigite uma opção:\n ')


                if escolha_cargo not in cargos:
                    print('Opção inválida.')
                    conexao.close()
                    return
                
                novo_cargo = cargos[escolha_cargo]["nome"]
                novo_salario = cargos[escolha_cargo]["salario"]
                
            elif opcao == '3':
                try:
                    novo_salario = float(input('Digite o novo salário: ').replace(',' , '.'))
                    
                    if novo_salario <= 0:
                        print("Salário inválido.")
                        conexao.close()
                        return

                except ValueError:
                    print('Salário inválido.')
                    conexao.close()
                    return
            
        
            else:
                print('Opção inválida.')
                conexao.close()
                return
            
            cursor.execute("""
                        UPDATE funcionarios
                        set nome = ?, cargo = ?, salario = ?
                        WHERE id = ? 
                        """, (novo_nome, novo_cargo, novo_salario, escolha))
            
            conexao.commit()
            conexao.close()

            print(f"\nFuncionário {novo_nome} atualizado com sucesso!\n")
            return
        
    print('\nFuncionário não encontrado.')
    conexao.close()
            

def buscar_funcionario():
    conexao = conectar()
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    
    print('\n=== BUSCAR FUNCIONÁRIO ===\n')
    
    escolha = input('Digite o ID do funcionário: ')

    if not escolha.isdigit():
            print('Entrada inválida.')
            conexao.close()
            return
    
    escolha = int(escolha)
    
    cursor.execute("SELECT * FROM funcionarios WHERE id = ?", (escolha,))
    funcionario = cursor.fetchone()

    
    if funcionario:
        f = dict(funcionario)
        print('\n=== FUNCIONÁRIO ENCONTRADO ===')
        print(f'\nID:  {f["id"]}')
        print(f'Nome: {f["nome"]}')
        print(f'Cargo: {f["cargo"]}')
        print(f'Salário: R$ {f["salario"]:.2f}')
    
    else:
        print("\nFuncionário não encontrado")
        
    conexao.close()

