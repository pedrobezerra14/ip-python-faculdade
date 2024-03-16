# 5. Escreva um programa que converta uma temperatura digitada em oC em
# oF. A fórmula para essa conversão é:
# F = 9 x C / 5 + 32

temperatura_celsius = float(input('Informe a temperatura em °C que deseja converter para °F: '))

converter_fahrenheit = ( 9 * temperatura_celsius / 5 ) + 32 

print(f'A temperatura de {temperatura_celsius}°C convetida será de {converter_fahrenheit}°F')