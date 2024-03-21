# 9. Escreva um programa que leia a quantidade de dias, horas, minutos e
# segundos do usuário. Calcule o total em segundos.

dias = int(input('Insira a quantidade de dias desejados: '))
horas = int(input('Insira a quantidade de horas desejadas: '))
minutos = int(input('Insira a quantidade de minutos desejados: '))
segundos = int(input('Insira a quantidade de segundos desejados: '))

converter = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print(f'Seu resultado será de {converter} segundos')
