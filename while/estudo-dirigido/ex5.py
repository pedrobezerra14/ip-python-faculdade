# Crie um jogo em que o computador escolhe um número aleatório entre 1 e 100, e o jogador
# tem que adivinhar o número. Permita que o jogador continue adivinhando até acertar o
# número.

import random

num = int(input('Informe um número inteiro aleatório entre 1 e 100:'))

numero_aleatorio = random.randint(1, 100)

while num != numero_aleatorio:
    num = int(input('Informe um número inteiro aleatório entre 1 e 100:'))
    if num == numero_aleatorio:
        print('Você acertou!')
