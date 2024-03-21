idade = int(input('Informe a sua idade para verificar sua obrigatoriedade de voto:'))

if idade < 16:
    print('Não pode votar ainda!')
elif idade >= 18 and idade < 70:
    print('Você se classifica como voto obrigatório!')
else:
    print('Voto Facultativo!')
    