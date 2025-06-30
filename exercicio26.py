'''
Escreva um programa que receba como entrada um arquivo de texto e imprima todas as palavras do arquivo que aparecem mais de uma vez.
'''

from collections import Counter

with open('arquivo.txt', 'r') as f:
    texto = f.read()

palavras = texto.split()
contador = Counter(palavras)

for palavra, frequencia in contador.items():
    if frequencia > 1:
        print(palavra)