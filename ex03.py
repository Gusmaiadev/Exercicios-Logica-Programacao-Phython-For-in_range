"""Desenvolva um programa para calcular a média salarial dos funcionários da empresa XXX, para isso seu programa deverá solicitar o nome e salário dos 5 funcionários que trabalham nessa empresa. Ao final seu programa deverá calcular a média dos salários e exibir na tela as seguintes informações:  (use 2 casas decimais na exibição dos números)
A média salarial dos funcionários da empresa XXX é _______
O nome e o salário do funcionário que recebe o menor salário
O nome e o salário do funcionário que recebe o maior salário
"""

media = 0
cont = 0

for i in range(5):
    cont += 1
    nome = input(f"Digite o nome do {cont}° funcionário: ")
    salario = float(input(f"Digite o sálario do {cont}° funcionário: "))

    media += salario

    if(i == 0):
        nome_maior = nome
        salario_maior = salario
        nome_menor = nome
        salario_menor = salario

    else:
        if(salario>salario_maior):
            salario_maior = salario
            nome_maior = nome


        if(salario<salario_menor):
            salario_menor = salario
            nome_menor = nome

media = media / 5


print(f"A média salarial dos funcionário é R${media:.2f}")
print(f"O maior salário pertence ao {nome_maior} com salaário de R${salario_maior:.2f}")
print(f"O menor salário pertence ao {nome_menor} com salaário de R${salario_menor:.2f}")





