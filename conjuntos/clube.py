membros = {'Tal do Mané', 'Henderson', 'Folkis Faguen', 'Hurivelton', 'Chica', 'Minsira'}

membros.add('Peuson')
membros.remove('Tal do Mané')

print('Membros do clube: ')
for membro in membros:
    print(membro)
    
consulta = input('Pesquise aqui para saber se é membro do clube: ')

if consulta in membros:
    print(f'{consulta} faz parte do clube!')
else:
    print(f'{consulta} NÃO faz parte do clube!')