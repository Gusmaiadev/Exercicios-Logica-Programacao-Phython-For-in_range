"""Escreva um programa para calcular o fatorial de um número n digitado pelo usuário. Por exemplo: n = 5     fatorial = 5 x 4 x 3 x 2 x 1 = 120. OBS: utilize o “for”."""

num = int(input("Digite um número: "))
fat = 1

for i in range(num):
   i += 1
   print(i)
   fat = fat * i


print(f"O fatorial de {num} é {fat}")