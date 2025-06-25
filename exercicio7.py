'''
Crie um programa que solicite ao usuário o raio de um círculo e calcule sua área. Exiba a área calculada.
'''
from math import pi

raio = float(input('Digite o raio do círculo: '))
area = pi * raio ** 2

print(f'A área do círculo é de {area:.2f} cm')