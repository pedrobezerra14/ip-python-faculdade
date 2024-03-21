# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e
# R$ 0,45 para viagens mais longas.

distancia = float(input('Informe a distância que você deseja percorrer em km: '))

if distancia <= 200:
    preco_passagem = distancia * 0.50
else:
    preco_passagem = distancia * 0.45

print(f'O preço da passagem será de R${preco_passagem}')
