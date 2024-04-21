carros = ['gol', 'chevete', 'uno', 'kombi', 'fusca', 'monza', 'mitsubishi']
nova_lista = []

for carro in carros:
    if (len(carro) > 5):
        nova_lista.append(carro)
        
# print(f'A lista de carros com mais de 5 caracteres é: {nova_lista}') 
for carro in nova_lista:
    print(carro)
