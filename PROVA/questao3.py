salario_anual = float(input('Digite o seu salário anual: '))
valor_emprestimo = float(input('Digite o valor que deseja fazer o empréstimo: '))
emprestimo_limite = 100000

if salario_anual >= 30 * valor_emprestimo and valor_emprestimo <= emprestimo_limite:
    print(f"Seu empréstimo foi aprovado! O valor dele será de R${valor_emprestimo}!")
else:
    print("Você não é elegível para o empréstimo!")
