# O Jogo da Forca é um jogo clássico em que um jogador tenta
# adivinhar uma palavra oculta, letra por letra, antes que seu boneco
# seja desenhado na forca. O programa deve gerar uma palavra
# aleatória a ser adivinhada pelo jogador e permitir que o jogador insira
# letras para tentar adivinhar a palavra.

import random

palavras_para_adivinhar = ['linux', 'macos', 'windows', 'programacao', 'python', 'desenvolvedor']
palavra_selecionada = random.choice(palavras_para_adivinhar)

letras_adivinhadas = []
tentativas_totais = 6

resultado = ''
for letra in palavra_selecionada:
    resultado += '_ '