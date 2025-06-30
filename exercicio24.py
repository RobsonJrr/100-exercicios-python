'''
Crie um programa que encontre o comprimento da maior sequência contígua de caracteres iguais em uma string dada pelo usuário.
'''
string = input('Digite uma palavra: ')
cont_atual = 1
maior = 1

for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        cont_atual += 1
    else:
        if cont_atual > maior:
            maior = cont_atual
        cont_atual = 1

    if cont_atual > maior:
        maior = cont_atual

print('Maior sequência contígua de caracteres iguais tem comprimento:', maior)
