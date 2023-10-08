"""Escreva um programa que calcule o somatório de todos os números pares em um intervalo definido pelo usuário.
Ex: para inicio = 2 e fim = 10 o somatório é 2+4+6+8+10. OBS: utilize o “for”."""

soma = 0

inicio = int(input("Digite um número: "))
fim = int(input("Digite outro número (que seja maior que o primeiro): "))


for i in range(inicio, fim + 1):
    print(i)
    if (i % 2 == 0):
        soma += i

print(f"O resultado da soma é {soma}")