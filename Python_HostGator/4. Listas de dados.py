## Lista de dados

cursos = ['Introdução ao wordpress', 'Criador de Sites', 'Afiliado de Sucesso', 'Introdução ao Googlo ADS', 'E-commerce e Vendas Online', 'Desenvolvimento de Plugins para wordpress']
print (cursos)
print (f"A lista de cursos tem {len(cursos)} cursos")

# Mais uma lista de dados
indice = int(input('Digite um número:\n'))
if indice < len (cursos):
    # estamos seguros
    print(f'o curso no índice {indice} é o "{cursos[indice]}"')
else:
    print (f'O indice {indice} não é válido')
