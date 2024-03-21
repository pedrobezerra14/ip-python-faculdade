nota1 = float(input('DIgite a primeira nota: '))
nota2 = float(input('DIgite a segunda nota: '))
nota3 = float(input('DIgite a terceira nota: '))

media = ( nota1 + nota2 + nota3 ) / 3

if media >= 7 and media <=10:
    print(f'Você foi aprovado! Sua média foi {media:.2f}')
elif media >= 4 and media < 7:
    print(f'Você está em recuperação! Sua média foi {media:.2f}')
elif media >= 0 and media < 4:
    print(f'Você foi reprovado! Sua média foi {media:.2f}')
else:
    print(f'Digite valores entre 0 a 10 para conseguir uma média válida!')