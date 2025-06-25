'''
Escreva um programa que converta uma temperatura em graus Celsius para Fahrenheit. O usuário deve fornecer a temperatura em graus Celsius.
'''

temperatura = input('Voce vai digitar a temperatura em qual escala (C/F)? ')

if temperatura == 'C':
    C = float(input(f'Temperatura equivalente em Celsius: '))
    Celsius = (C * 9 / 5) + 32
    print(f'Temperatura equivalente em Fahrenheit: {Celsius:.2f}')
else:
    F = float(input('Digite a temperatura em Fahrenheit: '))
    Fahrenheit = (F - 32) * 5 / 9
    print(f'Temperatura equivalente em Celsius: {Fahrenheit:.2f}')

