'''
Escreva um programa que encontre o maior número de um array de números inteiros sem usar loops e sem usar a função "max".
'''

def find_max(array):
    if len(array) == 1:
        return array[0]
    else:
        first = array[0]
        second = find_max(array[1:])
        return first if first > second else second
    
array = [4, 2, 8, 1, 9, 5, 3]
max_number = find_max(array)
print(f'O maior número d array é: {max_number}')