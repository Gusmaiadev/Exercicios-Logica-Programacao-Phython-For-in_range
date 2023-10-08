"""Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO."""


n = int(input("Digite um valor: "))

for i in range(n):
    i += 1
    print(i)