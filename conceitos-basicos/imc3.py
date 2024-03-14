peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / altura **2

imc_limitado = round(imc, 2)

print("---------------------------------")
print(f"Seu IMC é {imc_limitado}")
print("---------------------------------")

if imc_limitado < 18.5:
    print(f"Por seu IMC estar abaixo de 18.5, você se enquadra em MAGREZA")
elif imc_limitado >= 18.5 and imc_limitado <= 24.9:
    print(f"Por seu IMC estar entre de 18.5 e 24.9, você se enquadra em NORMAL")
elif imc_limitado >= 25.0 and imc_limitado <= 29.9:
    print(f"Por seu IMC estar entre de 25.0 e 29.9, você se enquadra em SOBREPESO")
elif imc_limitado >= 30.0 and imc_limitado <= 39.9:
    print(f"Por seu IMC estar entre de 18.5 e 24.9, você se enquadra em OBESIDADE")
elif imc_limitado >= 40.0:
    print(f"Por seu IMC ser maior que 40, você se enquadra em OBESIDADE GRAVE")

print("---------------------------------")
print("INFORMAÇÕES DE ACORDO COM A TABELA ABAIXO")
print("---------------------------------")

def tabelaImc():
    print("IMC   \t\tClassificação")
    print("---------------------------------")
    print("MENOR QUE 18,5\t\tMAGREZA")
    print("---------------------------------")
    print("ENTRE 18,5 E 24,9\tNORMAL")
    print("---------------------------------")
    print("ENTRE 25,0 E 29,9\tSOBREPESO")
    print("---------------------------------")
    print("ENTRE 30,0 E 39,9\tOBESIDADE")
    print("---------------------------------")
    print("MAIOR QUE 40,0\tOBESIDADE GRAVE")
    print("---------------------------------")
tabelaImc()
print('Informações retiradas de Programa Saúde Fácil')
print('---------------------------------')
