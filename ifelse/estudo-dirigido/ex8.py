# 8. Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
qtd_anos = float(input('Informe a quantidade de anos: '))


total_mensal = valor_casa / (qtd_anos * 12)
limite_prestacao = salario * 0.3
prestacao_mensal = abs(total_mensal - (30 / 100 * salario))

if prestacao_mensal <= limite_prestacao:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação mensal: R${prestacao_mensal:.3f}")
else:
    print("Empréstimo negado. Prestação excede 30% do salário.")
