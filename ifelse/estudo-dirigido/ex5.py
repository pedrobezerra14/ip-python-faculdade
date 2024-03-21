# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse
# 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor
# da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = float(input('Informe a velocidade do carro(km/h): '))

if velocidade > 80:
    print('Você foi multado! Sua velocidade está acima de 80km/h')
    valor_multa = velocidade * 5
    print(f'E o valor da multa foi de R${valor_multa:.2f}')
