'''
Crie um programa que solicite ao usuário a velocidade e o tempo que um objeto levou para se mover e calcule a distância percorrida. Exiba a distância calculada.
'''

velocidade = float(input('Digite uma velocidade em m/s: '))
tempo = float(input('Digite o tempo que foi percorrido em segundos: '))
distancia = velocidade * tempo

print(f'A distancia percorrida foi de {distancia} metros')