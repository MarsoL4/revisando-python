"""
Exercício 5: Lista de quadrados de números

1. Peça ao usuário um número inteiro positivo N.
2. Crie uma lista contendo o quadrado de cada número de 1 até N (exemplo: se N=4, a lista será [1, 4, 9, 16]).
3. Imprima a lista final.
"""
from functions import recebe_numero
import os
os.system('cls')

def atualiza_lista(lista_quadrados: list, base_potencia: int):
    lista_quadrados.append(base_potencia ** 2)

lista = []
for i in range(1, recebe_numero() + 1, 1):
    atualiza_lista(lista, i)

print(f"\nA lista dos quadrados dos números até o número selecionado ficou assim: \n{lista}")