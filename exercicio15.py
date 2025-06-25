'''
Escreva um programa que leia uma lista de números inteiros do usuário e imprima a soma desses números, utilizando um loop while.
'''

soma = 0
# i = 0
numero = int(input('Digite um número (0 para parar): '))
# numeros = [2, 4, 7, 9, 3, 5]

while numero != 0:
# while i < len(numeros):
    soma += numero
    numero = int(input('Digite um número (0 para parar): '))
    # soma += numeros[i]
    # i += 1
print(f'A soma dos números é: {soma}')


