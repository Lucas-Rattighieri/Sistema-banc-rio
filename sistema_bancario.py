menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ''''''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu + '=> ')
    print('\n')

    if opcao == 'd':
        print(' Depósito '.center(50,'='))
        print('\n')

        deposito = float(input('Informe o valor a ser depositado: R$ '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Deposito: R$ {deposito:.2f}\n'

        else:
            print('O valor depositado deve ser maior que R$ 0.00')

        print('\n')
        print('=' * 50)
    
    elif opcao == 's':

        print(' Saque '.center(50,'='))
        print('\n')

        if numero_saques < 3:
            saque = float(input('Informe o valor a ser sacado: R$ '))

            if saque <= saldo:
                if saque <= 500.0:
                    saldo -= saque
                    extrato += f'Saque: R$ {saque: .2f}\n'
                    numero_saques += 1
                else:
                    print('O valor máximo a ser sacado é de R$ 500.00')

            else: 
                print('Não é possível sacar o dinheiro, saldo insuficiente.')
        
        else:
            print('O limite de saques diários já foi atingido.')
        
        print('\n')
        print('=' * 50)
    
    elif opcao == 'e':
        print(' Extrato '.center(50,'='))
        print('\n')

        if len(extrato) > 0:
            print(extrato)
            print(f'Saldo atual: R$ {saldo: .2f}')
        else:
            print('Não foram realizadas movimentações')

        print('\n')
        print('=' * 50)
    
    elif opcao == 'q':
        print('=' * 50)
        break

    else:
        print('Operação inválida, por favor, selecione novamente a operação desejada.')
        print('\n')