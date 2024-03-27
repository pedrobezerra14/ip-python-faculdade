senha = input('Informe uma senha de pelo menos 8 caracteres: ')

while len(senha) < 8:
    senha = input('Informe uma senha de pelo menos 8 caracteres: ')
    break

print('Senha cadastrada com sucesso!')  
