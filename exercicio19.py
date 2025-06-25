'''
Escreva um programa que leia uma string do usuário e conte quantas vogais existem nessa string, utilizando um loop for.
'''

vogais = 'aeiou'
qtd_vogais = 0
string  = str(input('Digite uma palavra: ')).lower()

for i in string:
    if i in vogais:
        qtd_vogais += 1
    
print(f'A sua palavra tem {qtd_vogais} vogais!')