num = int(input('Informe números inteiros: '))
soma = 0

while num > 0:
    num = int(input('Informe números inteiros: '))
    if num % 2 == 0:
        soma += int(num)
while num < 0:
    print(f'A soma dos números informados é: {soma}')
    break
