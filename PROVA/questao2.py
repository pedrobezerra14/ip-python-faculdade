salario_colaborador = float(input('Informe o seu salário para ser calculado o reajuste: '))

if salario_colaborador < 1200:
    print('Seu salário é de até R$ 1200,00 então terá um acréscimo de 20%.')
    print(f'20% do seu salário irá equivaler a um acréscimo de R${ 20 / 100 * salario_colaborador}')
    print(f'Seu salário era de R$ {salario_colaborador}, com o acréscimo ficará R${salario_colaborador + ( 20 / 100 * salario_colaborador)}')

elif salario_colaborador >= 1200 and salario_colaborador <= 2000:
    print('Seu salário está entre R$ 1200,00 e R$ 2000,00 então terá um acréscimo de 15%.')
    print(f'15% do seu salário irá equivaler a um acréscimo de R${ 15 / 100 * salario_colaborador}')
    print(f'Seu salário era de R$ {salario_colaborador}, com o acréscimo ficará R${salario_colaborador + ( 15 / 100 * salario_colaborador)}')

else:
    print('Seu salário é maior que R$ 2000,00 então terá um acréscimo de 10%.')
    print(f'10% do seu salário irá equivaler a um acréscimo de R${ 10 / 100 * salario_colaborador}')
    print(f'Seu salário era de R$ {salario_colaborador}, com o acréscimo ficará R${salario_colaborador + ( 10 / 100 * salario_colaborador)}')
