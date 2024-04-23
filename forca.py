# O programa deve:
# 1- gerar uma palavra aleatória a ser adivinhada pelo jogador
# 2- permitir que o jogador insira letras para tentar adivinhar a palavra.

import random

palavras_para_adivinhar = ['linux', 'macos', 'windows', 'programacao', 'python', 'desenvolvedor']
palavra_selecionada = random.choice(palavras_para_adivinhar)

letras_adivinhadas = []
tentativas_totais = 6

boneco_forca = [
    "  ____\n |    |\n      |\n      |\n      |\n      |\n______|",
    "  ____\n |    |\n O    |\n      |\n      |\n      |\n______|",
    "  ____\n |    |\n O    |\n |    |\n      |\n      |\n______|",
    "  ____\n |    |\n O    |\n/|    |\n      |\n      |\n______|",
    "  ____\n |    |\n O    |\n/|\   |\n      |\n      |\n______|",
    "  ____\n |    |\n O    |\n/|\   |\n/     |\n      |\n______|",
    "  ____\n |    |\n O    |\n/|\   |\n/ \   |\n      |\n______|"
]

# Inicializa a string resultado com underscores para cada letra da palavra selecionada
resultado = '_' * len(palavra_selecionada)

print('VOCÊ TEM 6 TENTATIVAS PARA DESCOBRIR A PALAVRA!')

while True:
    print(resultado)
    
    letra = input("Digite uma letra para saber se ela está na palavra: ").lower()
    if len(letra) != 1:
        print("Por favor, digite apenas um caractere por vez.")
        continue

    if letra in letras_adivinhadas:
        print("Você já tentou essa letra!")
        continue

    letras_adivinhadas.append(letra)

    if letra not in palavra_selecionada:
        tentativas_totais -= 1
        print(f"ERROU! Agora você tem {tentativas_totais} tentativas restantes.")
        print(boneco_forca[6 - tentativas_totais])

        if tentativas_totais == 0:
            print(f"Infelizmente você perdeu! A palavra era: {palavra_selecionada}")
            break
    else:
        resultado = ''
        for letra_palavra in palavra_selecionada:
            if letra_palavra in letras_adivinhadas:
                resultado += letra_palavra
            else:
                resultado += '_'
                
        if '_' not in resultado:
            print(f"Parabéns! Você adivinhou a palavra: {palavra_selecionada}!")
            break
