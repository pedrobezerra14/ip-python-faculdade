# 4. Elabore um programa que realize a conversão do valor em dólares para
# real. (Considere a cotação: 1 dólar americano = 4,96 reais)

dolar = float(input('Digite o valor em dólar que deseja transformar em real: '))

conversor = dolar * 4.96

print(f'O valor de {dolar}$ convertido será de R${conversor}')