"""Exercício: Calcular Mediana

1. Crie uma função que recebe uma lista de números como argumento.
2. Calcule a mediana da lista (o número que fica no meio quando a lista está ordenada; se a lista tiver quantidade par de elementos, calcule a média dos dois do meio).
3. Retorne ou imprima a mediana calculada.
4. Teste sua função usando listas com quantidade par e ímpar de elementos.

Dica: não use bibliotecas externas (como numpy ou statistics) na primeira tentativa, para treinar a lógica do algoritmo."""

def calc_median(listed_numbers: list[int]) -> int:
    listed_numbers.sort() # Ordena a Lista
    num_items = len(listed_numbers) # Armazena a quantidade de items da lista numa variável
    if num_items % 2 == 0: # Verifica se a quantidade de itens na lista é par
        print(f"\nA Quantidade de números na lista {listed_numbers} é: {num_items} -> Par")
        
        mid_index = int((num_items / 2) - 1)
        mid_number = listed_numbers[mid_index]
        print(f"E sua Mediana é: ({mid_number} + {listed_numbers[mid_index + 1]}) / 2 = {(mid_number + listed_numbers[mid_index + 1]) / 2}")
    else:
        print(f"\nA Quantidade de números na lista {listed_numbers} é: {num_items} -> Ímpar")
        
        mid_index = int((num_items / 2))
        print(f"E sua Mediana é: {listed_numbers[mid_index]}")
    
calc_median([1, 2, 4, 3])
calc_median([3, 2, 1, 5, 4])
calc_median([8, 2, 7, 4, 4])