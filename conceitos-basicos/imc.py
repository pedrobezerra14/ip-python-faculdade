peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / altura **2

imc_limitado = round(imc, 2)

print('Seu IMC é:',imc_limitado)