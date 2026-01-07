"""
Exercício 1: Imprima números pares

1. Escreva um programa em Python que receba um número inteiro N do usuário.
2. Imprima na tela todos os números pares de 0 até N, inclusive, um por linha.
"""
from exercicios.functions import recebe_numero
import os
os.system('cls')

for i in range (0, recebe_numero() + 1, 2):
    print(i)