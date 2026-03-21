from armazenamento import carregar_funcionarios
def gerar_holerite():
    funcionarios = carregar_funcionarios()

    if not funcionarios:
        print('Nenhum funcionário cadastrado.')
        return

    for f in funcionarios:

        print(f'{f["id"]} - {f["nome"]}')

    escolha = input('\nDigite o ID do funcionário: ')
        
    if not escolha.isdigit():
        print('Entrada inválida.')
        return
    
    escolha =int(escolha)

    for f in funcionarios:

        if f["id"] == escolha:


            print('='*30)
            print('\n     HOLERITE\n')
            print('='*30)

            print(f'Nome: {f["nome"]}')
            print(f'Cargo: {f["cargo"]}')

            salario = f["salario"]
            inss = salario * 0.08
            vt = salario * 0.06
            vr = 500
            salario_liquido = salario - inss - vt
            total_recebido = salario_liquido + vr
            

            print(f'\nSalário bruto: R${salario:.2f}')

            print('\nDescontos:\n')
            print(f'INSS: {inss:.2f}')
            print(f'VT: R${vt:.2f}')

            print('\nBenefícios: \n')
            print(f'VR: R${vr:.2f}')


            print(f'\nSalário líquido: R${salario_liquido:.2f}')
            print(f'Total com benefícios: R${total_recebido:.2f}')
            return
    print('Funcionário não encontrado.')