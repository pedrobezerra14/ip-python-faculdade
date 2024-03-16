# 6. Elabore um programa que solicite o ano em que você nasceu. Crie uma
# mensagem que inclua o ano e informe quantos anos você tem
# atualmente.

ano_nascimento = int(input('Informe o ano que você nasceu: '))
ano_atual = int(input('Informe o ano atual: '))

idade = ano_atual - ano_nascimento
idade_sem_aniversario = idade - 1

print(f'Você nasceu no ano de {ano_nascimento} e se você já fez aniversário terá {idade} anos')
print(f'Porém, se você não fez aniversário terá {idade_sem_aniversario} anos')