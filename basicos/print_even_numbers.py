"""
Exercício 1: Imprima números pares

1. Escreva um programa em Python que receba um número inteiro N do usuário.
2. Imprima na tela todos os números pares de 0 até N, inclusive, um por linha.
"""

import os
os.system('cls')

while True:
    try:
        number = int(input("Digite o número: "))
        break  # Encerra quando o valor for válido
    except ValueError:
        print("Você precisa digitar um número inteiro válido. Tente novamente!")

for i in range (0, number + 1, 2):
    print(i)