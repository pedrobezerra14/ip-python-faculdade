curso = str(input('Insira o curso que deseja saber o tempo de conclusão: '))

if curso == 'ADS':
    print(f'O tempo de conclusão do curso {curso} corresponde a 2 anos')
elif curso == 'Medicina':
    print(f'O tempo de conclusão do curso {curso} corresponde a 6 anos')
elif curso == 'Engenharia':
    print(f'O tempo de conclusão do curso {curso} corresponde a 5 anos')
else:
    print(f'O tempo de conclusão do curso de {curso} corresponde a 4 anos')
