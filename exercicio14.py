'''
Escreva um programa que leia um número inteiro do usuário e imprima todos os números primos entre 1 e o número lido, utilizando um loop for.
'''

num = int(input('Digite um número inteiro: '))

for i in range(2, num + 1):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)