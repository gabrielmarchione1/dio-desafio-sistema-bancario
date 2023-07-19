menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        print('Despósito:\n')
        
        while True:
            valor_deposito = input('Digite o valor do depósito: ')
            if valor_deposito:
                valor_deposito = float(valor_deposito)
                saldo += valor_deposito
                extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
                print('Depósito feito com sucesso!')
                break
            else:
                print('Operação Inválida.', end=' ')
    
    elif opcao == 2:
        print('Sacar:\n')
        
        while True:
            valor_saque = input('Digite o valor de saque: ')
            if valor_saque:
                valor_saque = float(valor_saque)
                if valor_saque <= saldo:
                    if numero_saques < 3:
                        if valor_saque <= limite:
                            saldo -= valor_saque
                            extrato += f'Saque: R$ {valor_saque:.2f}\n'
                            numero_saques += 1
                            print(f'Saque feito com Sucesso!')
                            break
                        else:
                            print('Operação Inválida, o valor de saque excede o limite.', end=' ')
                            break
                    else:
                        print('Operação Inválida, número de saques excedido.', end=' ')
                        break
                else:
                    print('Operação Inválida, você não tem saldo suficiente.', end=' ')       
                    break
            else:
                print('Operação Inválida.', end=' ')
            

    elif opcao == 3:
        print('=============Extrato=============')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('=================================')

    
    elif opcao == 4:
        break
              
    else:
        print('Opção inválida. Digite novamente.')

