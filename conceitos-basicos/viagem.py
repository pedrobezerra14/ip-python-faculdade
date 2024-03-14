# 4. Escreva um programa que calcule o
# tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a
# velocidade média esperada para a
# viagem.

distancia = float(input('Informe a distância que irá percorrer(km): '))
velocidade_media = float(input('Informe a velocidade média para a viagem(km/h): '))

tempo = distancia / velocidade_media

print(f'O tempo de sua viagem será de {tempo}hrs')