"""Exercício 2: Ordenação de Lista com Insertion Sort

1. Crie uma função em Python chamada insertion_sort (ou outro nome que desejar).
2. Essa função deve receber uma lista de números inteiros como argumento.
3. Implemente o algoritmo de ordenação "insertion sort" manualmente (não use sorted ou sort).
   - O algoritmo percorre a lista e insere cada elemento no lugar correto, um de cada vez, até a lista estar ordenada.
4. Retorne a lista ordenada (pode ser uma nova lista ou modificar a existente).
5. Teste sua função com pelo menos duas listas de números diferentes, incluindo uma já ordenada e uma em ordem reversa.

Dica: pense em como “empurrar” os elementos à direita para liberar espaço para o número que está sendo inserido na posição correta."""

import os
os.system('cls')

def insertion_sort(lista: list[int]) -> list:
    # Passa por cada elemento da lista a partir do segundo
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Move os elementos da lista[0...i-1] que são maiores que a 'chave'
        # uma posição à frente para criar espaço para a 'chave'
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

print(insertion_sort([2, 1]))         # [1, 2]
print(insertion_sort([3, 2, 1]))      # [1, 2, 3]
print(insertion_sort([5, 3, 4, 1, 2]))# [1, 2, 3, 4, 5]
