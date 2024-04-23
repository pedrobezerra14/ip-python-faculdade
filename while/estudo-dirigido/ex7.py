# Crie um programa de caixa eletrônico simples que permita ao usuário verificar o saldo, fazer
# depósitos e saques.

saldo = 0

while True:
    operacao = input('Informe a operação que deseja realizar: ')    
    if operacao == 'consulta':
        print(f'Você tem R${saldo}')
    elif operacao == 'deposito':
        valor_deposito = float(input('Informe o valor que deseja depositar: '))
        deposito = saldo + valor_deposito
        saldo += deposito
        print(f'Seu saldo atual é de R${deposito}')
    elif operacao == 'saque':
        valor_saque = float(input('Informe o valor que deseja sacar: '))
        saque = saldo - valor_saque
        saldo -= saque
        print(f'Seu saldo atual é de R${saque}')
    else:
        print('Fechando operação')
        break