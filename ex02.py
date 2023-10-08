"""Escreva um algoritmo que solicite dois números e devolva quantos pares e ímpares há entre esses dois números. Exemplo: entre 7 e 10 há 2 números pares e 2 números ímpares"""
par = 0
impar = 0

inicio = int(input("Digite um número: "))

fim = int(input("Digite outro número: "))



for i in range(inicio, fim + 1):
    if (i %2 == 0):
        par += 1
    else:
        impar += 1

print(f"Existem {par} pares entre {inicio} e {fim}")
print(f"Existem {impar} ímpares entre {inicio} e {fim}")


