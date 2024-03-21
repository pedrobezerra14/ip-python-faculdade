# Escreva um programa que leia dois números e que pergunte qual operação você deseja
# realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
# Exiba o resultado da operação solicitada.
operacoes = ['soma', 'subtração', 'multiplicação', 'divisão']

num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))
operacao_desejada = input('Informe a operação desejada: ')


if operacao_desejada == 'soma':
    conta = num1 + num2
elif operacao_desejada == 'subtração':
    conta = num1 - num2
elif operacao_desejada == 'multiplicação':
    conta = num1 * num2
elif operacao_desejada == 'divisão':
    conta = num1 / num2
else: 
    print('Essa não é uma operação disponível nessa calculadora')
print(f'O resultado da sua conta é : {conta}')
