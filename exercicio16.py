'''
Escreva um programa que leia uma lista de números inteiros do usuário e imprima a média desses números, utilizando um loop for.
'''

# numeros = int(input('quantos números você vai digitar? '))
numeros = [10, 20, 30, 40, 50]
soma = 0

# for i in range(numeros):
for num in numeros:
    # num = int(input(f'digite o {i+1}º número: '))
    soma += num

# total = soma / numeros
media = soma / len(numeros)
# print(f'{total}')
print(f'A média dos números é: {media}')






