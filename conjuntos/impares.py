numeros_impares = set()

lista1 = [12, 13, 15, 14, -8, 99, 0, -4, 7]
lista2 = [7, 4, 6, 8, 123, 44, 567, -8, 15]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

intersecao = conjunto1.intersection(conjunto2)

for impar in intersecao:
    if (impar / 2) != 0:
        numeros_impares.add(impar)

print('O conjunto dos números ímpares presente em ambas as listas é: ')
print(numeros_impares)
