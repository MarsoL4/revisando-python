# map1 = map(int, ['1', '2', '3']) # Converte cada string da lista em um inteiro
# print(list(map1)) # Transforma o map em uma lista e imprime: [1, 2, 3]

string1 = "1 2 3 4 5"

string_split = string1.split(" ") # Transforma a string em uma lista de strings
map1 = list(map(int, string_split)) # Converte cada string da lista em um inteiro e armazena em uma nova lista

print(map1)    # -> [1, 2, 3, 4, 5]

print(map1[0]) # -> 1