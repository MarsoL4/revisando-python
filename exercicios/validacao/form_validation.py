"""Exercício 3: Validação Simples de Formulário

1. Crie uma função chamada valida_formulario que recebe um dicionário como argumento contendo: nome (string) e idade (inteiro).
2. Implemente as seguintes validações:
   a) O nome não pode ser vazio e deve ter pelo menos 3 caracteres.
   b) A idade deve ser um número inteiro maior que 0 e menor que 150.
3. Faça a função retornar True se os dados forem válidos e False caso contrário.
4. Teste sua função com diferentes combinações de valores válidos e inválidos, como nomes vazios, idade negativa, nomes curtos, etc.

Dica: use condicionais (if/else) e funções como len() para analisar as entradas."""

dados_1 = {'nome': 'Marcos', 'idade': 19}
dados_2 = {'nome': 'Marcos', 'idade': 159}
dados_3 = {'nome': '', 'idade': 25}

def valida_form(dados_form: dict[str, int]):
   if len(dados_form.get('nome', '')) > 3 and 0 < dados_form.get('idade', '') < 150:
      print(f"Dados Recebidos = {dados_form} -> Válidos")
      return True
   else:
      print(f"Dados Recebidos = {dados_form} -> Inválidos")
      return False
      
valida_form(dados_1)
valida_form(dados_2)
valida_form(dados_3)