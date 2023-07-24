def menu():
    menu = '''
    ---------- MENU ----------
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair

    '''
    return int(input(menu))


def depositar(saldo, valor, extrato, /):
    if valor:
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('<--- Depósito feito com sucesso! --->')
        else:
            print('Operação Inválida, Tente novamente.')
    else:
        print('Operação Inválida, Tente novamente.')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor:
        if valor <= saldo:
            if len(numero_saques) < limite_saques:
                if valor <= limite:
                    saldo -= valor
                    extrato += f'Saque: R$ {valor:.2f}\n'
                    numero_saques.append(1)
                    print('<--- Saque feito com Sucesso! --->')
                else:
                    print('Operação Inválida, o valor de saque excede o limite.')
            else:
                 print('Operação Inválida, número de saques excedido.')
        else:
            print('Operação Inválida, você não tem saldo suficiente.')       
    else:
        print('Operação Inválida, Tente novamente.')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('---------- EXTRATO ----------')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('-----------------------------')


def criar_usuario(usuarios):
    print('Criando usuário:\n')
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário com este CPF!')
        return
     
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe sua data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço (logradouro, numero - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('<--- Usuário criado com sucesso! --->')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n<--- Conta criada com sucesso! --->")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print('\nUsuário não encontrado, fluxo de criação de conta encerrado!')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("-" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = []
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()

        if opcao == 1:
            print('\nDespósito:\n')
            valor_deposito = float(input('Digite o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)
                
        elif opcao == 2:
            print('\nSacar:\n')
            valor_saque = float(input('Digite o valor de saque: '))
            
            saldo, extrato = sacar(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == 3:
            
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            criar_usuario(usuarios)

        elif opcao == 7:
            break
                
        else:
            print('Opção inválida. Digite novamente.')


main()