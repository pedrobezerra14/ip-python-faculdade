# Crie um jogo em que o computador escolhe um número aleatório entre 1 e 100, e o jogador
# tem que adivinhar o número. Permita que o jogador continue adivinhando até acertar o
# número.

import random

num = int(input('Informe um número inteiro aleatório entre 1 e 100: '))
numero_aleatorio = random.randint(1, 100)
contador = 1
print(numero_aleatorio)

while num != numero_aleatorio:
    if num < 1 or num > 100:
        print('O número informado está dentro do intervalo de 1 e 100.')
        num = int(input('Informe um número inteiro aleatório entre 1 e 100: '))
    else:
        print('Você errou, tente novamente!')
        num = int(input('Informe um número inteiro aleatório entre 1 e 100: '))
contador += 1

print(f'Você acertou! O número sorteado foi {numero_aleatorio}')
print(f'Você tentou {contador} vezes')