'''
Escreva um programa que implemente o algoritmo "mergesort" para ordenar uma lista de números inteiros.
'''

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    
    meio = len(lst) // 2
    esquerda = lst[:meio]
    direita = lst[meio:]

    esquerda = mergesort(esquerda)
    direita = mergesort(direita)

    return merge(esquerda, direita)

def merge (esquerda, direita):
    result = []

    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            result.append(esquerda[i])
            i += 1
        else:
            result.append(direita[j])
            j += 1

    result += esquerda[i:]
    result += direita[j:]

    return result

lista = [3,7,9,1,2,4,9,0]
mer = mergesort(lista)
print(mer)