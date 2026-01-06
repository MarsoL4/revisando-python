def recebe_numero() -> int:
    while True:
        try:
            number = int(input("Digite o número: "))
            return number
        except ValueError:
            print("\nVocê precisa digitar um número inteiro válido. Tente novamente!\n")

def recebe_frase() -> str:
    while True:
        frase = input("Digite a Frase: ")
        if frase.strip() == "":
            print("\nVocê precisa digitar uma frase não vazia. Tente novamente!\n")
        else:
            return frase