# 8. Escreva um programa que calcule o faturamento de um representante
# comercial que recebe R$ 500,00 fixos e 6% de comissão sobre as vendas
# do mês. Considere que ele fechou o mês com um valor de R$ 12.398,00
# em vendas. Exiba o resultado com duas casas decimais.

salario_com_comissao = 500 + ( 6 / 100 * 12398 )

print(f'O salário do RepresentanteCOmercial com comissão será de {salario_com_comissao:.2f}')
