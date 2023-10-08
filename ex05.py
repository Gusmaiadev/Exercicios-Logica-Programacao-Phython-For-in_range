"""Desenvolva um programa que receba:
taxa de abatimento em porcentagem;
número de prestações;
valor da primeira prestação.
Seu programa deverá exibir na tela os valores das prestações decrescente dado que a cada mês o valor da prestação diminui
do valor da prestação do mês anterior (utilize a taxa de abatimento fornecida pelo usuário para realizar esse cálculo).
OBS: utilize o “for”. """

taxa = float(input("Digite a taxa de abatimento: "))
qtd = int(input("Digite a quantidade de pretsções: "))
primeira = float(input("Digite o valor da perimeira prestação: "))

cont = 0

for i in range(qtd):

    cont += 1

    if(i == 0):
        print(f"{cont} parcela : {primeira}")
        valor_parcela = primeira

    else:
         valor_parcela = valor_parcela - (valor_parcela * (taxa / 100))
         print(f"{cont} parcela : {valor_parcela:.2f} ")