# 11. Escreva um programa que mostre na
# tela os dez primeiros termos de uma
# progressão aritmética (PA) com
# primeiro termo P e razão R. Os dois
# números P e R são inteiros e devem ser
# lidos do teclado.
# pa = sequencia de numeros com uma razão(diferença entre um elemento e o seu antecessor)

primeiro_termo = int(input('Informe o número que você deseja fazer a PA: '))
razao = int(input('Informe a razão da PA: '))
quantidade_termos = 1
termo_anterior = primeiro_termo

while quantidade_termos < 10:
    if quantidade_termos == 1:
        print(f'O 1º termo equivale a {primeiro_termo}')
    proximo_termo = termo_anterior + razao
    print(f'O {quantidade_termos + 1}º termo equivale a {proximo_termo}')
    quantidade_termos += 1
    termo_anterior = proximo_termo
