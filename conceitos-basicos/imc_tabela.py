peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / altura **2

imc_limitado = round(imc, 2)

print('Seu IMC é:',imc_limitado)

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
