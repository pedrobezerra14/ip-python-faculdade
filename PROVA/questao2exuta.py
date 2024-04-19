salario_colaborador = float(input('Informe o seu salário para ser calculado o reajuste: '))

if salario_colaborador < 1200:
    acrescimo = 0.2
    novo_salario = salario_colaborador + (0.2 * salario_colaborador)
    faixa_salarial = 'até R$ 1200,00'
elif 1200 <= salario_colaborador <= 2000:
    acrescimo = 0.15
    novo_salario = salario_colaborador + (0.15 * salario_colaborador)
    faixa_salarial = 'entre R$ 1200,00 e R$ 2000,00'
else:
    acrescimo = 0.1
    novo_salario = salario_colaborador + (0.1 * salario_colaborador)
    faixa_salarial = 'maior que R$ 2000,00'

print(f'Seu salário é de {faixa_salarial}, então terá um acréscimo de {acrescimo * 100}%')
print(f'{acrescimo * salario_colaborador}% do seu salário irá equivaler a um acréscimo de R${acrescimo * salario_colaborador}')
print(f'Seu salário era de R$ {salario_colaborador}, com o acréscimo ficará R${novo_salario}')
