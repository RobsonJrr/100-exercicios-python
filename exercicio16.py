'''
Escreva um programa que leia uma lista de números inteiros do usuário e imprima a média desses números, utilizando um loop for.
'''

numeros = int(input('quantos números você vai digitar? '))
soma = 0

for i in range(numeros):
    num = int(input(f'digite o {i+1}º número: '))
    soma += num

total = soma / numeros
print(f'{total}')