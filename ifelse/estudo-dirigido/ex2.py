num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))
maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 >= num2:
    maior = num3

print(f'O maior número informado foi {maior}')
