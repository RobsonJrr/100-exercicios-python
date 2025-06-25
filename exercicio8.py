'''
Crie um programa que solicite ao usuário o preço de um produto e o percentual de desconto aplicado a ele. Calcule e exiba o preço final com o desconto aplicado.'''

preco = float(input('Digite o preço do produto: '))
percentual = float(input('Digite o percentual do produto: '))
desconto = preco * (percentual / 100)
total = preco - desconto

print(f'O valor total do produto com desconto é de {total:.2f}R$')