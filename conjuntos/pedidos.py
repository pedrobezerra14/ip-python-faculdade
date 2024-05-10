pedido1 = {"Lancheira: R$ 132,67","Geladeira: R$ 1319,99","Air Fryer: R$ 552,67","Panela de Pressão: R$ 99,99"}
pedido2 = {"Teclado: R$ 169,99","Monitor: R$ 1299,99","Air Fryer: R$ 552,67","Lancheira: R$ 132,67"}

uniao = pedido1.union(pedido2)
intersecao = pedido1.intersection(pedido2)

print('===================================================')
print('Lista de todos os produtos: '.center(52))
print('===================================================')

for produto in uniao:
    print(produto.center(52))
    print('---------------------------------------------------')
    
print('===================================================')
print('Produtos que estão nas duas listas ao mesmo tempo: ')
print('===================================================')
    
for produto in intersecao:
    print(produto.center(52))
    print('---------------------------------------------------')

print('===================================================')