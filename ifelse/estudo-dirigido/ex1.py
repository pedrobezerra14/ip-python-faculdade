situacao = input('Informe sua situação para verificarmos: ')

grupos_prioritarios = ["gravida", "pcd", "lactante", "idoso"]

if situacao.lower() in grupos_prioritarios:
    print(f'Você faz parte do grupo prioritário, passe na frente da fila!')
else:
    print(f'Você não faz parte do grupo prioritário, espere na fila!')
