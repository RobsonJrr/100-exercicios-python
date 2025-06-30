'''
Escreva um programa em Python que subtraia dois números sem utilizar o operador aritmético "-".
'''

def substract(x, y):

    y = ~y + 1

    result = x + y

    return result