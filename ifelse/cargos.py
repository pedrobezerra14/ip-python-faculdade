salario = float(input('Informe o seu salário: '))
cargo = str(input('Informe o seu cargo: '))

if cargo == "programador":
     novo_salario = salario + ( 30 / 100 * salario)
     print(f'Com o aumento, seu salário será de R${novo_salario}')
elif cargo == "analista":
     novo_salario = salario + ( 20 / 100 * salario)
     print(f'Com o aumento, seu salário será de R${novo_salario}')
elif cargo == "analista banco de dados":
     novo_salario = salario + ( 15 / 100 * salario)
     print(f'Com o aumento, seu salário será de R${novo_salario}')
else:
     print("CARGO INVÁLIDO!")
