palavra = input('Digite uma palavra para que a letra a seja substituída por x: ')
nova_palavra = ''

for letra in palavra:
    if letra == "a" or letra == 'A':
       nova_palavra += "x" # nova_palavra = nova_palavra + letra
    else:
        nova_palavra += letra
        
print(f'A {palavra} que foi informada ficará correspondente a {nova_palavra}')
