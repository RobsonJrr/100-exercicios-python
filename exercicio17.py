'''
Escreva um programa que leia uma lista de números inteiros do usuário e imprima apenas os números pares da lista, utilizando um loop for.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numeros = int(input('quantos números você vai digitar? '))

for i in numeros:
# for i in range(numeros):
    # num = int(input(f'digite o {i+1}º número: '))
    if i % 2 == 0:
    # if num % 2 == 0:
        # print(f'{num} é par.')
        print(i)