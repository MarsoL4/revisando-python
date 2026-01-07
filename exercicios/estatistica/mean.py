"""Exercício: Calcular Média

1. Crie uma função que recebe uma lista de números como argumento.
2. Calcule a média da lista (a soma de todos os números dividida pela quantidade de elementos).
3. Retorne ou imprima a média calculada.
4. Teste sua função usando pelo menos três listas diferentes de números.

Dica: não use bibliotecas externas (como numpy ou statistics) na primeira tentativa, para treinar a lógica do algoritmo."""

def calcula_media(lista: list):
    while True:
        if lista != []:
            media = sum(list(map(int, lista))) / len(lista)
            if media == int(media):
                return int(media)
            else:
                return media
        else:
            return 0

print(f"Média da Lista [1, 2 , 3] = {calcula_media([1, 2, 3])}")    # -> 2
print(f"Média da Lista [1, 2 , 4] = {calcula_media([1, 2, 4])}")    # -> 2,33333...
print(f"Média da Lista [] = {calcula_media([])}")           # -> 0