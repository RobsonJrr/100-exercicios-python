'''
um programa que leia um número inteiro do usuário e imprima a tabuada desse número, utilizando um loop for.
'''

num = int(input('Digite um número inteiro: '))

for i in range(1, 11):
    print(num, "X", i, "=", num * i)