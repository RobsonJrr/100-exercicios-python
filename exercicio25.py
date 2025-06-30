'''
Crie um programa Python que implemente o algoritmo de ordenação "quicksort" e teste-o com uma grande lista de números aleatórios.
'''
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)
    
arr = [random.randint(1, 10000) for _ in range(10000)]
arr_sorted = quicksort(arr)
print(arr_sorted)
