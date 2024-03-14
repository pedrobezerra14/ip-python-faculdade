# 3. Faça um programa que solicite o
# preço de uma mercadoria e o
# percentual de desconto. Exiba o valor
# do desconto e o preço a pagar.

preco_mercadoria = float(input('Informe o preço do produto que deseja aplicar o desconto: '))
percentual_desconto = float(input('Informe o percentual de desconto desejado: '))

desconto = preco_mercadoria * ( percentual_desconto / 100 )

print(f'O valor do desconto foi de {percentual_desconto}% e o preço a pagar será de R${desconto}')