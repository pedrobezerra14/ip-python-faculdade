valor_camisa = 12.50
num_camisas = int(input('Informe o número de camisas desejado: '))
conta = valor_camisa * num_camisas

if num_camisas <= 5:
    desconto = conta - (3 / 100 * conta) 
elif num_camisas > 5 and num_camisas <=10:
    desconto = conta - (5 / 100 * conta) 
elif num_camisas > 10:
    desconto = conta - (7 / 100 * conta)

print(f'O valor que você vai pagar é de R${desconto:.2f}')
