numeros = []

while True:
    numero = int(input("Insira um número até digitar um número pela segunda vez e sair: "))
    
    if numero in numeros:
        print(f"O número repetido foi {numero}!")
        break
    
    numeros.append(numero)
