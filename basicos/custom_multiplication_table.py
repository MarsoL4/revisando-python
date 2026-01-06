"""
Exercício 6: Tabuada personalizada

1. Peça ao usuário para informar um número inteiro.
2. Imprima a tabuada desse número de 1 a 10 (exemplo: 7 x 1 = 7 ... 7 x 10 = 70).
"""

import os
os.system('cls')

def produto(f1, f2) -> int:
    return f1 * f2
    
while True:
    try:
        multiplicando = int(input("Digite o número: "))
        break  # Encerra quando o valor for válido
    except ValueError:
        print("\nVocê precisa digitar um número inteiro válido. Tente novamente! \n")

for multiplicador in range(0, 11, 1):
    print(f"{multiplicando} x {multiplicador} = {produto(multiplicando, multiplicador)}")