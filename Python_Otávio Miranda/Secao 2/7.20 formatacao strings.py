"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'João'
idade = 32 # int
altura = 1.80 # float
e_maior = idade > 18 # bool
peso = 80
imc = (peso / altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print(f'{nome} tem  {idade} anos de idade e seu imc é, {imc:.2f}') # formatando usando F-Strings

print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc)) # outra forma de formatação

