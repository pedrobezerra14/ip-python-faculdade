# Construa um programa que valide o acesso de um usuário ao sistema. Caso o par
# usuário/senha informado esteja correto, o programa deve imprimir a mensagem “Seja bem
# vindo!”. Caso contrário, “Usuário e senha não conferem”.

usuario = 'pedro'
senha = '123'

input_usuario = input('Informe o seu usuário: ')
input_senha = input('Informe a sua senha: ')

if usuario == input_usuario and senha == input_senha:
    print('Seja bem vindo!')
else:
    print('Usuário e senha não conferem')
