'''
Crie um programa Python que encontre o menor número primo após um número digitado pelo usuário. Se o usuário digitar um número que já é um número primo, o programa deve encontrar o próximo número primo maior do que o número digitado.
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def proximo_primo(numero):
    numero += 1
    while not is_prime(numero):
        numero +=1
    return numero

entrada = int(input("digite um número: "))
resultado = proximo_primo(entrada)
print(f"O menor número primo após {entrada} é {resultado}")