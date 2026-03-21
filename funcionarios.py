from armazenamento import carregar_funcionarios, salvar_funcionarios

def obter_cargos():
    return {
        '1': {'nome': 'Aprendiz de TI', 'salario': 800},
        '2': {'nome': 'Estagiário de TI', 'salario': 2000},
        '3': {'nome': 'Developer junior', 'salario': 3500},
        '4': {'nome': 'Developer Pleno', 'salario': 6500},
        '5': {'nome': 'Developer Sênior', 'salario': 9000},
        '6': {'nome': 'Gestor de TI', 'salario': 12000},
        '7': {'nome': 'Diretor Geral', 'salario': 20000}
    }

def cadastrar_funcionario():
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
        print('\nOpção inválida!')
        return

    dados_cargo = cargos[opcao]
    cargo = dados_cargo["nome"]
    salario = dados_cargo["salario"]

    funcionarios = carregar_funcionarios()
    
    if funcionarios:
        novo_id = max(f["id"] for f in funcionarios)+1
    
    else:
        novo_id = 1

    print('\nFuncionário cadastrado: \n')
    print(f'ID: {novo_id}')
    print("Nome:",nome)
    print("Cargo:",cargo)
    print(f"Salário: R${salario:.2f}")

    novo_funcionario = {
        "id" : novo_id,
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }

    funcionarios.append(novo_funcionario)

    salvar_funcionarios(funcionarios)


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
        print('Nenhum funcionário para remover. ')
        return

    print('\n=== REMOVER FUNCIONÁRIO ===\n')

    for f in funcionarios:
        print(f"{f['id']} - {f['nome']} ({f['cargo']})")

    escolha = input('\nDigite o número do funcionário que deseja remover: ')

    if not escolha.isdigit():
        print('Entrada inválida.')
        return
    
    escolha = int(escolha)

    for f in funcionarios:
        if f["id"] == escolha:
            funcionarios.remove(f)
            salvar_funcionarios(funcionarios)
            print(f'\nFuncionário {f["nome"]} removido com sucesso! ')
            return
        
    print('\nFuncionário não encontrado. ')

def editar_funcionario():
    funcionarios = carregar_funcionarios()
    if not funcionarios:
        print('Nenhum funcionário para editar. ')
        return
    
    print('\n=== EDITAR  FUNCIONÁRIO ===')

    for f in funcionarios:
        print(f"{f['id']} - {f['nome']} ({f['cargo']})")

    escolha = input('\nDigite o número do funcionário que deseja editar: ')

    if not escolha.isdigit():
        print('Entrada inválida.')
        return
    
    escolha = int(escolha)

    for f in funcionarios:
        if f["id"] == escolha:
            print('\nO que deseja editar?\n')
            print('1 - Nome')
            print('2 - Cargo')
            print('3 - Salário')

            opcao = input('\nEscolha uma opção: ')

            if opcao == '1':
                novo_nome = input('Digite o novo nome: ')
                f["nome"] = novo_nome
            
            elif opcao == '2':

                print('\nEscolha o novo cargo:\n')
                print('1 - Aprendiz de TI')
                print('2 - Estagiário de TI')
                print('3 - Developer Junior')
                print('4 - Developer Pleno')
                print('5 - Developer Sênior')
                print('6 - Gestor de TI')
                print('7 - Diretor Geral')

                novo_cargo = input('\nDigite uma opção:\n ')

                cargos = obter_cargos()
                
                if novo_cargo not in cargos:
                    print('Opção inválida.')
                    return
                
                f["cargo"] = cargos[novo_cargo]["nome"]
                f["salario"] = cargos[novo_cargo]["salario"]
                
            elif opcao == '3':
                try:
                    novo_salario = float(input('Digite o novo salário: ').replace(',' , '.'))
                    
                    if novo_salario <= 0:
                        print("Salário inválido.")
                        return

                    f['salario'] = novo_salario

                except ValueError:
                    print('Salário inválido.')
                    return
            
        
            else:
                print('Opção inválida.')
                return
            
            salvar_funcionarios(funcionarios) 
            print(f'\nFuncionário {f["nome"]} atualizado com sucesso!\n')
            return
        
    print('\nFuncionário não encontrado.')
            

def buscar_funcionario():
    funcionarios = carregar_funcionarios()
    
    if not funcionarios:
        print('Nenhum funcionário para editar. ')
        return
    
    print('\n=== BUSCAR FUNCIONÁRIO ===\n')
    for f in funcionarios:
        print(f'{f["id"]} - {f["nome"]}')
    escolha = input('Digite o ID do funcionário: ')

    if not escolha.isdigit():
            print('Entrada inválida.')
            return
    for f in funcionarios:
        if f["id"] == int(escolha):
            print('\nFuncionário encontrado!')
            print(f'\nID:  {f["id"]}')
            print(f'Nome: {f["nome"]}')
            print(f'Cargo: {f["cargo"]}')
            print(f'Salário: {f["salario"]:.2f}')
            return
    print('\nFuncionário não encontrado.')

