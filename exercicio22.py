'''
Crie um programa que calcule a soma dos dígitos de um número inteiro positivo. Se o resultado tiver mais de um dígito, o processo deve ser repetido até que o resultado tenha apenas um dígito.
'''

def soma_digitos(numero):
    while numero >= 10:
        soma = 0 
        while numero > 0:
            soma += numero % 10
            numero //= 10
        numero = soma
    return numero 
    
entrada = int(input("digite um número inteiro positivo: "))
resultado = soma_digitos(entrada)
print(f"A soma dos digitos de {entrada} é {resultado}")

    