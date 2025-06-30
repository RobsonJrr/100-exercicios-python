'''
Escreva um programa que encontre o número de ocorrências de uma determinada substring em uma string dada pelo usuário.
'''

def contar_substring(string, substring):
    contador = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            contador += 1
    return contador

string = input('Digite uma string: ')
substring = input('Digite a substring a ser contada: ')
resultado = contar_substring(string, substring)
print(f"A substring '{substring}' ocorre {resultado} vezes na string '{string}'")