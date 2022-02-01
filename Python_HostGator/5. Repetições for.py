## Repetições - for

cursos = ['Introdução ao wordpress', 
'Criador de Sites',
'Afiliado de Sucesso',
'Introdução ao Googlo ADS',
'E-commerce e Vendas Online',
'Desenvolvimento de Plugins para Wordpress']

for curso in cursos:
    print(curso)

# Criando um Intervalo 
for i in range(len(cursos)):
    print(cursos[i])

# Repetições com while
i = 0 
while i < len (cursos):
    print(cursos[i])
    i = i + 1



