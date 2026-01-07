"""
Exercício 4: Contar vogais em uma frase

1. Peça ao usuário que digite uma frase qualquer.
2. Conte quantas vogais (a, e, i, o, u) existem na frase.
3. Mostre o total de vogais encontradas.
"""
from functions import recebe_frase
import os
os.system('cls')

frase = recebe_frase()

vogais = "aeiouAEIOU"

contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

if contador > 0:
    print(f"O total de vogais na frase é: {contador}")
else:
    print("A frase não tem vogais.")