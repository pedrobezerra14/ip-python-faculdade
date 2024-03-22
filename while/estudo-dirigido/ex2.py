contagem_regressiva = 10

while contagem_regressiva <= 10:
    print(f'{contagem_regressiva}')
    contagem_regressiva -= 1
    if contagem_regressiva == -1:
        print('Fogo!')
        break
