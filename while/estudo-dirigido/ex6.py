# Escreva um algoritmo que solicite ao usuário o primeiro termo, a razão e o número de
# termos de uma progressão aritmética. Imprima os termos da progressão.

primeiro_termo = float(input('Informe o primeiro termo da PA: '))
razao = float(input('Informe a razão da PA: '))
num_termos = float(input('Informe o número de termos da PA: '))
termo_atual = primeiro_termo
contador = 0

print("Os termos da progressão aritmética são:")

while contador < num_termos:
    print(termo_atual)
    termo_atual += razao
    contador += 1
    