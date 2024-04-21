numeros = []

while True:
    numero = int(input('Digite um número inteiro: '))
    if numero != 0:
        numeros.append(numero)
    else:
        break
    
print(f'A lista de números é {numeros}')
print(f'E o seu tamanho é {len(numeros)}')
