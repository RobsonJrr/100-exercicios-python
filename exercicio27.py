'''
Escreva um programa em Python para somar dois inteiros positivos sem usar o operador '+'.
'''

def soma_sem_operador(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b 
        b = carry << 1
    return a

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

resultado = soma_sem_operador(a, b)
print(f'a soma de {a} e {b} é {resultado}')
