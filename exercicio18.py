'''
Crie um programa que leia uma lista de palavras do usuário e imprima apenas as palavras que começam com a letra "a", utilizando um loop for
'''
nomes = ['Ana','Paulo', 'Miguel', 'Abraão', 'Arnold', 'Pedro']
# nomes = int(input('quantos nomes você vai digitar? '))


for i in nomes:
    # name = str(input(f'digite o {i+1}º nome: '))
    if i.lower().startswith('a'):
        print(i)