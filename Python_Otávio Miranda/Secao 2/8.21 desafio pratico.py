"""
*  Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa. 
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e atura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Maria' # str
idade = 40 # int
altura = 1.62 # float
peso = 65.5 # float
ano_atual = 2022 # int
ano_de_nascimento = (ano_atual - idade)
imc = (peso / altura ** 2)

print(f'{nome} tem  {idade} anos de idade, {altura} de altura, {peso} kg, nasceu em {ano_de_nascimento}, e no ano de {ano_atual} desejou saber como estava sua saude e seu imc é, {imc:.2f}.')