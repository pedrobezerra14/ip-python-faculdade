senha = input('Informe uma senha de pelo menos 8 caracteres: ')
tamanho_senha = len(senha)

while tamanho_senha < 8:
    print('Digite uma senha com pelo menos 8 caracteres!!!')
    break
while tamanho_senha >= 8:
    print('Senha inserida com sucesso!')
    break
